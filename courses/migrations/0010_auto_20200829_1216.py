# Generated by Django 3.0.8 on 2020-08-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('courses', '0009_course_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='expense',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(blank=True, to='categories.Category'),
        ),
    ]
