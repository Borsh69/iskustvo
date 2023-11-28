# Generated by Django 4.2.7 on 2023-11-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default='parmesan', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='parmesan', max_length=20),
            preserve_default=False,
        ),
    ]