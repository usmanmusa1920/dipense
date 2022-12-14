from django.db import models
from django.utils import timezone


class IpPayloadRec(models.Model):
  payload_ip = models.TextField()
  timestamp = models.DateTimeField(default=timezone.now)
  is_seen = models.BooleanField(default=False)
  
  def __str__(self):
    return 'An ip of {} was payloaded on {}'.format(self.payload_ip, self.timestamp)