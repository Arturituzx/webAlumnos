# Generated by Django 4.2 on 2023-05-11 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_alumno_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='monto',
            field=models.CharField(max_length=1000000, null=True, verbose_name='Monto'),
        ),
    ]
