# Generated by Django 3.2.7 on 2021-10-01 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='down_persons',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='floor',
            name='floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='floor',
            name='up_persons',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='floor',
            name='waiting_down',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='floor',
            name='waiting_up',
            field=models.IntegerField(default=-1),
        ),
    ]
