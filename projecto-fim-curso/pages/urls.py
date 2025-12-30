from django.urls import path
from .views import IndexView, NoticesView, NoticiaDetailView, CategoryNoticeView

app_name = 'pages'

urlpatterns = [
     path('', IndexView.as_view(), name='index'),
     path('notices/', NoticesView.as_view(), name='notice'),
     path('noticia/<uuid:pk>/', NoticiaDetailView.as_view(), name='noticia_detail'),
     path('categoria/<str:categoria_nome>/', CategoryNoticeView.as_view(), name='category_news'),
]