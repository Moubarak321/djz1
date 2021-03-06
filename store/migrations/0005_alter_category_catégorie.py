# Generated by Django 4.0.4 on 2022-06-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_category_catégorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catégorie',
            field=models.CharField(choices=[('Bébé', 'Bébé'), ('Entretien et nettoyage', 'Entretien et nettoyage'), ('Sport', 'Sport'), ('Jeux videos', 'Jeux Vidéos'), ('Jeux et Jouets', 'Jeux et Jouets'), ('Electroménagers', 'Electroménagers'), ('Smartphones et objets connectés', 'Smartphones et objets connectés'), ('Informatique', 'Informatique'), ('Auto et moto', 'Autos et MoTos'), ('Livres et culture', 'Livres et culture'), ('Bricolage', 'Bricolage'), ('Jardin et Aménagement_extérieur', 'Jardin et Aménagement extérieur'), ('Vêtements Hommes', 'Vêtements Hommes'), ('Vêtements Femmes ', 'Vêtements Femmes'), ('Vêtements enfants', 'Vêtements enfants')], default='Smartphones et objets connectés', max_length=200),
        ),
    ]
