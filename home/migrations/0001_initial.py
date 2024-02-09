# Generated by Django 5.0.2 on 2024-02-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('destination', models.CharField(max_length=200)),
                ('flight_name', models.CharField(max_length=200)),
                ('flight_num', models.CharField(max_length=10)),
                ('eprice', models.IntegerField(null=True)),
                ('dept_time', models.TimeField()),
                ('dest_time', models.TimeField()),
                ('journey_time', models.IntegerField(null=True)),
                ('company', models.CharField(default=' ', max_length=15)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=200)),
                ('hotel_image', models.ImageField(null=True, upload_to='img/')),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_address', models.CharField(max_length=500)),
                ('hotel_price', models.IntegerField(null=True)),
                ('hotel_rating', models.IntegerField(null=True)),
                ('hotel_des', models.CharField(max_length=500)),
                ('rooms', models.IntegerField(default=0)),
            ],
        ),
    ]