from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
User = get_user_model()

from .find import ICHECKP
from .track import STRACK
from .trigger import WH


class GEO(ICHECKP):
  pass


class SMTK(STRACK):
  pass


class WH(WH):
  
  def coming(request, pg):
    messages.success(request, f'This page ({pg}) is coming soon!')
    return redirect(reverse('landing'))
