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
    search_fields = ('numero_estudante', 'nome', 'user__first_name', 'user__last_name', 'curso')
    list_filter = ('curso', 'ano_ingresso')
    ordering = ('nome', 'user__first_name')
    readonly_fields = ('criado_em',)
    raw_id_fields = ('user',) # Typable ID instead of a massive dropdown list
    
    def get_nome_completo(self, obj):
        if obj.user:
            return obj.user.get_full_name()
        return obj.nome or "---"
    get_nome_completo.short_description = 'Nome do Aluno'

@admin.register(InscricaoEvento)
class InscricaoEventoAdmin(admin.ModelAdmin):
    list_display = ('get_participante', 'get_tipo', 'evento', 'data_inscricao', 'confirmado')
    list_filter = ('confirmado', 'evento', 'data_inscricao')
    search_fields = (
        'aluno__user__first_name', 'aluno__user__last_name', 
        'aluno__numero_estudante', 'evento__titulo',
        'nome_externo', 'email_externo'
    )
    ordering = ('-data_inscricao',)
    readonly_fields = ('data_inscricao',)
    
    fieldsets = (
        ('Informações do Evento', {
            'fields': ('evento', 'confirmado', 'data_inscricao')
        }),
        ('Vínculo com Aluno', {
            'fields': ('aluno',),
            'description': 'Preencha este campo se o inscrito for um aluno registado.'
        }),
        ('Informações Externas (Não Alunos)', {
            'fields': ('nome_externo', 'email_externo', 'telefone_externo'),
            'description': 'Estes campos são usados para inscrições de pessoas de fora da instituição.'
        }),
    )
    
    def get_participante(self, obj):
        if obj.aluno:
            if obj.aluno.user:
                return obj.aluno.user.get_full_name()
            return obj.aluno.nome or f"Estudante ({obj.aluno.numero_estudante})"
        return obj.nome_externo
    get_participante.short_description = 'Participante'

    def get_tipo(self, obj):
        return "Aluno" if obj.aluno else "Externo"
    get_tipo.short_description = 'Tipo'
