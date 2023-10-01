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
    context = {
        'uptime': up('uptime', '-p'),
        'sysinfo': stat('sysinfo'),
        'linux': stat('linux'),
        # 'uptime': up('uptime'),
        'default': default()
    }
    return render(request, 'pages/stats.html', context)


@login_required
def vuln(request):
    context = {
        'uptime': up('uptime', '-p'),
        'sysinfo': stat('sysinfo'),
        'linux': stat('linux'),
        # 'uptime': up('uptime'),
        'default': default()
    }
    return render(request, 'pages/vuln.html', context)
