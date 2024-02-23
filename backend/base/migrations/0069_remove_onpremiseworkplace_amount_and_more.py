# Generated by Django 4.1.5 on 2023-01-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0068_onpremisebooking_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onpremiseworkplace',
            name='amount',
        ),
        migrations.AlterField(
            model_name='onpremisebooking',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='onpremisebooking',
            name='showed_up',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddConstraint(
            model_name='onpremisebooking',
            constraint=models.UniqueConstraint(fields=('workplace', 'slot_start', 'slot_end'), name='booking'),
        ),
    ]
