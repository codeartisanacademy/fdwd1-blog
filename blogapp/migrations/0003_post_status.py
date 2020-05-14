# Generated by Django 3.0.6 on 2020-05-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
