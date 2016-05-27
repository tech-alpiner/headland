from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from awesome_avatar.fields import AvatarField
from django.db.models.signals import post_save
from awesome_avatar import forms as avatar_forms

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    avatar = AvatarField(upload_to='avatars', width=100, height=100, null=True)
    bio = models.TextField(null=True)
    github = models.URLField(default='https://github.com')

    def __unicode__(self):
        return "%s's profile" % self.user

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)


class Images(models.Model):
    image = models.FileField(upload_to='media')

    def __unicode__(self):
        return self.image


# Blog modelsd

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return self.title

