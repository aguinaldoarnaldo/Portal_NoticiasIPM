from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Noticia
# Create your views here.
class IndexView(ListView):
    template_name = 'pages/index.html'
    model = Noticia
    context_object_name = 'noticias'
    
    def get_queryset(self):
        return Noticia.objects.filter(status=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Evento
        from django.utils import timezone
        
        # Get 5 latest news for banner slider - Explicitly ordering by publication date
        context['banner_noticias'] = Noticia.objects.filter(status=True).order_by('-publicado_em')[:5]
        
        # Get upcoming events
        context['eventos'] = Evento.objects.filter(data__gte=timezone.now().date()).order_by('data')[:5]
        return context

class NoticesView(ListView):
    model = Noticia
    template_name = 'pages/noticia.html'
    context_object_name = 'noticias'
    paginate_by = 6

    def get_queryset(self):
        return Noticia.objects.filter(status=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Categoria
        context['categorias'] = Categoria.objects.all()
        return context

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'pages/noticia_detail.html'
    context_object_name = 'noticia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Categoria
        # Get 3 other news items as highlights, excluding the current one
        context['destaques'] = Noticia.objects.filter(status=True).exclude(id=self.object.id).order_by('-publicado_em')[:3]
        context['categorias'] = Categoria.objects.all()
        return context

class CategoryNoticeView(ListView):
    model = Noticia
    template_name = 'pages/noticia.html'
    context_object_name = 'noticias'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs.get('categoria_nome')
        return Noticia.objects.filter(status=True, categoria__categoria__iexact=category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Categoria
        context['categoria_ativa'] = self.kwargs.get('categoria_nome')
        context['categorias'] = Categoria.objects.all()
        return context

class AboutView(ListView):
    template_name = 'pages/sobre.html'
    model = Noticia 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ContactosView(ListView):
    template_name = 'pages/contactos.html'
    model = Noticia

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class EventsView(ListView):
    template_name = 'pages/eventos.html'
    model = Noticia  # Dummy model, we override context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Evento
        from django.utils import timezone
        
        today = timezone.now().date()
        
        # Split events into upcoming and past
        context['upcoming_events'] = Evento.objects.filter(data__gte=today).order_by('data')
        context['past_events'] = Evento.objects.filter(data__lt=today).order_by('-data') # Most recent past first
        
        return context
