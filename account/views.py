from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from account.models import Message
from . forms import MessageForm


def message(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"Your message has been sent to DiPense community")
      return redirect(reverse('contact'))
  else:
    form = MessageForm(request.POST)
    messages.success(request, f"Something went wrong try again!")
  return render(request, 'contact.html')


def markMessages(request):
  message_not_read = Message.objects.filter(is_read=False)
  if request.user.is_authenticated:
    for msg in message_not_read:
      msg.is_read = True
      msg.save()
  return redirect(reverse('home'))



def markMessage(request, message_id):
  message_not_read = Message.objects.get(id=message_id)
  if request.user.is_authenticated:
    message_not_read.is_read = True
    message_not_read.save()
  return redirect(reverse('home'))