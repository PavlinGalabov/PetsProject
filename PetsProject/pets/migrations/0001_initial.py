# Generated by Django 5.0.4 on 2024-11-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('personal_photo', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]