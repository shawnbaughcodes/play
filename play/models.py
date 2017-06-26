from __future__ import unicode_literals

from django.db import models
import re, bcrypt
# Create your models here.

# USER MODEL
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# SPORT MODEL
class Sport(models.Model):
    name = models.CharField(mac_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# TEAM MODEL
class Team(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# EVENT MODEL
class Event(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, related_name='users')
    user = models.ForeignKey(User, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# USER_TEAM MODEL
class User_Team(models.Model):
    user = models.ForeignKey(User, related_name='teams')
    team = models.ForeignKey(Team, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# USER_SPORT MODEL
class User_Sport(models.Model):
    user = models.ForeignKey(User, related_name='sports')
    sport = models.ForeignKey(Sport, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# SPORT_TEAM MODEL
class Sport_Team(models.Model):
    user = models.ForeignKey(User, related_name='teams')
    team = models.ForeignKey(Team, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# USER_EVENT TABLE
class User_Event(models.Model):
    user = models.ForeignKey(User, related_name='events')
    event = models.ForeignKey(Event, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
