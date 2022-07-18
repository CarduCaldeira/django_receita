from django.contrib import admin
from .models import Receita

# Register your models here.


class Listando_Receitas(admin.ModelAdmin):
    list_display = ('id','nome_receita','categoria')
    list_display_links = ('id','nome_receita','categoria')
    search_fields = ('nome_receita','categoria')
    list_filter = ('categoria',)
    list_per_page = 2

admin.site.register(Receita, Listando_Receitas)


