# Generated by Django 3.0 on 2020-02-07 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0002_auto_20200206_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publised',
            new_name='is_published',
        ),
    ]
