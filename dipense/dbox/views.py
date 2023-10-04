# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import Messages
from .default import default
from .stats.base import up, stats as stat


@login_required
def stats(request):
    if request.method == 'POST':
        pwd = request.POST['sudo_pwd']
        print(pwd)
        context = {
            'uptime': up('uptime', '-p', pwd=pwd),
            'sysinfo': stat('sysinfo', pwd),
            'linux': stat('linux', pwd),
            # 'uptime': up('uptime'),
            'default': default()
        }
    else:
        context = {
            'linux': stat('linux'),
            'default': default()
        }
    return render(request, 'pages/stats.html', context)


@login_required
def vuln(request):
    if request.method == 'POST':
        pwd = request.POST['sudo_pwd']
        print(pwd)
        context = {
            'uptime': up('uptime', '-p', pwd=pwd),
            'sysinfo': stat('sysinfo', pwd),
            'linux': stat('linux', pwd),
            # 'uptime': up('uptime'),
            'default': default()
        }
    else:
        context = None
    return render(request, 'pages/vuln.html', context)
