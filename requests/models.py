from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Request(models.Model):
	"""(represents a Request for data)"""
	title = models.CharField(blank=True, max_length=100)
	description = models.TextField(blank=True)
	tags  = TaggableManager()
	notify_on_comment = models.BooleanField(default=True)
	date_created = models.DateTimeField()
	date_modified = models.DateTimeField()
	created_by = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

	def save(self):
	    if self.date_created == None:
		    self.date_created = datetime.now()
	    self.date_modified = datetime.now()
	    super(Request, self).save()

	class Admin:
		list_display = ('',)
		search_fields = ('',)

	def __unicode__(self):
		return u"Request"
