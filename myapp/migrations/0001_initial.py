# Generated by Django 3.1.2 on 2020-12-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('whatsapp', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('bloodgroup', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('recent', models.CharField(max_length=100)),
                ('frequent', models.CharField(max_length=100)),
                ('monetary', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('pid', models.IntegerField()),
                ('posttitle', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]