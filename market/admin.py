from django.contrib import admin
from .models import ProductCategory, Product, ProductGallery

class ProductImageInline(admin.TabularInline):
   model = ProductGallery
   extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ['name']
   search_fields = ['name']

   inlines = [ProductImageInline]
   # list_display = ['gallery']

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name']
   search_fields = ['name']

@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
   pass

