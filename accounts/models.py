from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=200,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    skills = models.CharField(max_length=200, default='')
    emp_rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)
