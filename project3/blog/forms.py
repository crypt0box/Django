from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):

    # bootstrap4にコメントフォームを対応させるための記述
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('name', 'text')

