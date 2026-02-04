from django.contrib import admin
from .models import Noticia, Categoria, Evento, Aluno, InscricaoEvento

# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'publicado_em', 'exclusivo_alunos', 'status')
    list_editable = ('status', 'exclusivo_alunos')
    list_filter = ('status', 'exclusivo_alunos', 'categoria', 'publicado_em', 'autor')
    search_fields = ('titulo', 'subtitulo', 'conteudo', 'autor')
    ordering = ('-publicado_em',)
    date_hierarchy = 'publicado_em'
    
    fieldsets = (
        (None, {
            'fields': ('titulo', 'subtitulo', 'categoria', 'status', 'exclusivo_alunos')
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
    list_display = ('titulo', 'data', 'vagas', 'vagas_disponiveis', 'criado_em')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data',)
    ordering = ('data',)
    
    def vagas_disponiveis(self, obj):
        return obj.vagas_disponiveis()
    vagas_disponiveis.short_description = 'Vagas Disponíveis'

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('numero_estudante', 'get_nome_completo', 'curso', 'ano_ingresso', 'criado_em')
    search_fields = ('numero_estudante', 'user__first_name', 'user__last_name', 'curso')
    list_filter = ('curso', 'ano_ingresso')
    ordering = ('user__first_name',)
    readonly_fields = ('criado_em',)
    
    def get_nome_completo(self, obj):
        return obj.user.get_full_name()
    get_nome_completo.short_description = 'Nome Completo'

@admin.register(InscricaoEvento)
class InscricaoEventoAdmin(admin.ModelAdmin):
    list_display = ('get_aluno_nome', 'evento', 'data_inscricao', 'confirmado')
    list_filter = ('confirmado', 'evento', 'data_inscricao')
    search_fields = ('aluno__user__first_name', 'aluno__user__last_name', 'aluno__numero_estudante', 'evento__titulo')
    ordering = ('-data_inscricao',)
    readonly_fields = ('data_inscricao',)
    
    def get_aluno_nome(self, obj):
        return obj.aluno.user.get_full_name()
    get_aluno_nome.short_description = 'Aluno'
