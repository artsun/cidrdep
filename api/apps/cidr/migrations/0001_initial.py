# Generated by Django 2.1.5 on 2019-01-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iprange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_ip', models.CharField(max_length=255)),
                ('last_ip', models.CharField(max_length=255)),
            ],
        ),
    ]