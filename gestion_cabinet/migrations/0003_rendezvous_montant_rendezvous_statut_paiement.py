# Generated by Django 5.0.2 on 2025-05-31 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_cabinet', '0002_customuser_photo_profil_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='montant',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='statut_paiement',
            field=models.CharField(choices=[('EN_ATTENTE', 'En attente'), ('REGLE', 'Réglé')], default='EN_ATTENTE', max_length=20),
        ),
    ]
