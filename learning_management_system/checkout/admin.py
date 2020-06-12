from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('course_price',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created',
                       'order_total', 'original_cart', 'stripe_pid',)

    fields = ('order_number', 'full_name', 'email',
              'phone_number', 'order_total',)

    list_display = ('order_number', 'full_name', 'created', 'order_total',)

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)
