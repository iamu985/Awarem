from django.forms import ModelForm
from .models import Questions


class PollCreateQuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question']





