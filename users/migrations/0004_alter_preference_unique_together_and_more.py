# Generated by Django 4.0.4 on 2022-05-14 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_post_alter_profile_profile_picture_preference'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='preference',
            name='post',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]
