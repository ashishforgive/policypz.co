# Generated by Django 4.2.5 on 2023-09-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CondidateData',
            fields=[
                ('condidate_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('contact_details', models.TextField(blank=True, default='', null=True)),
                ('electorate', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('age', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('social_media_contact', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('about_me', models.TextField(blank=True, default='', null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartyData',
            fields=[
                ('party_id', models.AutoField(primary_key=True, serialize=False)),
                ('party_name', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('Founder', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('Founded_year', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('current_mps', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('no_of_electorate_held', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('polling_average', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('donations', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('contact_details', models.TextField(blank=True, default='', null=True)),
                ('party_logo', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('about_me', models.TextField(blank=True, default='', null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
