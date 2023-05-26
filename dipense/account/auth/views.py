from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordChangeForm
from box.default import default


class LoginCustom(LoginView):
  """account login class"""
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            "default": default(),
            self.redirect_field_name: self.get_redirect_url(),
            "site": current_site,
            "site_name": current_site.name,
            **(self.extra_context or {})
        })
        return context
        

class LogoutCustom(LoginRequiredMixin ,LogoutView):
  """account logout class"""
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            "default": default(),
            "site": current_site,
            "site_name": current_site.name,
            # "title": _("Logged out"),
            **(self.extra_context or {})
        })
        return context
        

def changePassword(request):
  """change password view"""
  if request.user.is_authenticated:
    form = PasswordChangeForm(user=request.user, data=request.POST or None)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      messages.success(request, f"That sound great {request.user.first_name}, your password has been changed")
      return redirect(reverse("landing"))
    else:
      context = {
        "default": default(),
        "form": form
      }
      return render(request, "account/changePassword.html", context)
  return False
