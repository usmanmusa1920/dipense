from django import forms
from .models import CrapSafe, CrapUnsafe


class SafeImage(forms.ModelForm):
    class Meta:
        model = CrapSafe
        fields = ['image']


class UnsafeImage(forms.ModelForm):
    class Meta:
        model = CrapUnsafe
        fields = ['image']
