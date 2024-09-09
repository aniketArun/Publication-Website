# Generated by Django 5.1.1 on 2024-09-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_coverform'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('language_of_book', models.CharField(max_length=100)),
                ('book', models.FileField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('budget', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
