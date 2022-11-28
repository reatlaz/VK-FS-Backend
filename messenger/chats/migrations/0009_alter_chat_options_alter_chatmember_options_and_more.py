# Generated by Django 4.1.2 on 2022-11-13 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0008_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.AlterModelOptions(
            name='chatmember',
            options={'verbose_name': 'Участник чата', 'verbose_name_plural': 'Участники чатов'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='прочитано'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='description',
            field=models.CharField(default='', max_length=500, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='name',
            field=models.CharField(max_length=30, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='picture',
            field=models.ImageField(null=True, upload_to='', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='chatmember',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat', verbose_name='чат'),
        ),
        migrations.AlterField(
            model_name='chatmember',
            name='role',
            field=models.CharField(default='member', max_length=20, verbose_name='роль'),
        ),
        migrations.AlterField(
            model_name='chatmember',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat', verbose_name='чат'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=500, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_forwarded',
            field=models.BooleanField(default=False, verbose_name='переслано'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_messages', to='chats.chatmember', verbose_name='отправитель'),
        ),
    ]
