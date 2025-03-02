# Generated by Django 5.0.6 on 2025-02-07 22:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_studentanswer_is_attempted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_code', models.CharField(blank=True, max_length=20, null=True)),
                ('recipient', models.TextField(blank=True, null=True)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.DurationField()),
            ],
        ),
    ]
