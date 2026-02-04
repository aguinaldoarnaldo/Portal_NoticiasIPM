from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Aluno

class AlunoRegistroForm(UserCreationForm):
    """Formulário de registro para alunos"""
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(max_length=30, required=True, label='Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome')
    numero_estudante = forms.CharField(max_length=20, required=True, label='Número de Estudante')
    curso = forms.CharField(max_length=200, required=True, label='Curso')
    ano_ingresso = forms.IntegerField(required=True, label='Ano de Ingresso', min_value=2000, max_value=2030)
    telefone = forms.CharField(max_length=20, required=False, label='Telefone')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar labels e placeholders
        self.fields['username'].label = 'Nome de Utilizador'
        self.fields['username'].help_text = 'Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmar Senha'
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            # Criar perfil de aluno
            Aluno.objects.create(
                user=user,
                numero_estudante=self.cleaned_data['numero_estudante'],
                curso=self.cleaned_data['curso'],
                ano_ingresso=self.cleaned_data['ano_ingresso'],
                telefone=self.cleaned_data.get('telefone', '')
            )
        return user
