# Generated by Django 4.2.1 on 2023-05-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.CharField(max_length=1024),
        ),
    ]