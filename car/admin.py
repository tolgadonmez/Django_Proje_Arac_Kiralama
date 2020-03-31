from django.contrib import admin

# Register your models here.
from car.models import Category, Car


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'status']
    list_filter = ['status', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)
