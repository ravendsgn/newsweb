# Generated by Django 5.1.7 on 2025-03-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravennews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
