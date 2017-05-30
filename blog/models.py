from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=50)
	text = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	publish_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


	
