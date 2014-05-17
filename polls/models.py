from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.choice_text

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username