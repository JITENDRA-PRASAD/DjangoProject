# Generated by Django 3.2.5 on 2021-07-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserloginDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
