# Generated by Django 2.0.6 on 2018-06-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0006_auto_20180625_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='pay_interest',
            field=models.FloatField(blank=True, null=True),
        ),
    ]