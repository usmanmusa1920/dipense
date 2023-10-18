# -*- coding: utf-8 -*-
import os
import secrets
import subprocess as sp
from pathlib import Path
from django.urls import reverse
from django.contrib import messages
from django.utils.html import format_html
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .default import default
# apt install steghide -y
# xdg-open nothing.jpg
# nano secret.txt
# steghide embed -cf nothing.jpg -ef secret.txt
# passwd: *****
# rm secret.txt
# ls
# steghide ectract -sf nothing.jpg
# passwd: *****
from .forms import SafeImage, UnsafeImage
from .stats.base import auth_sudo
from account.views import picture_name


def catch_crap_safe(request):
    """
    This image_update function it will update the current login user profile image only
    """

    if request.method == 'POST':
        pwd = request.POST['sudo_pwd']
        p = auth_sudo(pwd=pwd, req=request)
        if p:
            print(1)
            return p
        print(2)
        # try:
        #     h = sp.run(f'steghide -h', shell=True)
        #     if h.returncode > 0 or h.returncode != 0:
        #         sp.run(f'apt install steghide -y', shell=True)
        #     return True
        # except:
        #     pass

        form = SafeImage(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            pic_name = picture_name(instance.image.name)
            instance.image.name = pic_name
            instance.save()
            messages.success(request, f'Your profile mask has been updated!')
            return redirect(reverse('account:profile'))
    else:
        form = SafeImage()
        context = {
            'form': form,
            'default': default()
        }
    return render(request, 'pages/crap.html', context)


def catch_crap_unsafe(request):
    """
    This image_update function it will update the current login user profile image only
    """

    try:
        h = sp.run(f'steghide -h', shell=True)
        if h.returncode > 0 or h.returncode != 0:
            sp.run(f'apt install steghide -y', shell=True)
        return True
    except:
        pass
    
    # instead of hard coded the path of our default mask image like:
    # '/home/user/Desktop/dipense/media/anonymous.jpg'
    
    # which will raise issues when deployed in a different environment
    # we use the `Path(__file__).resolve().parent.parent` to give
    # us this module parent of the parent path (which include the machine hostname)
    # the main reason is that of `hostname` since every machine has it own, or
    # user can make his own different, and then join it with `media/anonymous.jpg`
    default_img_path = os.path.join(
        Path(__file__).resolve().parent.parent, 'media/anonymous.jpg')
    
    # Here we check if the request method is POST then it will proceed, else it will return the user to the profile image update page together with his current profile image instance (image)
    if request.method == 'POST':
        form = SafeImage(request.POST, request.FILES, instance=request.user)
        r = request.user.image.path
        if form.is_valid():
            if r != default_img_path:
                if os.path.exists(r):
                    os.remove(r)
            instance = form.save(commit=False)
            pic_name = picture_name(instance.image.name)
            instance.image.name = pic_name
            instance.save()
            messages.success(request, f'Your profile mask has been updated!')
            return redirect(reverse('account:profile'))
    else:
        form = SafeImage(instance=request.user)
        context = {
            'form': form,
            'default': default()
        }
    return render(request, 'pages/crap.html', context)

