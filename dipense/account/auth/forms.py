from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()


class PasswordChangeForm(PasswordChangeForm):
  class Meta:
    model = User