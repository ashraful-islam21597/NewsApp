from django.forms import forms, ModelForm

from articles.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)