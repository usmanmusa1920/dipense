"""dipense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from datetime import datetime
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from simtrack import views as s_views
from account import views as a_views
from icheckp import views as i_views


class LoginCustom(LoginView):
  def get_context_data(self, **kwargs):
        the_year = datetime.utcnow().year
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'the_year':the_year,
            'site': current_site,
            'site_name': current_site.name,
            **(self.extra_context or {})
        })
        return context
      
      
class LogoutCustom(LoginRequiredMixin ,LogoutView):
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            'site': current_site,
            'site_name': current_site.name,
            # 'title': _('Logged out'),
            **(self.extra_context or {})
        })
        return context

urlpatterns = [
    path('', s_views.home, name='home'),
    path('simtrack', s_views.simtrack, name='simtrack'),
    path('icheckp', i_views.icheckp, name='icheckp'),
    path('about/', s_views.about, name='about'),
    path('contact/', s_views.contactUs, name='contact'),
    path('message/', a_views.message, name='message'),
    path('mark_message/<int:message_id>/', a_views.markMessage, name='mark_message'),
    path('mark_messages/', a_views.markMessages, name='mark_messages'),
    path('7ecf9a02ee68bcbc266ec5261d2f8d83d92dd61b4a646abc6df49b28e7af/', admin.site.urls),
    path('login/', LoginCustom.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutCustom.as_view(template_name='login.html'), name='logout'),
]
