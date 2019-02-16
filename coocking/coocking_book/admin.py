from django.contrib import admin
from .models import Dish, Ingredient, Order, IngredientInOrder

# Register your models here.


class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('title',)
    fields = ['title', 'description', 'ingredient']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight',)
    list_filter = ('name',)


admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Order)
admin.site.register(IngredientInOrder)
