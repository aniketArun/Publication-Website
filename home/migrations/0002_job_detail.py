# Generated by Django 5.1.1 on 2024-09-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=4000)),
                ('salary', models.IntegerField(blank=True)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
