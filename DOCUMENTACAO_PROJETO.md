# 📰 Portal de Notícias IPM - Documentação do Projeto

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Arquitetura do Sistema](#arquitetura-do-sistema)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Banco de Dados](#banco-de-dados)
5. [Modelos de Dados](#modelos-de-dados)
6. [Atores do Sistema](#atores-do-sistema)
7. [Casos de Uso](#casos-de-uso)
8. [Requisitos Funcionais](#requisitos-funcionais)
9. [Requisitos Não Funcionais](#requisitos-não-funcionais)
10. [Estrutura do Projeto](#estrutura-do-projeto)
11. [Configurações](#configurações)
12. [Rotas e URLs](#rotas-e-urls)

---

## 🎯 Visão Geral

O **Portal de Notícias IPM** é um sistema web desenvolvido em Django para gerenciamento e publicação de notícias do Instituto Politécnico do Mayombe (IPM). O sistema permite a criação, edição, publicação e visualização de notícias categorizadas, além de gerenciamento de eventos.

### Objetivos do Projeto
- Centralizar a publicação de notícias institucionais
- Facilitar a comunicação com a comunidade acadêmica
- Organizar notícias por categorias
- Gerenciar eventos importantes da instituição
- Fornecer interface administrativa moderna e intuitiva

---

## 🏗️ Arquitetura do Sistema

O projeto segue o padrão **MVT (Model-View-Template)** do Django:

```
┌─────────────────────────────────────────────────┐
│                   USUÁRIO                        │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│              TEMPLATES (HTML)                    │
│  - index.html                                    │
│  - noticia.html                                  │
│  - noticia_detail.html                           │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│              VIEWS (Lógica)                      │
│  - IndexView                                     │
│  - NoticesView                                   │
│  - NoticiaDetailView                             │
│  - CategoryNoticeView                            │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│              MODELS (Dados)                      │
│  - Noticia                                       │
│  - Categoria                                     │
│  - Evento                                        │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│          BANCO DE DADOS (SQLite3)                │
└─────────────────────────────────────────────────┘
```

---

## 💻 Tecnologias Utilizadas

### Backend
- **Django 4.2.27** - Framework web Python
- **Python 3.x** - Linguagem de programação
- **SQLite3** - Banco de dados relacional
- **Django Jazzmin** - Interface administrativa moderna

### Frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização
- **JavaScript** - Interatividade
- **Bootstrap** (via Jazzmin) - Framework CSS

### Bibliotecas Python
- `django` - Framework principal
- `django-jazzmin` - Painel administrativo customizado
- `Pillow` - Processamento de imagens
- `uuid` - Geração de identificadores únicos

---

## 🗄️ Banco de Dados

### Tipo de Banco de Dados
**SQLite3** - Banco de dados relacional leve e embutido

**Arquivo:** `projecto_fim_curso.sqlite3`

### Configuração do Banco de Dados

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'projecto_fim_curso.sqlite3',
    }
}
```

### Características
- **Leve e portátil** - Não requer servidor separado
- **Adequado para desenvolvimento** - Ideal para projetos de pequeno a médio porte
- **Transacional** - Suporta ACID (Atomicidade, Consistência, Isolamento, Durabilidade)
- **Sem configuração** - Funciona imediatamente sem setup adicional

---

## 📊 Modelos de Dados

### 1. Categoria

Armazena as categorias de notícias (Esporte, Política, Cultura, etc.)

```python
class Categoria(models.Model):
    id = UUIDField (Primary Key)
    categoria = CharField (max_length=255)
    criado_em = DateTimeField (auto_now_add=True)
```

**Campos:**
- `id`: Identificador único UUID
- `categoria`: Nome da categoria
- `criado_em`: Data de criação automática

**Metadados:**
- Ordenação: Por nome da categoria
- Verbose Name: "Categoria" / "Categorias"

---

### 2. Noticia

Modelo principal que armazena as notícias publicadas

```python
class Noticia(models.Model):
    id = UUIDField (Primary Key)
    titulo = CharField (max_length=255)
    subtitulo = CharField (max_length=255, opcional)
    conteudo = TextField
    imagem = ImageField (upload_to='static/uploads/images/')
    autor = CharField (max_length=150)
    categoria = ForeignKey (Categoria)
    publicado_em = DateTimeField (auto_now_add=True)
    atualizado_em = DateTimeField (auto_now=True)
    status = BooleanField (default=True)
```

**Campos:**
- `id`: Identificador único UUID
- `titulo`: Título da notícia (obrigatório)
- `subtitulo`: Subtítulo (opcional)
- `conteudo`: Corpo da notícia (obrigatório)
- `imagem`: Imagem de capa (opcional)
- `autor`: Nome do autor (obrigatório)
- `categoria`: Relacionamento com Categoria (ForeignKey)
- `publicado_em`: Data de publicação automática
- `atualizado_em`: Data de última atualização automática
- `status`: Ativo/Inativo (True/False)

**Metadados:**
- Ordenação: Por data de publicação (mais recentes primeiro)
- Tabela: `noticias`
- Permissões customizadas: `pode_publicar`

---

### 3. Evento

Armazena eventos importantes da instituição

```python
class Evento(models.Model):
    id = UUIDField (Primary Key)
    titulo = CharField (max_length=255)
    data = DateField
    descricao = TextField (opcional)
    criado_em = DateTimeField (auto_now_add=True)
```

**Campos:**
- `id`: Identificador único UUID
- `titulo`: Título do evento
- `data`: Data do evento
- `descricao`: Descrição detalhada (opcional)
- `criado_em`: Data de criação

**Metadados:**
- Ordenação: Por data do evento
- Verbose Name: "Evento" / "Eventos"

---

### Diagrama de Relacionamento (ER)

```
┌─────────────────┐
│   Categoria     │
│─────────────────│
│ id (PK)         │
│ categoria       │
│ criado_em       │
└────────┬────────┘
         │
         │ 1:N
         │
         ▼
┌─────────────────┐
│    Noticia      │
│─────────────────│
│ id (PK)         │
│ titulo          │
│ subtitulo       │
│ conteudo        │
│ imagem          │
│ autor           │
│ categoria (FK)  │
│ publicado_em    │
│ atualizado_em   │
│ status          │
└─────────────────┘

┌─────────────────┐
│     Evento      │
│─────────────────│
│ id (PK)         │
│ titulo          │
│ data            │
│ descricao       │
│ criado_em       │
└─────────────────┘
```

---

## 👥 Atores do Sistema

### 1. **Administrador**
**Descrição:** Usuário com permissões completas no sistema

**Responsabilidades:**
- Gerenciar categorias de notícias
- Criar, editar e excluir notícias
- Gerenciar eventos
- Controlar status de publicação (ativar/desativar)
- Gerenciar usuários do sistema
- Acessar painel administrativo Django Jazzmin

**Permissões:**
- Acesso total ao Django Admin
- CRUD completo em todos os modelos
- Gerenciamento de permissões

---

### 2. **Editor/Jornalista**
**Descrição:** Usuário responsável pela criação de conteúdo

**Responsabilidades:**
- Criar novas notícias
- Editar notícias existentes
- Upload de imagens
- Categorizar notícias
- Criar eventos

**Permissões:**
- Acesso ao painel administrativo
- Criar e editar notícias
- Visualizar todas as categorias
- Permissão customizada: `pode_publicar`

---

### 3. **Visitante/Leitor**
**Descrição:** Usuário público que acessa o portal

**Responsabilidades:**
- Visualizar notícias publicadas
- Navegar por categorias
- Ler detalhes de notícias
- Visualizar eventos próximos

**Permissões:**
- Acesso somente leitura
- Visualização de notícias com status=True
- Sem acesso ao painel administrativo

---

## 📝 Casos de Uso

### UC01 - Publicar Notícia

**Ator Principal:** Administrador/Editor

**Pré-condições:**
- Usuário autenticado no sistema
- Usuário possui permissão `pode_publicar`

**Fluxo Principal:**
1. Usuário acessa o painel administrativo
2. Seleciona "Adicionar Notícia"
3. Preenche título, subtítulo, conteúdo
4. Seleciona categoria
5. Faz upload da imagem (opcional)
6. Informa nome do autor
7. Define status (ativo/inativo)
8. Salva a notícia
9. Sistema registra data de publicação automaticamente

**Pós-condições:**
- Notícia criada no banco de dados
- Notícia visível no portal (se status=True)

---

### UC02 - Visualizar Notícias

**Ator Principal:** Visitante

**Pré-condições:**
- Acesso à internet
- Notícias publicadas com status=True

**Fluxo Principal:**
1. Usuário acessa a página inicial
2. Sistema exibe lista de notícias recentes
3. Usuário pode filtrar por categoria
4. Usuário clica em uma notícia
5. Sistema exibe detalhes completos
6. Sistema mostra notícias relacionadas

**Pós-condições:**
- Usuário visualiza conteúdo da notícia

---

### UC03 - Gerenciar Categorias

**Ator Principal:** Administrador

**Pré-condições:**
- Usuário autenticado como administrador

**Fluxo Principal:**
1. Administrador acessa painel administrativo
2. Seleciona "Categorias"
3. Pode criar nova categoria
4. Pode editar categoria existente
5. Sistema valida nome único
6. Salva alterações

**Pós-condições:**
- Categoria criada/atualizada no sistema

---

### UC04 - Filtrar Notícias por Categoria

**Ator Principal:** Visitante

**Pré-condições:**
- Categorias cadastradas
- Notícias publicadas

**Fluxo Principal:**
1. Usuário acessa menu de categorias
2. Seleciona categoria desejada
3. Sistema filtra notícias da categoria
4. Exibe lista paginada (6 por página)

**Pós-condições:**
- Usuário visualiza notícias filtradas

---

### UC05 - Gerenciar Eventos

**Ator Principal:** Administrador/Editor

**Pré-condições:**
- Usuário autenticado

**Fluxo Principal:**
1. Usuário acessa "Eventos" no admin
2. Cria novo evento
3. Preenche título, data e descrição
4. Salva evento
5. Sistema ordena por data

**Pós-condições:**
- Evento criado e visível na página inicial (próximos 5 eventos)

---

### UC06 - Editar Notícia

**Ator Principal:** Administrador/Editor

**Pré-condições:**
- Notícia existente no sistema
- Usuário autenticado

**Fluxo Principal:**
1. Usuário acessa lista de notícias no admin
2. Seleciona notícia para editar
3. Modifica campos desejados
4. Salva alterações
5. Sistema atualiza `atualizado_em` automaticamente

**Pós-condições:**
- Notícia atualizada no banco de dados

---

### UC07 - Ativar/Desativar Notícia

**Ator Principal:** Administrador

**Pré-condições:**
- Notícia existente

**Fluxo Principal:**
1. Administrador acessa lista de notícias
2. Altera campo `status` diretamente na lista
3. Sistema atualiza status
4. Notícia fica visível/invisível no portal

**Pós-condições:**
- Status da notícia alterado

---

## ✅ Requisitos Funcionais

### RF01 - Gerenciamento de Notícias
O sistema deve permitir criar, editar, visualizar e desativar notícias.

**Prioridade:** Alta  
**Status:** Implementado

---

### RF02 - Categorização de Notícias
O sistema deve permitir categorizar notícias em diferentes categorias.

**Prioridade:** Alta  
**Status:** Implementado

---

### RF03 - Upload de Imagens
O sistema deve permitir upload de imagens para as notícias.

**Prioridade:** Média  
**Status:** Implementado  
**Diretório:** `static/uploads/images/`

---

### RF04 - Listagem de Notícias
O sistema deve exibir notícias em ordem cronológica decrescente.

**Prioridade:** Alta  
**Status:** Implementado

---

### RF05 - Paginação
O sistema deve paginar a lista de notícias (6 por página).

**Prioridade:** Média  
**Status:** Implementado

---

### RF06 - Filtro por Categoria
O sistema deve permitir filtrar notícias por categoria.

**Prioridade:** Alta  
**Status:** Implementado

---

### RF07 - Visualização de Detalhes
O sistema deve exibir detalhes completos de uma notícia.

**Prioridade:** Alta  
**Status:** Implementado

---

### RF08 - Notícias Relacionadas
O sistema deve exibir 3 notícias relacionadas na página de detalhes.

**Prioridade:** Baixa  
**Status:** Implementado

---

### RF09 - Gerenciamento de Eventos
O sistema deve permitir criar e gerenciar eventos.

**Prioridade:** Média  
**Status:** Implementado

---

### RF10 - Exibição de Eventos Próximos
O sistema deve exibir os próximos 5 eventos na página inicial.

**Prioridade:** Média  
**Status:** Implementado

---

### RF11 - Controle de Status
O sistema deve permitir ativar/desativar notícias sem excluí-las.

**Prioridade:** Alta  
**Status:** Implementado

---

### RF12 - Busca no Admin
O sistema deve permitir buscar notícias por título, subtítulo, conteúdo e autor.

**Prioridade:** Média  
**Status:** Implementado

---

### RF13 - Autenticação de Usuários
O sistema deve autenticar usuários para acesso ao painel administrativo.

**Prioridade:** Alta  
**Status:** Implementado (Django Auth)

---

### RF14 - Permissões Customizadas
O sistema deve implementar permissão `pode_publicar` para notícias.

**Prioridade:** Média  
**Status:** Implementado

---

### RF15 - Timestamps Automáticos
O sistema deve registrar automaticamente datas de criação e atualização.

**Prioridade:** Alta  
**Status:** Implementado

---

## 🔒 Requisitos Não Funcionais

### RNF01 - Usabilidade
**Descrição:** Interface administrativa intuitiva e moderna  
**Implementação:** Django Jazzmin com tema darkly  
**Métrica:** Tempo de aprendizado < 30 minutos

---

### RNF02 - Performance
**Descrição:** Tempo de carregamento de páginas  
**Implementação:** Queries otimizadas, paginação  
**Métrica:** Tempo de resposta < 2 segundos

---

### RNF03 - Segurança
**Descrição:** Proteção contra ataques comuns  
**Implementação:**
- CSRF Protection (Django middleware)
- XSS Protection
- SQL Injection Protection (Django ORM)
- Autenticação obrigatória para admin

**Métrica:** Conformidade com OWASP Top 10

---

### RNF04 - Manutenibilidade
**Descrição:** Código organizado e documentado  
**Implementação:**
- Padrão MVT
- Separação de responsabilidades
- Nomenclatura clara

**Métrica:** Facilidade de adicionar novas funcionalidades

---

### RNF05 - Portabilidade
**Descrição:** Executável em diferentes ambientes  
**Implementação:**
- SQLite (banco portátil)
- Django (multiplataforma)
- Python 3.x

**Métrica:** Funciona em Windows, Linux, macOS

---

### RNF06 - Escalabilidade
**Descrição:** Capacidade de crescimento  
**Implementação:**
- Paginação
- Queries otimizadas
- Possibilidade de migração para PostgreSQL/MySQL

**Métrica:** Suporta até 10.000 notícias sem degradação

---

### RNF07 - Disponibilidade
**Descrição:** Sistema disponível para acesso  
**Implementação:** Servidor web Django  
**Métrica:** Uptime > 99% (em produção)

---

### RNF08 - Internacionalização
**Descrição:** Suporte ao idioma português de Angola  
**Implementação:**
```python
LANGUAGE_CODE = 'pt-ao'
TIME_ZONE = 'Africa/Luanda'
```
**Métrica:** Datas e textos em português

---

### RNF09 - Responsividade
**Descrição:** Interface adaptável a diferentes dispositivos  
**Implementação:** Bootstrap (via Jazzmin)  
**Métrica:** Funcional em desktop, tablet e mobile

---

### RNF10 - Backup e Recuperação
**Descrição:** Possibilidade de backup do banco de dados  
**Implementação:** Arquivo SQLite copiável  
**Métrica:** Backup completo em < 1 minuto

---

### RNF11 - Compatibilidade
**Descrição:** Compatibilidade com navegadores modernos  
**Implementação:** HTML5, CSS3, JavaScript ES6+  
**Métrica:** Funciona em Chrome, Firefox, Safari, Edge (últimas 2 versões)

---

### RNF12 - Auditoria
**Descrição:** Rastreamento de alterações  
**Implementação:**
- Campos `criado_em`, `atualizado_em`
- Campo `autor` nas notícias

**Métrica:** Histórico completo de publicações

---

## 📁 Estrutura do Projeto

```
projecto-fim-curso/
│
├── core/                          # Configurações principais do projeto
│   ├── __init__.py
│   ├── asgi.py                    # Configuração ASGI
│   ├── settings.py                # Configurações do Django
│   ├── urls.py                    # URLs principais
│   └── wsgi.py                    # Configuração WSGI
│
├── pages/                         # App principal de notícias
│   ├── migrations/                # Migrações do banco de dados
│   │   ├── 0001_initial.py
│   │   ├── 0002_evento_alter_noticia_imagem.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py                   # Configuração do Django Admin
│   ├── apps.py                    # Configuração do app
│   ├── models.py                  # Modelos de dados
│   ├── tests.py                   # Testes unitários
│   ├── urls.py                    # URLs do app
│   └── views.py                   # Views (lógica de negócio)
│
├── static/                        # Arquivos estáticos
│   ├── css/                       # Folhas de estilo
│   ├── js/                        # JavaScript
│   ├── images/                    # Imagens do site
│   │   └── favicon.ico
│   └── uploads/                   # Uploads de usuários
│       └── images/                # Imagens de notícias
│
├── templates/                     # Templates HTML
│   └── pages/
│       ├── index.html             # Página inicial
│       ├── noticia.html           # Lista de notícias
│       └── noticia_detail.html    # Detalhes da notícia
│
├── .git/                          # Controle de versão Git
├── .gitignore                     # Arquivos ignorados pelo Git
├── manage.py                      # Script de gerenciamento Django
└── projecto_fim_curso.sqlite3     # Banco de dados SQLite
```

---

## ⚙️ Configurações

### Configurações Principais (settings.py)

#### Aplicações Instaladas
```python
INSTALLED_APPS = [
    'jazzmin',                          # Admin moderno
    'django.contrib.admin',             # Admin padrão
    'django.contrib.auth',              # Autenticação
    'django.contrib.contenttypes',      # Content types
    'django.contrib.sessions',          # Sessões
    'django.contrib.messages',          # Mensagens
    'django.contrib.staticfiles',       # Arquivos estáticos
    'pages.apps.PagesConfig',           # App de notícias
]
```

#### Internacionalização
```python
LANGUAGE_CODE = 'pt-ao'              # Português de Angola
TIME_ZONE = 'Africa/Luanda'          # Fuso horário de Luanda
USE_I18N = True                      # Internacionalização
USE_TZ = True                        # Timezone aware
```

#### Arquivos Estáticos
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, STATIC_URL)
]
```

#### Configuração Jazzmin
```python
JAZZMIN_SETTINGS = {
    "site_title": "Painel Administrativo",
    "site_header": "Painel de Noticias do IPM",
    "site_brand": "IPM Noticias",
    "site_logo": "images/favicon.ico",
    "welcome_sign": "Bem-vindo ao painel administrativo!",
    "copyright": "© 2025 Grupo Numero 6",
    "theme": "darkly",
    "sidebar": "dark",
    "navigation_expanded": True,
    
    "icons": {
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "pages.Noticia": "far fa-newspaper",
        "pages.Categoria": "fas fa-tags",
    },
}
```

---

## 🌐 Rotas e URLs

### URLs Principais (core/urls.py)

```python
urlpatterns = [
    path('admin/', admin.site.urls),      # Painel administrativo
    path('', include('pages.urls')),      # URLs do app pages
]
```

### URLs do App Pages (pages/urls.py)

| URL | View | Nome | Descrição |
|-----|------|------|-----------|
| `/` | IndexView | index | Página inicial com notícias, cursos e eventos |
| `/notices/` | NoticesView | notice | Lista paginada de todas as notícias |
| `/noticia/<uuid:pk>/` | NoticiaDetailView | noticia_detail | Detalhes de uma notícia específica |
| `/categoria/<str:categoria_nome>/` | CategoryNoticeView | category_news | Notícias filtradas por categoria |

### Exemplos de URLs

```
http://localhost:8000/                           # Página inicial
http://localhost:8000/notices/                   # Todas as notícias
http://localhost:8000/noticia/123e4567-e89b.../ # Detalhes da notícia
http://localhost:8000/categoria/Esporte/         # Notícias de esporte
http://localhost:8000/admin/                     # Painel administrativo
```

---

## 🎨 Views Implementadas

### 1. IndexView (ListView)
**Template:** `pages/index.html`  
**Função:** Exibe página inicial com notícias ativas, seção de cursos e próximos eventos

**Contexto:**
- `noticias`: Todas as notícias com status=True
- `eventos`: Próximos 5 eventos ordenados por data

---

### 2. NoticesView (ListView)
**Template:** `pages/noticia.html`  
**Função:** Lista todas as notícias com paginação

**Configuração:**
- Paginação: 6 notícias por página
- Filtro: Apenas notícias ativas (status=True)

---

### 3. NoticiaDetailView (DetailView)
**Template:** `pages/noticia_detail.html`  
**Função:** Exibe detalhes completos de uma notícia

**Contexto:**
- `noticia`: Notícia selecionada
- `destaques`: 3 outras notícias recentes (excluindo a atual)

---

### 4. CategoryNoticeView (ListView)
**Template:** `pages/noticia.html`  
**Função:** Lista notícias filtradas por categoria

**Configuração:**
- Paginação: 6 notícias por página
- Filtro: Por categoria e status=True
- Contexto adicional: `categoria_ativa`

---

## 🛠️ Painel Administrativo

### Funcionalidades do Admin

#### NoticiaAdmin
**Campos de Lista:**
- Título
- Categoria
- Autor
- Data de publicação
- Status (editável inline)

**Filtros:**
- Status
- Categoria
- Data de publicação
- Autor

**Busca:**
- Título
- Subtítulo
- Conteúdo
- Autor

**Hierarquia:** Por data de publicação

---

#### CategoriaAdmin
**Campos de Lista:**
- Categoria
- Data de criação

**Busca:** Por nome da categoria

**Campos Somente Leitura:** `criado_em`

---

#### EventoAdmin
**Campos de Lista:**
- Título
- Data do evento
- Data de criação

**Filtros:** Por data do evento

**Ordenação:** Por data do evento

---

## 📦 Dependências do Projeto

```
Django==4.2.27
django-jazzmin
Pillow
```

---

## 🚀 Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone <url-do-repositorio>
cd projecto-fim-curso
```

### 2. Criar Ambiente Virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instalar Dependências
```bash
pip install django django-jazzmin Pillow
```

### 4. Aplicar Migrações
```bash
python manage.py migrate
```

### 5. Criar Superusuário
```bash
python manage.py createsuperuser
```

### 6. Executar Servidor
```bash
python manage.py runserver
```

### 7. Acessar o Sistema
- **Portal:** http://localhost:8000/
- **Admin:** http://localhost:8000/admin/

---

## 👨‍💻 Equipe de Desenvolvimento

**Grupo Número 6**  
Instituto Politécnico de Malanje (IPM)  
Ano: 2025

---

## 📄 Licença

Este projeto foi desenvolvido como projeto de fim de curso para o Instituto Politécnico de Malanje.

---

## 📞 Suporte

Para dúvidas ou sugestões sobre o projeto, entre em contato com a equipe de desenvolvimento.

---

**Última Atualização:** Janeiro de 2026  
**Versão da Documentação:** 1.0
