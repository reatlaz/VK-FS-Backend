# Generated by Django 4.1.2 on 2022-12-24 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_chat_is_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='is_private',
        ),
    ]