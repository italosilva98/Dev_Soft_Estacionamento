# Generated by Django 3.0.5 on 2020-04-25 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_movmensalisata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovMensalisata',
            new_name='MovMensalista',
        ),
        migrations.RenameField(
            model_name='movmensalista',
            old_name='mensalisata',
            new_name='mensalista',
        ),
    ]
