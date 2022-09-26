# Generated by Django 4.1.1 on 2022-09-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amcCargoApp', '0005_lahoreaccount_delivery_day_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lahoreaccount',
            old_name='Recovery_Amount',
            new_name='Amount',
        ),
        migrations.AddField(
            model_name='lahoreaccount',
            name='Payment_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
