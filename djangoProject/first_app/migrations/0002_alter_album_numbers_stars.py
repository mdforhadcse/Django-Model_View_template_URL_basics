# Generated by Django 4.0.5 on 2022-08-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='numbers_stars',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]