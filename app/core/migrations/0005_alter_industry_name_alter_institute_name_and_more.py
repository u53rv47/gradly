# Generated by Django 4.1.7 on 2023-11-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_rename_university_institute"),
    ]

    operations = [
        migrations.AlterField(
            model_name="industry",
            name="name",
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="institute",
            name="name",
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="major",
            name="name",
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
