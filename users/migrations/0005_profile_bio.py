# Generated by Django 4.0.4 on 2022-05-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_preference_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Your bio here!', max_length=150),
        ),
    ]