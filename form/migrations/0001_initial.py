# Generated by Django 4.2.1 on 2023-05-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookacall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('business_type', models.CharField(max_length=2500)),
                ('business_name', models.CharField(max_length=2500)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('business_detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('contact_matter', models.TextField()),
            ],
        ),
    ]
