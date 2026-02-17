from django.urls import path
from . import views
from .views import (
    IndexView, NoticesView, NoticiaDetailView, CategoryNoticeView, 
    EventsView, ContactosView, AboutView, AlunoRegistroView, CustomLoginView,
    CustomLogoutView, EventoDetailView, InscreverEventoView, 
    CancelarInscricaoView, MinhasInscricoesView, PerfilView, PerfilUpdateView
)

app_name = 'pages'

urlpatterns = [
     path('', IndexView.as_view(), name='index'),
     path('notices/', NoticesView.as_view(), name='notice'),
     path('noticia/<uuid:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
     path('categoria/<str:categoria_nome>/', CategoryNoticeView.as_view(), name='category_news'),
     path('sobre/', AboutView.as_view(), name='sobre'),
     path('eventos/', EventsView.as_view(), name='eventos'),
     path('contactos/', views.ContactosView.as_view(), name='contactos'),
     
     # Autenticação
     path('registro/', AlunoRegistroView.as_view(), name='registro'),
     path('login/', CustomLoginView.as_view(), name='login'),
     path('logout/', CustomLogoutView.as_view(), name='logout'),
     
     # Eventos e Perfil
     path('evento/<uuid:pk>/', EventoDetailView.as_view(), name='evento_detail'),
     path('evento/<uuid:pk>/inscrever/', InscreverEventoView.as_view(), name='inscrever_evento'),
     path('evento/<uuid:pk>/cancelar/', CancelarInscricaoView.as_view(), name='cancelar_inscricao'),
     path('perfil/', PerfilView.as_view(), name='perfil'),
     path('perfil/editar/', PerfilUpdateView.as_view(), name='perfil_editar'),
     path('minhas-inscricoes/', MinhasInscricoesView.as_view(), name='minhas_inscricoes'),
]