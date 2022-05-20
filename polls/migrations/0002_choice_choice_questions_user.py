# Generated by Django 4.0.4 on 2022-05-19 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice',
            field=models.CharField(default='Choice', max_length=250),
        ),
        migrations.AddField(
            model_name='questions',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]