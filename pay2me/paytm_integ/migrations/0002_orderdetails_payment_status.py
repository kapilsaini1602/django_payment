# Generated by Django 3.2.9 on 2021-12-02 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm_integ', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]