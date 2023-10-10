# -*- coding: utf-8 -*-
from django.urls import reverse
from django.contrib import messages
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .default import default
from .stats.base import up, stats, sys_proc


@login_required
def stats_view(request):
    if request.method == 'POST':
        pwd = request.POST['sudo_pwd']
        
        u = up('uptime', '-p', pwd=pwd, req=request)
        s1 = stats('sysinfo', pwd=pwd, req=request)
        s2 = stats('baby')
        context = {
            'uptime': u,
            'sysinfo': s1,
            'baby': s2,
            'sys_proc': sys_proc(),
            # 'uptime': up('uptime'),
            'default': default()
        }
    else:
        context = {
            'baby': stats('baby'),
            'sys_proc': sys_proc(),
            'default': default()
        }
    return render(request, 'pages/stats.html', context)


@login_required
def vuln(request):
    messages.success(
        request, format_html('Sorry this page <a href="{}" class="peace">&nbsp;vuln</a> is under development', reverse('trigger:vuln')))
    return redirect('trigger:stats')
    context = {
        'None': None,
    }
    return render(request, 'pages/vuln.html', context)
