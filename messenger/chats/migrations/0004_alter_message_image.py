# Generated by Django 4.1.2 on 2022-12-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='ссылка на картинку'),
        ),
    ]
