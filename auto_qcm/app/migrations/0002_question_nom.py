# Generated by Django 5.1.1 on 2024-09-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='nom',
            field=models.CharField(default='QuestionQCM', max_length=50),
        ),
    ]
