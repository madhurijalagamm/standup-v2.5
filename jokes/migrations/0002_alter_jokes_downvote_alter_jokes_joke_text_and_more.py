# Generated by Django 4.1.5 on 2023-02-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokes',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='jokes',
            name='joke_text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jokes',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
