# Generated by Django 2.0.6 on 2018-06-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0003_loantype_client_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='loantype',
            name='penalty',
            field=models.FloatField(default=0),
        ),
    ]
