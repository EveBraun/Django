from django import forms
from django.contrib.auth.models import User
from .models import Post


# class PostForm(forms.Form):
#     # author = forms.CharField(max_length=50, label='Автор')
#     title = forms.CharField(max_length=200, label='Title')
#     text = forms.CharField()
#     image = forms.ImageField(required=False)


class PostForm(forms.ModelForm):
    # author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.ModelChoiceField(attrs={"readonly":"readonly"}))
    class Meta:
        model = Post
        fields = "__all__"
        # exclude = ['author']
        