from django.contrib import admin

# Register your models here.
from car.models import Category, Car, Images

class CarImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [CarImageInline]



class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'car', 'image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Images, ImagesAdmin)
