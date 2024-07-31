from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class IpPayloadRec(models.Model):
	payload_ip = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)
	is_seen = models.BooleanField(default=False)
		
	def __str__(self):
		return 'An ip of {} was payloaded on {}'.format(self.payload_ip, self.timestamp)
		
		
class NumPayloadRec(models.Model):
	payload_num = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)
	is_seen = models.BooleanField(default=False)
		
	def __str__(self):
		return 'A search of {} on {}'.format(self.payload_num, self.timestamp)
		

class CrapSafe(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='crap_safe')
	name = models.CharField(max_length=1000000)
	is_craped = models.BooleanField(default=False)
		
	def __str__(self):
		return f'This img is craped = {self.is_craped} (safe)'
