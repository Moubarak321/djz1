# Generated by Django 4.0.4 on 2022-06-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_catégorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catégorie',
            field=models.CharField(choices=[('Bébé', 'Bébé'), ('Entretien et nettoyage', 'Entretien et nettoyage'), ('Sport', 'Sport'), ('Jeux_videos', 'Jeux Vidéos'), ('Jeux_et_Jouets', 'Jeux et Jouets'), ('Electroménagers', 'Electroménagers'), ('Smartphones_et_objets_connectés', 'Smartphones et objets connectés'), ('Informatique', 'Informatique'), ('Auto_et_moto', 'Autos et MoTos'), ('Livres_et_culture', 'Livres et culture'), ('Bricolage', 'Bricolage'), ('Jardin_et_Aménagement_extérieur', 'Jardin et Aménagement extérieur'), ('Vêtements_Hommes', 'Vêtements Hommes'), ('Vêtements_Femmes', 'Vêtements Femmes'), ('Vêtements_enfants', 'Vêtements enfants')], default='Smartphones_et_objets_connectés', max_length=200),
        ),
    ]
