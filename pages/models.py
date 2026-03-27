from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Categoria(models.Model):
    id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    categoria=models.CharField(max_length=255,verbose_name='Categoria',null=False,blank=False)
    criado_em=models.DateTimeField(auto_now_add=True,blank=False,null=False,verbose_name='Data de Criação')
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['categoria']
        get_latest_by='criado_em'
    def __str__(self):
        return self.categoria

class Noticia(models.Model):
    id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    titulo = models.CharField(max_length=255 , blank=False, null=False, verbose_name='Título')
    subtitulo = models.CharField(max_length=255, blank=True, null=True ,verbose_name='Subtitulo')
    conteudo = models.TextField( blank=False, null=False,verbose_name='Conteúdo')
    imagem = models.ImageField(upload_to='static/uploads/images/', blank=True, null=True ,   verbose_name='Imagem')
    autor = models.CharField(max_length=150 , blank=False, null=False, verbose_name='Autor')
    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT)
    publicado_em = models.DateTimeField(auto_now_add=True , blank=False, null=False,verbose_name='Data de Publicação')
    atualizado_em = models.DateTimeField(auto_now=True , blank=False, null=False,verbose_name='Data de Actualização')
    status = models.BooleanField(default=True , blank=False, null=False)  # ativo/inativo
    exclusivo_alunos = models.BooleanField(default=False, verbose_name='Exclusivo para Alunos')  # Notícias exclusivas
    
    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-publicado_em']          # mais recentes primeiro
        db_table = 'noticias'
        get_latest_by = 'publicado_em'
        permissions = [
            ("pode_publicar", "Pode publicar notícias"),
        ]
    def __str__(self):
        return self.titulo

class Evento(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    titulo = models.CharField(max_length=255, verbose_name='Título')
    data = models.DateField(verbose_name='Data do Evento')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    vagas = models.IntegerField(default=50, verbose_name='Número de Vagas')
    exclusivo_alunos = models.BooleanField(default=True, verbose_name='Exclusivo para Alunos')
    imagem = models.ImageField(upload_to='static/uploads/events/', blank=True, null=True, verbose_name='Imagem')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data']

    def __str__(self):
        return f"{self.data.strftime('%d/%m')} - {self.titulo}"
    
    def vagas_disponiveis(self):
        """Retorna o número de vagas disponíveis"""
        inscritos = self.inscricoes.count()
        return max(0, self.vagas - inscritos)

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno', null=True, blank=True, verbose_name='Utilizador Associado')
    nome = models.CharField(max_length=255, verbose_name='Nome Completo', null=True, blank=True)
    numero_estudante = models.CharField(max_length=20, unique=True, verbose_name='Número de Estudante')
    curso = models.CharField(max_length=200, verbose_name='Curso')
    ano_ingresso = models.IntegerField(verbose_name='Ano de Ingresso')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    foto = models.ImageField(upload_to='static/uploads/alunos/', blank=True, null=True, verbose_name='Foto')
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['user__first_name']
    
    def __str__(self):
        if self.user:
            return f"{self.numero_estudante} - {self.user.get_full_name()}"
        return f"{self.numero_estudante} - {self.nome or 'Estudante sem nome'}"

class InscricaoEvento(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='inscricoes', null=True, blank=True)
    
    # Campos para inscritos externos (não alunos)
    nome_externo = models.CharField(max_length=255, null=True, blank=True, verbose_name='Nome (Externo)')
    email_externo = models.EmailField(null=True, blank=True, verbose_name='Email (Externo)')
    telefone_externo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone (Externo)')
    
    data_inscricao = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Inscrição em Evento'
        verbose_name_plural = 'Inscrições em Eventos'
        ordering = ['-data_inscricao']
    
    def __str__(self):
        if self.aluno:
            return f"{self.aluno.user.get_full_name()} - {self.evento.titulo}"
        return f"{self.nome_externo} (Externo) - {self.evento.titulo}"
