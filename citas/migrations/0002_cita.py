# Generated by Django 4.1 on 2022-09-02 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("citas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cita",
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
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "servicio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="citas.servicio"
                    ),
                ),
            ],
        ),
    ]
