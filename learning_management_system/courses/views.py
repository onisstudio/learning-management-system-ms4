from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib import messages
from .models import Course, Lesson, Enrollement

# Create your views here.


def all_courses(request):
    """ A view to show all published courses """

    courses = Course.objects.all().filter(state=1)

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show course details """

    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.all().filter(course_id=course_id)

    context = {
        'course': course,
        'lessons': lessons,
    }

    return render(request, 'courses/course_detail.html', context)


def enroll_to_course(request, course_id):
    """ Enroll user to course """

    course = get_object_or_404(Course, pk=course_id)

    try:
        obj = Enrollement.objects.get(
            user_id=request.user.id, course_id=course_id)

        messages.success(request,
                         f'You are already enrolled to {course.title}')

        return HttpResponse(status=200)

    except Enrollement.DoesNotExist:
        obj = Enrollement(user_id=request.user.id, course_id=course_id)
        obj.save()

        messages.success(request,
                         f'You have successfully enrolled to {course.title}')

        return HttpResponse(status=200)
