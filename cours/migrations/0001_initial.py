# Generated by Django 5.1.1 on 2024-09-16 20:57

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('programme', models.CharField(choices=[('Bachelor', 'bachelor'), ('Master', 'master'), ('PhD', 'phd'), ('DEC', 'dec'), ('AEC', 'aec')], max_length=10)),
                ('niveau', models.CharField(choices=[('1ere année', '1ère année'), ('2eme année', '2ème année'), ('3eme année', '3ème année'), ('4eme année', '4ème année')], max_length=10)),
                ('credits', models.IntegerField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('jour', models.CharField(choices=[('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'), ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi')], max_length=10)),
                ('heure_debut', models.TimeField(default=django.utils.timezone.now)),
                ('heure_fin', models.TimeField(default=django.utils.timezone.now)),
                ('enseignant', models.ForeignKey(limit_choices_to={'type_utilisateur': 'Enseignant'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prerequis', models.ManyToManyField(blank=True, to='cours.cours')),
            ],
        ),
    ]
