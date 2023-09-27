import os
from pathlib import Path
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import Messages
from . import forms as acc_forms
from dbox.default import default


class Accnt:
    """user account class together with user account utilities"""
    @login_required
    def profile(request):
        context = {
            'default': default()
        }
        return render(request, 'account/profile.html', context)
    
    @login_required
    def image_update(request):
        """
        This image_update function it will update the current login user profile image only
        """

        # instead of hard coded the path of our default mask image like:
        # '/home/usman/Desktop/acode/dipense/media/user.png'
        
        # which will raise issues when deployed in a different environment
        # we use the `Path(__file__).resolve().parent.parent` to give
        # us this module parent of the parent path (which include the machine hostname)
        # the main reason is that of `hostname` since every machine has it own
        
        # and then join it with `media/user.png`
        default_img_path = os.path.join(Path(__file__).resolve().parent.parent, 'media/user.png')
        
        # Here we check if the request method is POST then it will proceed, else it will return the user to the profile image update page together with his current profile image instance (image)
        if request.method == 'POST':
            form = acc_forms.ImageUpdate(request.POST, request.FILES, instance=request.user)
            r = request.user.image.path
            if form.is_valid():
                if r != default_img_path:
                    if os.path.exists(r):
                        os.remove(r)
                form.save()
                messages.success(request, f'Your profile mask has been updated!')
                return redirect(reverse('account:profile'))
        else:
            form = acc_forms.ImageUpdate(instance=request.user)
            context = {
                'form': form,
                'default': default()
            }
        return render(request, 'account/changeImage.html', context)
    
    def signup(request):
        if request.method == 'POST':
            form = acc_forms.SignupForm(request.POST)
            if form.is_valid():
                form.save()
                first_name = form.cleaned_data.get('first_name')
                messages.success(
                    request, f'Welcome {first_name}, your account has been created, you are ready to login!')
                return redirect('account:auth:login')
        else:
            form = acc_forms.SignupForm()
            context = {
                'form':form,
                'default': default()
            }
        return render(request, 'account/signup.html', context)
