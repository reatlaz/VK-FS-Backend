# Generated by Django 4.1.2 on 2022-11-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar_user_bio_user_birth_date_user_last_seen_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_seen',
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default='', max_length=500, verbose_name='о себе'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default='не в сети', max_length=20, null=True, verbose_name='статус'),
        ),
    ]
