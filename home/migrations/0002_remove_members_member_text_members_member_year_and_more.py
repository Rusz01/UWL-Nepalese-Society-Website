# Generated by Django 5.0.1 on 2024-03-16 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='member_text',
        ),
        migrations.AddField(
            model_name='members',
            name='member_year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Member_detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='image')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
                ('details_text', models.CharField(blank=True, max_length=150, null=True)),
                ('socials_link', models.URLField(blank=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.members')),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
