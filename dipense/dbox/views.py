# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .default import default
from .stats.base import up, stats as stat


@login_required
def stats(request):
    if request.method == 'POST':
        pwd = request.POST['sudo_pwd']
        
        u = up('uptime', '-p', pwd=pwd, req=request)
        s1 = stat('sysinfo', pwd=pwd, req=request)
        s2 = stat('linux')
        context = {
            'uptime': u,
            'sysinfo': s1,
            'linux': s2,
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

        u = up('uptime', '-p', pwd=pwd, req=request)
        s1 = stat('sysinfo', pwd, req=request)
        s2 = stat('linux', pwd, req=request)
        print('pop', u, 123)
        context = {
            'uptime': u,
            'sysinfo': s1,
            'linux': s2,
            # 'uptime': up('uptime'),
            'default': default()
        }
    else:
        context = None
    return render(request, 'pages/vuln.html', context)
