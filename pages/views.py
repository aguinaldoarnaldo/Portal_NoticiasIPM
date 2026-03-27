from django.views.generic import CreateView, DetailView, ListView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Noticia, Aluno, Evento, Categoria
from .forms import AlunoRegistroForm, AlunoUpdateForm

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
        from .forms import AlunoRegistroForm
        from django.utils import timezone
        
        # Get 5 latest news for banner slider
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            context['banner_noticias'] = Noticia.objects.filter(status=True).order_by('-publicado_em')[:5]
        else:
            context['banner_noticias'] = Noticia.objects.filter(status=True, exclusivo_alunos=False).order_by('-publicado_em')[:5]
        
        # Get upcoming events
        context['eventos'] = Evento.objects.filter(data__gte=timezone.now().date()).order_by('data')[:5]
        
        # Form for registration modal
        context['registro_form'] = AlunoRegistroForm()
        
        return context

class NoticesView(ListView):
    model = Noticia
    template_name = 'pages/noticia.html'
    context_object_name = 'noticias'
    paginate_by = 32

    def get_queryset(self):
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        order = self.request.GET.get('order', 'latest')
        
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            queryset = Noticia.objects.filter(status=True)
        else:
            queryset = Noticia.objects.filter(status=True, exclusivo_alunos=False)
        
        if q:
            queryset = queryset.filter(Q(titulo__icontains=q) | Q(conteudo__icontains=q) | Q(subtitulo__icontains=q))
        
        if cat:
            queryset = queryset.filter(categoria__categoria__iexact=cat)

        if order == 'oldest':
            queryset = queryset.order_by('publicado_em')
        else:
            queryset = queryset.order_by('-publicado_em')
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['q'] = self.request.GET.get('q', '')
        context['categoria_ativa'] = self.request.GET.get('cat', '')
        context['order'] = self.request.GET.get('order', 'latest')
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
    paginate_by = 32

    def get_queryset(self):
        category_name = self.kwargs.get('categoria_nome')
        q = self.request.GET.get('q')
        
        if self.request.user.is_authenticated and hasattr(self.request.user, 'aluno'):
            queryset = Noticia.objects.filter(status=True, categoria__categoria__iexact=category_name)
        else:
            queryset = Noticia.objects.filter(status=True, exclusivo_alunos=False, categoria__categoria__iexact=category_name)
            
        if q:
            queryset = queryset.filter(Q(titulo__icontains=q) | Q(corpo__icontains=q) | Q(subtitulo__icontains=q))
            
        return queryset.order_by('-publicado_em')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria_ativa'] = self.kwargs.get('categoria_nome')
        context['categorias'] = Categoria.objects.all()
        context['q'] = self.request.GET.get('q', '')
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
        from django.utils import timezone
        
        today = timezone.now().date()
        q = self.request.GET.get('q')
        status = self.request.GET.get('status', 'all')
        order = self.request.GET.get('order', 'upcoming_first')
        
        queryset = Evento.objects.all()
        
        if q:
            queryset = queryset.filter(Q(titulo__icontains=q) | Q(descricao__icontains=q))
            context['q'] = q

        if status == 'upcoming':
            queryset = queryset.filter(data__gte=today)
        elif status == 'past':
            queryset = queryset.filter(data__lt=today)

        upcoming_events = queryset.filter(data__gte=today)
        past_events = queryset.filter(data__lt=today)
        
        if order == 'latest':
            upcoming_events = upcoming_events.order_by('-data')
            past_events = past_events.order_by('-data')
        elif order == 'oldest':
            upcoming_events = upcoming_events.order_by('data')
            past_events = past_events.order_by('data')
        else: # upcoming_first
            upcoming_events = upcoming_events.order_by('data')
            past_events = past_events.order_by('-data')
            
        context['upcoming_events'] = upcoming_events
        context['past_events'] = past_events
        context['status'] = status
        context['order'] = order
        
        # Slider Banner - Top 5 upcoming events
        context['banner_eventos'] = Evento.objects.filter(data__gte=today).order_by('data')[:5]
        
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

class AlunoRegistroView(FormView):
    form_class = AlunoRegistroForm
    template_name = 'pages/registro.html'
    success_url = reverse_lazy('pages:login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Conta criada com sucesso! Faça login para continuar.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar conta. Verifique os dados e tente novamente.')
        return super().form_invalid(form)
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

class InscreverEventoView(View):
    def post(self, request, pk):
        from .models import Evento, InscricaoEvento
        
        evento = get_object_or_404(Evento, pk=pk)
        
        # 1. Caminho para Usuário Autenticado (Aluno)
        if request.user.is_authenticated:
            if not hasattr(request.user, 'aluno'):
                # Se for admin/staff sem perfil de aluno, e o evento permitir externo, tratar como externo ou sugerir criação de perfil
                if not evento.exclusivo_alunos:
                    return self._inscrever_externo(request, evento)
                messages.error(request, 'Apenas alunos podem se inscrever neste evento exclusivo.')
                return redirect('pages:evento_detail', pk=pk)
            
            # Verificar se já está inscrito
            if InscricaoEvento.objects.filter(evento=evento, aluno=request.user.aluno).exists():
                messages.warning(request, 'Você já está inscrito neste evento.')
                return redirect('pages:evento_detail', pk=pk)
            
            # Verificar vagas
            if evento.vagas_disponiveis() <= 0:
                messages.error(request, 'Desculpe, as vagas para este evento estão esgotadas.')
                return redirect('pages:evento_detail', pk=pk)
            
            # Criar inscrição de aluno
            InscricaoEvento.objects.create(
                evento=evento,
                aluno=request.user.aluno,
                confirmado=True
            )
            messages.success(request, f'Inscrição realizada com sucesso, {request.user.first_name}!')
            return redirect('pages:evento_detail', pk=pk)
            
        # 2. Caminho para Usuário Não Autenticado (Externo)
        else:
            if evento.exclusivo_alunos:
                messages.error(request, 'Este evento é exclusivo para alunos. Por favor, faça login para se inscrever.')
                return redirect('pages:login')
            
            return self._inscrever_externo(request, evento)

    def _inscrever_externo(self, request, evento):
        from .models import InscricaoEvento
        
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        
        if not nome or not email or not telefone:
            messages.error(request, 'Nome, Email e Telefone são obrigatórios para a inscrição.')
            return redirect('pages:evento_detail', pk=evento.id)
            
        # Verificar vagas
        if evento.vagas_disponiveis() <= 0:
            messages.error(request, 'Desculpe, as vagas para este evento estão esgotadas.')
            return redirect('pages:evento_detail', pk=evento.id)
            
        # Evitar duplicados por email
        if InscricaoEvento.objects.filter(evento=evento, email_externo=email).exists():
            messages.warning(request, 'Este email já está inscrito neste evento.')
            return redirect('pages:evento_detail', pk=evento.id)
            
        InscricaoEvento.objects.create(
            evento=evento,
            nome_externo=nome,
            email_externo=email,
            telefone_externo=telefone,
            confirmado=True
        )
        messages.success(request, f'Inscrição pública realizada com sucesso! Bem-vindo, {nome}.')
        return redirect('pages:evento_detail', pk=evento.id)

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
        
        # Retorna as inscrições apenas se o perfil de aluno existir
        aluno = getattr(self.request.user, 'aluno', None)
        if aluno:
            return InscricaoEvento.objects.filter(
                aluno=aluno
            ).select_related('evento').order_by('-data_inscricao')
        return InscricaoEvento.objects.none()

class PerfilView(LoginRequiredMixin, DetailView):
    login_url = 'pages:login'
    template_name = 'pages/perfil.html'
    context_object_name = 'aluno'
    
    def get_object(self):
        # Retorna o aluno se existir, senão retorna None
        return getattr(self.request.user, 'aluno', None)
    
    def get_context_data(self, **kwargs):
        # Força o objeto a ser o aluno (get_object já trata isso)
        context = super().get_context_data(**kwargs)
        from .models import InscricaoEvento
        from django.utils import timezone
        
        aluno = self.get_object()
        if aluno:
            # Eventos futuros inscritos
            context['eventos_futuros'] = InscricaoEvento.objects.filter(
                aluno=aluno,
                evento__data__gte=timezone.now().date()
            ).select_related('evento').order_by('evento__data')
            
            # Eventos passados
            context['eventos_passados'] = InscricaoEvento.objects.filter(
                aluno=aluno,
                evento__data__lt=timezone.now().date()
            ).select_related('evento').order_by('-evento__data')[:5]
        else:
            context['eventos_futuros'] = []
            context['eventos_passados'] = []
            
        return context

from django.views.generic.edit import UpdateView

class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'pages:login'
    template_name = 'pages/perfil_edit.html'
    form_class = AlunoUpdateForm
    success_url = reverse_lazy('pages:perfil')
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'aluno'):
            messages.warning(request, "Você precisa preencher o seu perfil de estudante primeiro.")
            return redirect('pages:perfil')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return getattr(self.request.user, 'aluno', None)

    def form_valid(self, form):
        messages.success(self.request, 'Perfil atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar perfil. Verifique os dados.')
        return super().form_invalid(form)
