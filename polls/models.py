from django.db import models

# Create your models here.

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.choice_text