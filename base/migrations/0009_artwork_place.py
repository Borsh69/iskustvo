# Generated by Django 4.2.7 on 2023-11-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_artwork_object3d_exhibition'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='place',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
