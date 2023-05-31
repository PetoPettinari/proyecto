from django import forms

from . import models


class Autorform(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        Fields = "__all__"
