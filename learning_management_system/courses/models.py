from django.db import models

STATE_CHOICES = (
    ('1', 'Published'),
    ('0', 'Unpublished'),
)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    title = models.CharField(max_length=254)
    alias = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='1')

    def __str__(self):
        return self.title

    def get_description(self):
        return self.description


class Course(models.Model):
    title = models.CharField(max_length=254)
    alias = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.TextField()

    def __str__(self):
        return self.title
