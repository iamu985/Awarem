# Generated by Django 4.0.4 on 2022-05-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='downvote',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='upvote',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
