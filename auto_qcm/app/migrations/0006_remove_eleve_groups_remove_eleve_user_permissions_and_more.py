# Generated by Django 5.1.1 on 2024-09-16 08:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_qcm_creator_alter_question_creator_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='eleve',
            name='user_permissions',
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('Etudiant', 'Etudiant'), ('Enseignant', 'Enseignant')], default='Etudiant', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='utilisateur_groups', to='auth.group', verbose_name='groups')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='utilisateur_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
        ),
        migrations.AlterField(
            model_name='reponseqcm',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reponses_qcm', to='app.utilisateur'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Eleve',
        ),
    ]
