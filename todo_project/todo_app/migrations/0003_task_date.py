# Generated by Django 4.1.5 on 2023-01-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0002_rename_name_task_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="2000-06-27"),
            preserve_default=False,
        ),
    ]
