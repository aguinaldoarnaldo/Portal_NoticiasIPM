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

class AlunoRegistroForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, label='Nome')
    last_name = forms.CharField(max_length=150, label='Apelido')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')

    class Meta:
        model = Aluno
        fields = ['numero_estudante', 'curso', 'ano_ingresso', 'telefone']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        # Primeiro cria o usuário
        user = User.objects.create_user(
            username=self.cleaned_data['numero_estudante'], # Usando o número de estudante como username
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        
        # Depois cria o aluno associado
        aluno = super().save(commit=False)
        aluno.user = user
        
        if commit:
            aluno.save()
        return aluno
