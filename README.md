# 🌐 Portal de Notícias IPM (Instituto Politécnico do Mayombe)

![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Produção-success?style=for-the-badge)

O **Portal de Notícias IPM** é uma plataforma web desenvolvida para o Instituto Politécnico do Mayombe, com o objetivo de centralizar a comunicação institucional, notícias escolares e gestão de eventos para alunos e o público em geral.

---

## 🚀 Funcionalidades Principais

### 📰 Gestão de Notícias
- **Públicas e Exclusivas**: Notícias que podem ser lidas por qualquer pessoa ou restritas apenas a alunos autenticados.
- **Categorização**: Organização de notícias por categorias (ex: Esportes, Tecnologia, Acadêmico).
- **Banner Dinâmico**: Destaque das notícias mais recentes na página inicial.
- **Busca e Filtro**: Sistema de filtragem por categoria para fácil navegação.

### 📅 Gestão de Eventos
- **Inscrições Online**: Alunos podem se inscrever em eventos diretamente pelo portal.
- **Acesso Externo**: Suporte a inscrições de visitantes em eventos não exclusivos.
- **Controle de Vagas**: Gestão automática de disponibilidade de vagas.
- **Histórico**: Alunos podem visualizar os eventos em que se inscreveram.

### 👤 Perfil do Aluno
- **Área Restrita**: Painel personalizado para alunos logados.
- **Edição de Perfil**: Atualização de dados cadastrais, curso, ano e foto de perfil.
- **Gestão de Inscrições**: Possibilidade de cancelar inscrições em eventos futuros.

### 🛠️ Painel Administrativo
- **Interface Premium**: Utiliza o tema **Jazzmin** para uma experiência de administração moderna e intuitiva.
- **CRUD Completo**: Gestão total de usuários, alunos, notícias, categorias e eventos.
- **Permissões**: Controle refinado de quem pode publicar e editar conteúdos.

---

## 🛠️ Tecnologias Utilizadas

- **Framework Web:** Django 5.2.7
- **Linguagem:** Python 3.11.9
- **Banco de Dados:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Interface Admin:** Django Jazzmin
- **Processamento de Imagem:** Pillow
- **Documentação:** Mermaid (UML)

---

## 📁 Estrutura do Projeto

```text
Portal_NoticiasIPM/
├── core/                # Configurações globais do projeto Django
├── pages/               # App principal (models, views, forms, templates)
│   ├── templates/pages/ # Arquivos HTML
│   └── models.py        # Definição das entidades do sistema
├── static/              # Arquivos estáticos (CSS, JS, Imagens)
├── media/               # Arquivos enviados por usuários (Uploads)
├── DIAGRAMAS_UML.md     # Documentação técnica completa (Mermaid)
├── manage.py            # Utilitário de linha de comando do Django
└── README.md            # Este arquivo
```

---

## ⚙️ Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/aguinaldoarnaldo/Portal_NoticiasIPM.git
   cd Portal_NoticiasIPM
   ```

2. **Crie um ambiente virtual (opcional mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/scripts/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   *(Certifique-se de ter o Django e o Pillow instalados)*
   ```bash
   pip install django pillow django-jazzmin
   ```

4. **Execute as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

6. **Acesse no navegador:**
   - Portal: `http://127.0.0.1:8000`
   - Admin: `http://127.0.0.1:8000/admin`

---

## 📊 Documentação Técnica

Para uma visão detalhada da arquitetura do sistema, incluindo diagramas de classes, casos de uso e sequência, consulte o arquivo:
👉 [**DIAGRAMAS_UML.md**](file:///c:/Users/Aguinaldo%20Arnaldo/Documents/Meus_projetos/Portal_NoticiasIPM/DIAGRAMAS_UML.md)

---

## 📝 Autores

- **Desenvolvido por:** Grupo Número 6
- **Instituição:** Instituto Politécnico do Mayombe
- **Ano:** 2026

---
© 2026 IPM - Todos os direitos reservados.
