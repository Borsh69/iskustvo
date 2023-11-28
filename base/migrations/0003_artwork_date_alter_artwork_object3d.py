# Generated by Django 4.2.7 on 2023-11-28 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_login_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='object3d',
            field=models.FileField(blank=True, upload_to='files/', verbose_name='3D файл'),
        ),
    ]
