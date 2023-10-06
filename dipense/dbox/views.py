# -*- coding: utf-8 -*-
from django.urls import reverse
from django.contrib import messages
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .default import default
from .stats.base import up, stats as stat


@login_required
def stats(request):
    messages.success(
        request, format_html('Thank you, follow <a href="{}" class="peace">&nbsp;link</a>', reverse('account:profile')))
    if request.method == 'POST':
        pwd = request.POST['sudo_pwd']
        
        u = up('uptime', '-p', pwd=pwd, req=request)
        s1 = stat('sysinfo', pwd=pwd, req=request)
        s2 = stat('baby')
        context = {
            'uptime': u,
            'sysinfo': s1,
            'baby': s2,
            # 'uptime': up('uptime'),
            'default': default()
        }
    else:
        context = {
            'baby': stat('baby'),
            'default': default()
        }
    return render(request, 'pages/stats.html', context)


@login_required
def vuln(request):
    if request.method == 'POST':
        pwd = request.POST['sudo_pwd']
        u = up('uptime', '-p', pwd=pwd, req=request)
        s1 = stat('sysinfo', pwd, req=request)
        s2 = stat('baby', pwd, req=request)
        context = {
            'uptime': u,
            'sysinfo': s1,
            'baby': s2,
            # 'uptime': up('uptime'),
            'default': default()
        }
    else:
        context = None
    return render(request, 'pages/vuln.html', context)
