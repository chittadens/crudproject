# Generated by Django 4.0.5 on 2022-06-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10)),
                ('username', models.TextField(max_length=10)),
                ('password', models.TextField(max_length=8)),
                ('confirmpassword', models.TextField(max_length=8)),
            ],
            options={
                'db_table': 'signup',
            },
        ),
    ]
