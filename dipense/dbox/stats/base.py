# -*- coding: utf-8 -*-
import os
import shlex
import subprocess as sp
from pathlib import Path
from django.urls import reverse
from django.contrib import messages
from django.utils.html import format_html
from django.shortcuts import redirect
import psutil


BASE_DIR = Path(__file__).resolve().parent


def up(*args, pwd: str = False, req=None):
    if pwd:
        p = sp.run(f'echo {pwd} | sudo -S uptime', shell=True)
        if p.returncode > 0 or p.returncode != 0:
            messages.success(
                req, format_html('Something bad, review sudo credentials, <a href="{}" class="peace">&nbsp;landing</a>', reverse('account:landing')))
            return redirect(reverse('account:landing'))
    up = sp.run(list(args), capture_output=True, text=True).stdout
    return up


def stats(file: str, pwd: str = False, ext: str = 'a', req=None, m: bool = False):
    if pwd:
        p = sp.run(f'echo {pwd} | sudo -S uptime', shell=True)
        if p.returncode > 0 or p.returncode != 0:
            if m:
                messages.success(
                    req, format_html('Something bad, review sudo credentials, <a href="{}" class="peace">&nbsp;landing</a>', reverse('account:landing')))
            return redirect(reverse('account:landing'))
    if ext == 'a':
        _ext = '.sh'
    else:
        raise NotImplemented('Not implemented!')
    sysinfo = os.path.join(BASE_DIR, file + _ext)
    cmd = 'sh ' + sysinfo
    # p = sp.run(shlex.split(cmd), capture_output=True, text=True).stdout
    p = sp.run(cmd, shell=True, capture_output=True, text=True).stdout
    return p


def sys_proc():
    l = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        l.append(proc.info)
    return l
