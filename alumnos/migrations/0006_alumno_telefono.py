# Generated by Django 4.2 on 2023-05-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_alter_alumno_fechanacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=9, null=True, verbose_name='Telefono'),
        ),
    ]
