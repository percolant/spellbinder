# Generated by Django 2.2.2 on 2019-06-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_auto_20190611_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='colors',
            field=models.ManyToManyField(blank=True, to='cards.Color'),
        ),
    ]
