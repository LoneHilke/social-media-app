# Generated by Django 4.0.4 on 2022-04-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.png.url', upload_to='uploads/profile_pictures'),
        ),
    ]
