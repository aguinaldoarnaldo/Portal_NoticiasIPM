from django.db import models
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
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data']

    def __str__(self):
        return f"{self.data.strftime('%d/%m')} - {self.titulo}"