# Generated by Django 5.1.2 on 2024-10-23 20:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_jobmodel_posted_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobApplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, max_length=200, null=True, upload_to='media/resume')),
                ('cover', models.TextField(blank=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('work_experience', models.CharField(blank=True, max_length=100, null=True)),
                ('skills', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin_url', models.URLField(blank=True, max_length=100, null=True)),
                ('expected_salary', models.PositiveIntegerField(blank=True, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.jobmodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
