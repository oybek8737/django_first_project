# Generated by Django 4.0 on 2023-03-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_alter_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='news/images'),
        ),
    ]
