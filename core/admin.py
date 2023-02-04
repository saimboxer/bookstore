from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author', 'year', 'publisher']

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['id','attribute']

@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ['id','attribute_value']

@admin.register(BookAttributeValue)
class BookAttributeValueAdmin(admin.ModelAdmin):
    list_display = ['id','book', 'attribute', 'attribute_value']
