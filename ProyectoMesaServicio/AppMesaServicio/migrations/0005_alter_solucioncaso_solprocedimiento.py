# Generated by Django 4.2.13 on 2024-06-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMesaServicio', '0004_alter_caso_casestado_alter_caso_casusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solucioncaso',
            name='solProcedimiento',
            field=models.TextField(db_comment='Texto del procedimiento realizado en la solución del caso', max_length=2000),
        ),
    ]
