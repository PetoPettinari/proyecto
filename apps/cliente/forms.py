from django import forms

from . import models


class Autorform(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        Fields = "__all__"
