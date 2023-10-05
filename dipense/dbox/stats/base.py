# -*- coding: utf-8 -*-
import os
import shlex
import subprocess as sp
from pathlib import Path
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect


BASE_DIR = Path(__file__).resolve().parent


def up(*args, pwd: str = False, req=None):
    if pwd:
        p = sp.run(f'echo {pwd} | sudo -S uptime', shell=True)
        if p.returncode > 0:
            messages.success(req, 'Something bad with sudo')
            return redirect(reverse('account:landing'))
    # sp.run(['make'])
    up = sp.run(list(args), capture_output=True, text=True).stdout
    return up


def stats(file: str, pwd: str = False, ext: str = 'a', req=None, m: bool = False):
    if pwd:
        p = sp.run(f'echo {pwd} | sudo -S uptime', shell=True)
        if p.returncode > 0:
            if m:
                messages.success(req, 'Something bad with sudo')
            return redirect(reverse('account:landing'))
    if ext == 'a':
        _ext = '.sh'
    elif ext == 'b':
        _ext = '.cpp'
    elif ext == 'c':
        _ext = '.py'
    elif ext == 'd':
        _ext = '.js'
    else:
        raise NotImplemented('Not implemented!')
    sysinfo = os.path.join(BASE_DIR, file + _ext)
    cmd = 'sh ' + sysinfo
    # p = sp.run(shlex.split(cmd), capture_output=True, text=True).stdout
    p = sp.run(cmd, shell=True, capture_output=True, text=True).stdout
    return p
