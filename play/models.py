from __future__ import unicode_literals

from django.db import models
from polymorphic.models import PolymorphicModel
import re, bcrypt
# models below.
# USER MANAGER
class UserManager(models.Manager):
    def register_validate(self, post):
        result = {'errors': []}
        if len(post['first_name']) < 2:
            result['errors'].append('Please enter your full first name.')
        if len(post['last_name']) < 2:
            result['errors'].append('Please enter your full last name.')
        if not re.search(r'\w+\@\w+\.\w+', post.get('email')):
            result['errors'].append('Please enter a valid email.')
        if len(post['password']) < 4:
            result['errors'].append('Please Enter a longer password.')
        if post['password_confirmation'] != post['password']:
            result['errors'].append('Passwords must match')
        else:
            return
        return result
    # END REGISTER VALIDATE
    def create_user(self, post):
        user = User.objects.create(first_name=post.get('first_name'), last_name=post.get('last_name'), email=post.get('email'), password=bcrypt.hashpw(post.get('password').encode(), bcrypt.gensalt()))
        return user
    # END CREATE USER
    def login_validate(self, post):
        user = User.objects.filter(email=post.get('email')).first()
        if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'message': 'Please enter valid credentials'}
    # END LOGIN VALIDATE
    def login(self, request, user):
        if('user_id' not in request.session):
            request.session['user_id'] = user.id
    # END LOGIN
# END USER MANAGER

# USER MODEL
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=1000)
    friend = models.ManyToManyField('self', related_name='friends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# SPORT MODEL
class Sport(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='sports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# TEAM MODEL
class Team(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="teams")
    sport = models.ForeignKey(Sport, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# EVENT MODEL
class Event(models.Model):
    name = models.CharField(max_length=255)
    sport = models.ForeignKey(Sport, related_name='events')
    user = models.ForeignKey(User, related_name='user_events')
    users = models.ManyToManyField(User, related_name='events')
    teams = models.ManyToManyField(Team, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# CHATROOM MODEL
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chatroom(PolymorphicModel):
    message = models.ForeignKey(Message, related_name='messages')
    users = models.ManyToManyField(User, related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EventChatroom(Chatroom):
    event = models.ForeignKey(Event, related_name='messages')
