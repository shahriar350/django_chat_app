# Generated by Django 3.2.4 on 2021-07-05 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='receiver',
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rooms', to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(related_name='room_members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='room_messages', to='chat_app.room'),
            preserve_default=False,
        ),
    ]