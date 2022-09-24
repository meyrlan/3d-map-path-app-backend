# Generated by Django 4.1.1 on 2022-09-23 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('identifier', models.CharField(max_length=255, null=True)),
                ('timestamp', models.IntegerField()),
                ('floor', models.IntegerField(null=True)),
                ('horizontal_accuracy', models.FloatField()),
                ('vertical_accuracy', models.FloatField()),
                ('confidence_in_location_accuracy', models.FloatField()),
                ('activity', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeline', to='user.user')),
            ],
        ),
    ]
