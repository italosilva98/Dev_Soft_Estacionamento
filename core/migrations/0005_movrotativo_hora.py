# Generated by Django 3.0.5 on 2020-04-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200425_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='movrotativo',
            name='hora',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
