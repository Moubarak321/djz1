# Generated by Django 4.0.4 on 2022-06-13 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catégorie', models.CharField(choices=[('BB', 'Bébé'), ('EntreNetoi', 'Entretien et nettoyage'), ('Sport', 'Sport'), ('JeuxV', 'Jeux Vidéos'), ('JeuxJouets', 'Jeux et Jouets'), ('ElectroMena', 'Electroménagers'), ('PhoneIOT', 'Smartphones et objets connectés'), ('IT', 'Informatique'), ('AutoMoTo', 'Autos et MoTos'), ('LivreCult', 'Livres et culture'), ('Bricol', 'Bricolage'), ('JardinEX', 'Jardin et Aménagement extérieur'), ('hoe', 'Vêtements Hommes'), ('meufs', 'Vêtements Femmes'), ('eft', 'Vêtements enfants')], max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('price', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('ordered', models.BooleanField(default=False)),
                ('ordered_date', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.ManyToManyField(to='store.order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]