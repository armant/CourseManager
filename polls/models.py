from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Choice(models.Model):
    new_course = models.CharField(max_length=200, null=True, blank=True)
    courses_taking = models.ManyToManyField(User)
    def __unicode__(self):
        return self.new_course

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        if self.user.first_name + ' ' + self.user.last_name != ' ':
        	return self.user.first_name + ' ' + self.user.last_name + ' ' + str(self.birthday)
        else:
        	return self.user.username