# Generated by Django 4.1.7 on 2023-03-09 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galery", "0005_photography_published_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photography",
            name="published_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
