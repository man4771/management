# Generated by Django 4.1.1 on 2022-10-15 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Master",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=12)),
                ("Isactive", models.BooleanField(default=False)),
            ],
            options={"db_table": "master",},
        ),
        migrations.CreateModel(
            name="UserRole",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Role", models.CharField(max_length=10)),
            ],
            options={"db_table": "userole",},
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(blank=True, default="", max_length=255)),
                ("Date_of_birth", models.DateField()),
                ("Date_of_joining", models.DateField()),
                ("Address", models.TextField()),
                ("compensation", models.CharField(max_length=255)),
                (
                    "Master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="instituteapp.master",
                    ),
                ),
            ],
            options={"db_table": "teacher",},
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(blank=True, default="", max_length=255)),
                ("Date_of_birth", models.DateField()),
                ("Date_of_joining", models.DateField()),
                ("Address", models.TextField()),
                (
                    "Gender",
                    models.CharField(
                        choices=[("m", "male"), ("f", "female")], max_length=5
                    ),
                ),
                ("Roll_number", models.IntegerField()),
                (
                    "Master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="instituteapp.master",
                    ),
                ),
            ],
            options={"db_table": "student",},
        ),
        migrations.AddField(
            model_name="master",
            name="UserRole",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="instituteapp.userrole"
            ),
        ),
    ]
