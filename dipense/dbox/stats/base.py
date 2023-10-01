# -*- coding: utf-8 -*-
import os
import shlex
import subprocess as sp
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
# print(BASE_DIR)


def up(*args):
    sp.run(['make'])
    up = sp.run(list(args), capture_output=True, text=True).stdout
    return up


def stats(file: str, ext: str = 'a'):
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
    cmd = "sh " + sysinfo
    p = sp.run(shlex.split(cmd), capture_output=True, text=True).stdout
    return p
