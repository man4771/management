# Generated by Django 4.1.1 on 2022-12-02 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("instituteapp", "0008_alter_userrole_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Viewer",
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
                (
                    "UserRole",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="instituteapp.userrole",
                    ),
                ),
            ],
            options={"db_table": "viewer",},
        ),
    ]
