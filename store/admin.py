from django.contrib import admin

from store.models import Product, Order, Cart, Categorie

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display= ('name', 'price', 'category', 'stock')

class AdminCategory(admin.ModelAdmin):
    list_display= ('catégorie', 'date_added')


admin.site.register(Product, AdminProduct )
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Categorie,AdminCategory)