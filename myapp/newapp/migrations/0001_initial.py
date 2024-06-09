# Generated by Django 5.0.6 on 2024-06-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hall',
            fields=[
                ('hall_id', models.AutoField(primary_key=True, serialize=False)),
                ('hall_name', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('locality', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1500)),
                ('contact_no', models.CharField(max_length=500)),
                ('capacity', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('manager_name', models.CharField(max_length=500)),
                ('hall_email_id', models.CharField(max_length=500)),
                ('cost', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='Photos/')),
            ],
        ),
    ]
