from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL


class UserAccountManager(BaseUserManager):
  def create_user(self, first_name, last_name, username, email, password=None):
    if not first_name:
      raise ValueError('Your first name is required')
    if not last_name:
      raise ValueError('Your last name is required')
    if not username:
      raise ValueError('Your username is required')
    if not email:
      raise ValueError('You must provide your email address')
    if not password:
      raise ValueError('You must include password')
    user = self.model(
      first_name = first_name,
      last_name = last_name,
      username = username,
      email = self.normalize_email(email),
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, first_name, last_name, username, email, password=None):
    user = self.create_user(
      first_name = first_name,
      last_name = last_name,
      username = username,
      email = self.normalize_email(email),
      password = password,
    )
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
    return user
  
  
  
class UserAccount(AbstractBaseUser):
  first_name = models.CharField(max_length=100, unique=False)
  last_name = models.CharField(max_length=100, unique=False)
  username = models.CharField(max_length=255, unique=True)
  email = models.EmailField(max_length=255, unique=True)
  image_url = models.CharField(max_length=1000000, blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  
  objects = UserAccountManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
  
  def __str__(self):
    return self.username
  
  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True
  
  
  
class Message(models.Model):
  email = models.CharField(max_length=255, blank=False, null=False)
  text_body = models.TextField(blank=False, null=False)
  timestamp = models.DateTimeField(default=timezone.now)
  is_read = models.BooleanField(default=False)
  
  def __str__(self):
    return 'Message sent from {} on {}'.format(self.email, self.timestamp)
  
  
  
class MessageResponse(models.Model):
  response_to = models.ForeignKey(Message, on_delete=models.CASCADE)
  recepient_email = models.CharField(max_length=255, blank=False, null=False)
  subject = models.CharField(max_length=255, blank=False, null=False)
  message_body = models.TextField(blank=False, null=False)
  timestamp = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return 'Reply message was sent to {} on {}'.format(self.recepient_email, self.timestamp)
  
  
  
class SiteToGet(models.Model):
  site = models.CharField(max_length=255)
  
  def __str__(self):
    return 'A site ({}) to get'.format(self.site)