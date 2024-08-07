# -*- coding: utf-8 -*-
import os
import shutil
import secrets
import subprocess as sp
from pathlib import Path
from datetime import datetime
from django.urls import reverse
from django.contrib import messages
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .default import default
from .models import CrapSafe
from .forms import SafeImage
from .stats.base import auth_sudo
from account.views import picture_name


today = datetime.today()


def age():
	for i in os.listdir():
		if os.path.isfile(i):
			negators = [
				'auto.sh',
				'config.json',
				'db.sqlite3',
				'dump.json',
				'manage.py',
				'requirements.txt'
			]
			if os.path.basename(i) not in negators:
				mtime = datetime.fromtimestamp(os.stat(i)[8])
				filetime = mtime - today
				if abs(filetime.days) <= 3:
					# print(mtime,f" {os.path.basename(i)} older {abs(filetime.days)} days")
					# print(mtime.year, mtime.month, mtime.day, mtime.hour, mtime.minute, mtime.second, 'm')
					# print(today.year, today.month, today.day, today.hour, today.minute, today.second, 't')
					# print()
					directory = os.path.join(
						Path(__file__).resolve().parent.parent, 'sec')
					timestamp = datetime.now()
					# move any recent (1 - 3 days) files into sec folder, using shutil.
					shutil.move(os.path.basename(i), directory + '/' + os.path.basename(i))
				else:
					os.remove(i)


@login_required
def catch_crap_safe(request):
	"""This image_update function it will update the current login user profile image only"""

	if request.method == 'POST':
		pwd = request.POST['sudo_pwd']
		file_enc_pwd = request.POST['file_enc_pwd']
		secret_file_path = request.POST['secret_file_path']
		p = auth_sudo(pwd=pwd, req=request)
		if p:
			return p
		
		form = SafeImage(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			pic_name = picture_name(instance.image.name)
			instance.image.name = pic_name
			instance.owner = request.user
			instance.name = pic_name
			instance.save()
			pt = instance.image.path
			sp.run(f'echo {pwd} | sudo -S steghide embed -cf {pt} -ef {secret_file_path} -p {file_enc_pwd}', shell=True, capture_output=True)
			messages.success(request, f'You just add crap')
			return redirect(reverse('account:profile'))
	else:
		form = SafeImage()
		context = {
			'form': form,
			'default': default()
		}
	return render(request, 'pages/crap.html', context)


@login_required
def catch_crap_unsafe(request):
	"""This image_update function it will update the current login user profile image only"""

	uncraped = CrapSafe.objects.filter(is_craped=False)
	if request.method == 'POST':
		g_pwd = request.POST['guess_pass']
		fn = request.POST['sel_img']

		fn_splt = fn.split('/')[3]
		target = CrapSafe.objects.filter(name=fn_splt).first()
		if not target:
			messages.warning(request, 'Query not found')
			return redirect('/')
		rp = target.image.path
		if os.path.exists(rp):
			y = sp.run(
				f'steghide extract -sf {rp} -p {g_pwd}', shell=True, capture_output=True)
			if y.returncode > 0 or y.returncode != 0:
				messages.warning(request, 'Invalid passphrase!')
				return redirect('trigger:crap_unsafe')
		# target.is_craped = True
		# target.save()
		age()
		messages.success(request, f'You just craped!!!')
		return redirect(reverse('account:profile'))
	context = {
		'uncraped': uncraped,
		'default': default(),
	}
	return render(request, 'pages/uncrap.html', context)
