# Generated by Django 5.1.1 on 2024-09-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
    ]
