from django.contrib import admin
from .models import Noticia, Categoria, Evento
# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'publicado_em', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'categoria', 'publicado_em', 'autor')
    search_fields = ('titulo', 'subtitulo', 'conteudo', 'autor')
    ordering = ('-publicado_em',)
    date_hierarchy = 'publicado_em'
    
    fieldsets = (
        (None, {
            'fields': ('titulo', 'subtitulo', 'categoria', 'status')
        }),
        ('Conteúdo', {
            'fields': ('conteudo', 'imagem')
        }),
        ('Informações de Publicação', {
            'fields': ('autor',),
        }),
    )

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'criado_em')
    search_fields = ('categoria',)
    readonly_fields = ('criado_em',)
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'criado_em')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data',)
    ordering = ('data',)
