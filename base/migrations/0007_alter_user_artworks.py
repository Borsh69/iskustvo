# Generated by Django 4.2.7 on 2023-11-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_user_alter_comment_author_delete_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='artworks',
            field=models.ManyToManyField(blank=True, related_name='users', to='base.artwork'),
        ),
    ]