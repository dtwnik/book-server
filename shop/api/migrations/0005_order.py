# Generated by Django 4.2.1 on 2023-05-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(blank=True)),
                ('book', models.ManyToManyField(to='api.book')),
            ],
        ),
    ]