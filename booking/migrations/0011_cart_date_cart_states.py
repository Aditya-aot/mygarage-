# Generated by Django 4.0.5 on 2022-07-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='states',
            field=models.BooleanField(null=True),
        ),
    ]