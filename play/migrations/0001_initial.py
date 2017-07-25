# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-24 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='play.Sport')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=500)),
                ('password', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friend', models.ManyToManyField(related_name='_user_friend_+', to='play.User')),
            ],
        ),
        migrations.CreateModel(
            name='EventChatroom',
            fields=[
                ('chatroom_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='play.Chatroom')),
            ],
            options={
                'abstract': False,
            },
            bases=('play.chatroom',),
        ),
        migrations.AddField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(related_name='teams', to='play.User'),
        ),
        migrations.AddField(
            model_name='sport',
            name='users',
            field=models.ManyToManyField(related_name='sports', to='play.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='play.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='play.Sport'),
        ),
        migrations.AddField(
            model_name='event',
            name='teams',
            field=models.ManyToManyField(related_name='events', to='play.Team'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_events', to='play.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(related_name='events', to='play.User'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='play.Message'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_play.chatroom_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(related_name='chatrooms', to='play.User'),
        ),
        migrations.AddField(
            model_name='eventchatroom',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='play.Event'),
        ),
    ]
