# Generated by Django 5.0.2 on 2024-03-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='EventCreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recentevent',
            name='RecentEventCreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
