from django.db import models
import datetime
from django.conf import settings

STATE_CHOICES = (
    ('1', 'Published'),
    ('0', 'Unpublished'),
)


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                             on_delete=models.SET_NULL, editable=False)
    title = models.CharField(max_length=254)
    alias = models.CharField(max_length=50)
    description = models.TextField()
    topic = models.ForeignKey(
        'Topic', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='courses', null=True, blank=True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='1')

    def get_price(self):
        if self.price > 0:
            readable_price = str(self.price) + ' £'
        else:
            readable_price = 'Free'
        return readable_price

    def get_enrollement(self):
        obj = Enrollement.objects.get(
            user_id=self.user.id, course_id=self.id)

        if obj:
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        """ Update timestamp on save """

        if not self.id:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, null=False, blank=False,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    description = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Lesson id:{self.id} on {self.course.title}'


class Topic(models.Model):
    title = models.CharField(max_length=254)
    alias = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='1')

    def __str__(self):
        return self.title

    def get_description(self):
        return self.description


class Enrollement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                             on_delete=models.SET_NULL, editable=False)
    course = models.ForeignKey(Course, null=False, blank=False,
                               on_delete=models.CASCADE)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='1')
