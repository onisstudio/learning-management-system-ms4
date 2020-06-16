from django import forms
from .models import Course, Topic


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topics = Topic.objects.all().filter(state=1)
        topic_aliases = [(topic.id, topic.title) for topic in topics]

        self.fields['topic'].choices = topic_aliases
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
