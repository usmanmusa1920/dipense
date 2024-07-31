from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ImageUpdate(forms.ModelForm):
	class Meta:
		model = User
		fields = ['image']
