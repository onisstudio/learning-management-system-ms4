from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

# Create your views here.


def all_courses(request):
    """ A view to show all courses, including sorting and search queries """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show course details """

    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.all()

    context = {
        'course': course,
        'lessons': lessons,
    }

    return render(request, 'courses/course_detail.html', context)
