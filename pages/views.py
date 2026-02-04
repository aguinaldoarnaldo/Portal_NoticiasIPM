from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Noticia, Aluno, Evento
from .forms import AlunoRegistroForm

# Create your views here.
class IndexView(ListView):
    template_name = 'pages/index.html'
    model = Noticia
    context_object_name = 'noticias'
    
    def get_queryset(self):
        # Se o usuário está logado e é aluno, mostra todas as notícias
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            return Noticia.objects.filter(status=True)
        # Caso contrário, mostra apenas notícias não exclusivas
        return Noticia.objects.filter(status=True, exclusivo_alunos=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Evento
        from django.utils import timezone
        
        # Get 5 latest news for banner slider
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            context['banner_noticias'] = Noticia.objects.filter(status=True).order_by('-publicado_em')[:5]
        else:
            context['banner_noticias'] = Noticia.objects.filter(status=True, exclusivo_alunos=False).order_by('-publicado_em')[:5]
        
        # Get upcoming events
        context['eventos'] = Evento.objects.filter(data__gte=timezone.now().date()).order_by('data')[:5]
        return context

class NoticesView(ListView):
    model = Noticia
    template_name = 'pages/noticia.html'
    context_object_name = 'noticias'
    paginate_by = 12  # Aumentado de 6 para 12

    def get_queryset(self):
        # Filtrar notícias baseado no status de login
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            return Noticia.objects.filter(status=True)
        return Noticia.objects.filter(status=True, exclusivo_alunos=False)
    
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
        
        # Verificar se o usuário pode ver notícias exclusivas
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            context['destaques'] = Noticia.objects.filter(status=True).exclude(id=self.object.id).order_by('-publicado_em')[:3]
        else:
            context['destaques'] = Noticia.objects.filter(status=True, exclusivo_alunos=False).exclude(id=self.object.id).order_by('-publicado_em')[:3]
        
        context['categorias'] = Categoria.objects.all()
        return context

class CategoryNoticeView(ListView):
    model = Noticia
    template_name = 'pages/noticia.html'
    context_object_name = 'noticias'
    paginate_by = 12  # Aumentado de 6 para 12

    def get_queryset(self):
        category_name = self.kwargs.get('categoria_nome')
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            return Noticia.objects.filter(status=True, categoria__categoria__iexact=category_name)
        return Noticia.objects.filter(status=True, exclusivo_alunos=False, categoria__categoria__iexact=category_name)

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
        context['past_events'] = Evento.objects.filter(data__lt=today).order_by('-data')
        
        return context

# Views de Autenticação
class CustomLoginView(LoginView):
    template_name = 'pages/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('pages:index')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Nome de utilizador ou senha incorretos.')
        return super().form_invalid(form)

class AlunoRegistroView(CreateView):
    form_class = AlunoRegistroForm
    template_name = 'pages/registro.html'
    success_url = reverse_lazy('pages:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Conta criada com sucesso! Faça login para continuar.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar conta. Verifique os dados e tente novamente.')
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    """View personalizada para logout que redireciona para a home"""
    pass  # O Django automaticamente usa LOGOUT_REDIRECT_URL do settings

# Views de Eventos e Inscrições
class EventoDetailView(DetailView):
    model = Evento
    template_name = 'pages/evento_detail.html'
    context_object_name = 'evento'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import InscricaoEvento
        
        # Verificar se o usuário já está inscrito
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            context['ja_inscrito'] = InscricaoEvento.objects.filter(
                evento=self.object,
                aluno=self.request.user.aluno
            ).exists()
        else:
            context['ja_inscrito'] = False
            
        return context

from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class InscreverEventoView(LoginRequiredMixin, View):
    login_url = 'pages:login'
    
    def post(self, request, pk):
        from .models import Evento, InscricaoEvento
        
        evento = get_object_or_404(Evento, pk=pk)
        
        # Verificar se o usuário é aluno
        if not hasattr(request.user, 'aluno'):
            messages.error(request, 'Apenas alunos podem se inscrever em eventos.')
            return redirect('pages:evento_detail', pk=pk)
        
        # Verificar se já está inscrito
        if InscricaoEvento.objects.filter(evento=evento, aluno=request.user.aluno).exists():
            messages.warning(request, 'Você já está inscrito neste evento.')
            return redirect('pages:evento_detail', pk=pk)
        
        # Verificar vagas disponíveis
        if evento.vagas_disponiveis() <= 0:
            messages.error(request, 'Desculpe, as vagas para este evento estão esgotadas.')
            return redirect('pages:evento_detail', pk=pk)
        
        # Criar inscrição
        InscricaoEvento.objects.create(
            evento=evento,
            aluno=request.user.aluno,
            confirmado=True
        )
        
        messages.success(request, f'Inscrição realizada com sucesso! Você está inscrito em "{evento.titulo}".')
        return redirect('pages:evento_detail', pk=pk)

class CancelarInscricaoView(LoginRequiredMixin, View):
    login_url = 'pages:login'
    
    def post(self, request, pk):
        from .models import Evento, InscricaoEvento
        
        evento = get_object_or_404(Evento, pk=pk)
        
        # Verificar se o usuário é aluno
        if not hasattr(request.user, 'aluno'):
            messages.error(request, 'Erro ao processar solicitação.')
            return redirect('pages:evento_detail', pk=pk)
        
        # Buscar e deletar inscrição
        inscricao = InscricaoEvento.objects.filter(evento=evento, aluno=request.user.aluno).first()
        
        if inscricao:
            inscricao.delete()
            messages.success(request, 'Inscrição cancelada com sucesso.')
        else:
            messages.warning(request, 'Você não está inscrito neste evento.')
        
        return redirect('pages:evento_detail', pk=pk)

class MinhasInscricoesView(LoginRequiredMixin, ListView):
    login_url = 'pages:login'
    template_name = 'pages/minhas_inscricoes.html'
    context_object_name = 'inscricoes'
    
    def get_queryset(self):
        from .models import InscricaoEvento
        from django.utils import timezone
        
        if hasattr(self.request.user, 'aluno'):
            return InscricaoEvento.objects.filter(
                aluno=self.request.user.aluno
            ).select_related('evento').order_by('-data_inscricao')
        return InscricaoEvento.objects.none()

class PerfilView(LoginRequiredMixin, DetailView):
    login_url = 'pages:login'
    template_name = 'pages/perfil.html'
    context_object_name = 'aluno'
    
    def get_object(self):
        return self.request.user.aluno
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import InscricaoEvento
        from django.utils import timezone
        
        # Eventos futuros inscritos
        context['eventos_futuros'] = InscricaoEvento.objects.filter(
            aluno=self.request.user.aluno,
            evento__data__gte=timezone.now().date()
        ).select_related('evento').order_by('evento__data')
        
        # Eventos passados
        context['eventos_passados'] = InscricaoEvento.objects.filter(
            aluno=self.request.user.aluno,
            evento__data__lt=timezone.now().date()
        ).select_related('evento').order_by('-evento__data')[:5]
        
        return context
