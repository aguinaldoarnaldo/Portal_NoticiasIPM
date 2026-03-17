from django import forms
from .models import Aluno
from django.contrib.auth.models import User

class AlunoUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, label='Nome')
    last_name = forms.CharField(max_length=150, label='Apelido')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = Aluno
        fields = ['numero_estudante', 'curso', 'ano_ingresso', 'telefone', 'foto']
        widgets = {
            'numero_estudante': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control-readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(AlunoUpdateForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        aluno = super(AlunoUpdateForm, self).save(commit=False)
        user = aluno.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            aluno.save()
        return aluno

class AlunoRegistroForm(forms.Form):
    first_name = forms.CharField(max_length=150, label='Nome')
    last_name = forms.CharField(max_length=150, label='Apelido')
    email = forms.EmailField(label='E-mail')
    username = forms.CharField(max_length=150, label='Nome de Utilizador', help_text='Necessário para login.')
    numero_estudante = forms.CharField(max_length=20, label='Número de Estudante')
    curso = forms.CharField(max_length=200, label='Curso')
    ano_ingresso = forms.IntegerField(label='Ano de Ingresso')
    telefone = forms.CharField(max_length=20, label='Telefone', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    def clean_numero_estudante(self):
        numero = self.cleaned_data.get('numero_estudante')
        try:
            aluno = Aluno.objects.get(numero_estudante=numero)
            if aluno.user:
                raise forms.ValidationError("Este número de estudante já possui uma conta associada.")
            return numero
        except Aluno.DoesNotExist:
            raise forms.ValidationError("Número de estudante não encontrado no sistema. Por favor, contacte a secretaria.")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self):
        # 1. Busca o aluno pré-existente (já validado no clean)
        numero = self.cleaned_data['numero_estudante']
        aluno = Aluno.objects.get(numero_estudante=numero)
        
        # 2. Cria o utilizador
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        
        # 3. Associa e atualiza os dados
        aluno.user = user
        aluno.curso = self.cleaned_data.get('curso', aluno.curso)
        aluno.ano_ingresso = self.cleaned_data.get('ano_ingresso', aluno.ano_ingresso)
        aluno.telefone = self.cleaned_data.get('telefone', aluno.telefone)
        aluno.save()
        
        return aluno
