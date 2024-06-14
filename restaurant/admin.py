from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    search_fields =['title']
admin.site.register(Restaurant, RestaurantAdmin)

# Register your models here.
