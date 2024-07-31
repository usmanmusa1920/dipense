# -*- coding: utf-8 -*-
# This is `dbox` (DiPenseBox) package
from abc import abstractmethod, ABCMeta
from typing import overload
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from .find import ICHECKP
from .track import STRACK
from .trigger import WH


User = get_user_model()


class GEO(ICHECKP): ...
class SMTK(STRACK): ...
class WH(WH):
	def coming(request, pg):
		messages.warning(
			request, format_html('Sorry this page <a href="{}" class="peace">&nbsp;{}&nbsp;</a> is under development', request.path_info, pg))
		return redirect(reverse('account:landing'))
		
	@overload
	def _que(self, val: int) -> int: ...
	def _que(self, val: float) -> float: ...
	def _que(self, val: str) -> str: ...
	def _que(self, val: bytes) -> bytes: ...
	def _que(self, val: None) -> None: ...
	

class Danger(metaclass=ABCMeta):
	@abstractmethod
	def danger_up(self): ...
	@abstractmethod
	def danger_down(self): ...
	@abstractmethod
	def danger_left(self): ...
	@abstractmethod
	def danger_right(self): ...

class Chaos(Danger):
	def danger_up(self):
		return 'Danger up'
	def danger_down(self):
		return 'Danger down'
	def danger_left(self):
		return 'Danger left'
	def danger_right(self):
		return 'Danger right'
		
# ch = Chaos()
# print(ch.abstractName())
