from pickle import TRUE
from unicodedata import category
from django.utils import timezone 
from tkinter import CASCADE
from django.urls import reverse
# from distutils.command.upload import upload
from django.db import models


from ecom.settings import AUTH_USER_MODEL

# Create your models here.

"""categorie
    nom
    date_d'ajout

"""

class Categorie(models.Model):
    # Bébé = "Bébé"
    # Entretien_et_nettoyage = "Entretien et nettoyage"
    # Sport = "Sport"
    # Jeux_videos = "Jeux videos"
    # Jeux_et_Jouets = "Jeux et Jouets"
    # Electroménagers = "Electroménagers"
    # Smartphones_et_objets_connectés = "Smartphones et objets connectés"
    # Informatique = "Informatique"
    # Auto_et_moto = "Auto et moto"
    # Livres_et_culture = "Livres et culture"
    # Bricolage = "Bricolage"
    # Jardin_et_Aménagement_extérieur = "Jardin et Aménagement extérieur"
    # Vêtements_Hommes = "Vêtements Hommes"
    # Vêtements_Femmes = "Vêtements Femmes"
    # Vêtements_enfants = "Vêtements enfants"

    les_choix = [
        ('Bébé' , 'Bébé'),
        ('Entretien et nettoyage' , 'Entretien et nettoyage'),
        ('Sport' , 'Sport'),
        ('Jeux videos' , 'Jeux Vidéos'),
        ('Jeux et Jouets' , 'Jeux et Jouets'),
        ('Electroménagers' , 'Electroménagers'),
        ('Smartphones et objets connectés' , 'Smartphones et objets connectés'),
        ('Informatique' , 'Informatique'),
        ('Auto et moto' , 'Autos et MoTos'),
        ('Livres et culture' , 'Livres et culture'),
        ('Bricolage' , 'Bricolage'),
        ('Jardin et Aménagement_extérieur' , 'Jardin et Aménagement extérieur'),
        ('Vêtements Hommes' , 'Vêtements Hommes'),
        ('Vêtements Femmes ', 'Vêtements Femmes'),
        ('Vêtements enfants' , 'Vêtements enfants'),
    ]
    catégorie = models.CharField(max_length=200, choices = les_choix, default='Smartphones et objets connectés' )
    date_added = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.catégorie




    





""""
Product
    Nom 
    Prix
    Stock
    Description
    Image

"""

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Categorie, related_name = 'categorie', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description =models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product", kwargs = {"slug": self.slug}) # nom de l'url "product" et un paramètre contenant le slug



"""
Article(Order):  les articles que l'utilisateur souhaite acheter et les details
    UTILISATEUR
    PRODUIT
    Quantité
    Commandé ou non
"""
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
"""
Panier(Cart):  panier de l'utilsateur qui sera relié aux articles
    UTILISATEUR
    Articles
    Commandé ou non
    Date de commande
"""

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    
    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date =timezone.now()
            order.save()
        self.orders.clear()
        super().delete(*args, **kwargs)