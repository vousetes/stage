# Generated by Django 5.1.1 on 2024-09-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_alter_utilisateur_type_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='type_utilisateur',
            field=models.CharField(choices=[('adminitration_menbre', "Menbre d'administration"), ('Etudiant', 'Etudiant'), ('Enseignant', 'Enseignant')], default='Etudiant', max_length=255),
        ),
    ]
