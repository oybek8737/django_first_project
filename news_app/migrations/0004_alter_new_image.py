# Generated by Django 4.0 on 2023-03-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='media/news/images'),
        ),
    ]
