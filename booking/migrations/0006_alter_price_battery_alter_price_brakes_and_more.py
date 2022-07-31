# Generated by Django 4.0.5 on 2022-06-29 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_price_regular_alter_price_running_repair_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='battery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.battery'),
        ),
        migrations.AlterField(
            model_name='price',
            name='brakes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.brakes'),
        ),
        migrations.AlterField(
            model_name='price',
            name='cable_replacement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.cable_replacement'),
        ),
        migrations.AlterField(
            model_name='price',
            name='tyres',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.tyres'),
        ),
        migrations.AlterField(
            model_name='price',
            name='washing_and_cleaning',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.washing_and_cleaning'),
        ),
    ]
