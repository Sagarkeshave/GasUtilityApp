# Generated by Django 4.2.2 on 2023-08-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gas_utility_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="supportrepresentative",
            name="email",
            field=models.EmailField(default="support@gmail.com", max_length=254),
        ),
        migrations.AddField(
            model_name="supportrepresentative",
            name="mob_no",
            field=models.IntegerField(default=77777777),
        ),
    ]
