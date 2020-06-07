from courses.models import Topic


def topics(request):
    """ A view to show all published courses """

    topics = Topic.objects.all().filter(state=1)

    context = {
        'all_topics': topics,
    }

    return context
