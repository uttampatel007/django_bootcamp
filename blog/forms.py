from django import forms
from blog.models import Post

# model form

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'author']

