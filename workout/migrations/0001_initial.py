# Generated by Django 4.0.4 on 2022-05-10 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=256, unique=True)),
                ('exercise_type', models.SmallIntegerField(choices=[(1, 'Pull-ups'), (2, 'Push-ups'), (3, 'Static Elements'), (4, 'Dynamic elements'), (5, 'Compound')])),
                ('level', models.SmallIntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Advanced')])),
                ('description', models.TextField(max_length=1024)),
                ('group_of_muscles', models.CharField(max_length=1024)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
