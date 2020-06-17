# Generated by Django 3.0.5 on 2020-06-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shubham', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbloptions',
            fields=[
                ('optionid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=550, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('alternet_number', models.CharField(max_length=16)),
                ('facebook_link', models.CharField(max_length=300)),
                ('twitter_link', models.CharField(max_length=300)),
                ('youtube_link', models.CharField(max_length=300)),
                ('instagram_link', models.CharField(max_length=300)),
                ('linkedin_link', models.CharField(max_length=300)),
                ('github_link', models.CharField(max_length=300)),
                ('google_ver_id', models.CharField(blank=True, max_length=50, null=True)),
                ('googleana_script', models.TextField(blank=True, null=True)),
                ('facebook_script', models.TextField(blank=True, null=True)),
                ('logo', models.CharField(blank=True, max_length=150, null=True)),
                ('favicon', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=150, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
