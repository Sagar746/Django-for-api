# Generated by Django 3.2.11 on 2022-01-30 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_alter_todo_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
