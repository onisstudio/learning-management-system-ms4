import uuid
import datetime

from django.db import models
from django.db.models import Sum

from courses.models import Course

STATE_CHOICES = (
    ('1', 'Published'),
    ('0', 'Unpublished'),
)


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='1')
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def get_order_total(self):
        if self.order_total > 0:
            readable_price = str(self.order_total) + ' £'
        else:
            readable_price = 'Free'
        return readable_price

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update order total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(Sum('course_price'))[
            'course_price__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        """ Update timestamp on save """

        if not self.id:
            self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    course = models.ForeignKey(
        Course, null=False, blank=False, on_delete=models.CASCADE)
    course_price = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.course_price = self.course.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.course.title} on order {self.order.order_number}'
