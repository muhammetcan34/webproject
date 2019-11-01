from .models import postt, comment
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = postt
        fields = [
            'title',
            'content',
            'image',

        ]

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = [
            'name',
            'content',
        ]

