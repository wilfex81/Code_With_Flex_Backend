# Generated by Django 4.0.4 on 2022-04-28 18:45

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_course_rename_communities_communitie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
            ],
            bases=(models.Model, django.db.models.fields.related.ManyToManyField),
        ),
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('specialty', models.CharField(max_length=100)),
                ('community', models.CharField(max_length=100)),
                ('programming_language', models.CharField(max_length=100)),
                ('framework', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('framework', models.CharField(max_length=100)),
                ('programming_language', models.CharField(max_length=100)),
                ('community', models.CharField(max_length=100)),
                ('complexity', models.CharField(max_length=100)),
                ('modules', models.CharField(max_length=50)),
                ('tasks', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
