# Generated by Django 4.0.4 on 2022-05-14 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_date_published'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set(),
        ),
    ]
