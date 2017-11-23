from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
designation_choices = (
    (0, "Supervisor"),
    (1, "Project Manager"),
    (2, "Developer"),
    (3, "Client")
)
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    designation = models.IntegerField(default = 3, choices = designation_choices)
    description = models.CharField(max_length=1000, default='')
    city = models.CharField(max_length=200,default='')
    website = models.URLField(null=True, blank=True, default='')
    phone = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    skills = models.CharField(max_length=200, default='')
    emp_rating = models.FloatField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)


    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    feedback = models.CharField(max_length=1000, default='')
    #feedback_time = models.DateTimeField()

class Contact(models.Model):
    selectuser = models.CharField(max_length=1000,default='')



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)
