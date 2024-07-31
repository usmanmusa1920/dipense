from django import forms
from .models import CrapSafe


class SafeImage(forms.ModelForm):
	class Meta:
		model = CrapSafe
		fields = ['image']
