# Generated by Django 4.1.1 on 2022-09-24 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("icsviewer", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Events",
            new_name="Event",
        ),
    ]
