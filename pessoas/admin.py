from django.contrib import admin
from .models import Pessoa

# Register your models here.

class Listando_Pessoas(admin.ModelAdmin):
    list_display = ('id','nome','email')
    list_display_links = ('id','nome','email')
    search_fields = ('nome',)
    list_per_page = 2

admin.site.register(Pessoa, Listando_Pessoas)