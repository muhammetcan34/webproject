from .models import postt
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = postt
        fields = [
            'title',
            'content',
        ]