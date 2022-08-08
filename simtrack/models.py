from django.db import models
from django.utils import timezone


class NumPayloadRec(models.Model):
  payload_num = models.TextField()
  timestamp = models.DateTimeField(default=timezone.now)
  is_seen = models.BooleanField(default=False)
  
  def __str__(self):
    return 'A search of {} on {}'.format(self.payload_num, self.timestamp)