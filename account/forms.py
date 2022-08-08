from django import forms
from .models import Message, MessageResponse
    
    
class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ['email', 'text_body']
    
    
# class EmailResponseMessageForm(forms.ModelForm):
#   class Meta:
#     model = MessageResponse
#     fields = ['recepient_email', 'subject', 'message_body']
