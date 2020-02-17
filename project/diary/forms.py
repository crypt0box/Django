from django import forms
from .models import Day


class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'  # フィールドを指定したいときは('title', 'text', 'date')のように書く
