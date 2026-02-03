from django.urls import path
from . import views
from .views import IndexView, NoticesView, NoticiaDetailView, CategoryNoticeView, EventsView, ContactosView, AboutView

app_name = 'pages'

urlpatterns = [
     path('', IndexView.as_view(), name='index'),
     path('notices/', NoticesView.as_view(), name='notice'),
     path('noticia/<uuid:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
     path('categoria/<str:categoria_nome>/', CategoryNoticeView.as_view(), name='category_news'),
     path('sobre/', AboutView.as_view(), name='sobre'),
     path('eventos/', EventsView.as_view(), name='eventos'),
     path('contactos/', views.ContactosView.as_view(), name='contactos'),
]