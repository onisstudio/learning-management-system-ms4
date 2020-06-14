from django.shortcuts import render, get_object_or_404, HttpResponse
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Course, Lesson, Enrollement, Topic
from .forms import CourseForm


def all_courses(request):
    """ A view to show all published courses """

    courses = Course.objects.all().filter(state=1)

    query = None
    topics = None

    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                courses = courses.annotate(lower_name=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            courses = courses.order_by(sortkey)

        if 'topic' in request.GET:
            topics = request.GET['topic'].split(',')
            courses = courses.filter(topic__title__in=topics)
            topics = Topic.objects.filter(title__in=topics)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "No search criteria entered! Try again please.")
                return redirect(reverse('courses'))

            queries = Q(title__icontains=query) | Q(
                description__icontains=query)
            courses = courses.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'courses': courses,
        'search_term': query,
        'current_topics': topics,
        'current_sorting': current_sorting,
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


def add_course(request):
    """ Add a course """
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course successfully added!')
            return redirect(reverse('add_course'))
        else:
            messages.error(
                request, 'Course not added. Please ensure the form is valid.')
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
