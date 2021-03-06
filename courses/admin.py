from django.contrib import admin
from .models import Course, Topic, Lesson

# Register your models here.


class LessonAdminInline(admin.TabularInline):
    model = Lesson


class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonAdminInline,)

    readonly_fields = ['user_profile', 'created', 'updated']

    list_display = (
        'title',
        'topic',
        'price',
        'id',
    )

    ordering = ('id',)

    def save_model(self, request, obj, form, change):
        obj.save()


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
