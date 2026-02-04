# 📊 DIAGRAMAS UML DO SISTEMA
## Portal de Notícias IPM

**Data:** 04 de Fevereiro de 2026  
**Versão:** 2.0 (Atualizada)  
**Status:** Sistema em Produção (95% completo)

---

## 📋 ÍNDICE

1. [Diagrama de Casos de Uso](#diagrama-de-casos-de-uso)
2. [Diagrama de Classes](#diagrama-de-classes)
3. [Diagrama de Objetos](#diagrama-de-objetos)
4. [Diagrama Entidade-Relacionamento (ER)](#diagrama-entidade-relacionamento)
5. [Diagrama de Implementação](#diagrama-de-implementação)
6. [Diagrama de Sequência](#diagrama-de-sequência)
7. [Diagrama de Atividades](#diagrama-de-atividades)

---

## 1. DIAGRAMA DE CASOS DE USO

### Descrição
Representa as funcionalidades do sistema e como os diferentes atores interagem com elas.

### Atores
- **Visitante**: Usuário não autenticado
- **Aluno**: Usuário autenticado (estudante do IPM)
- **Administrador**: Gestor do sistema

```mermaid
graph TB
    subgraph "Portal de Notícias IPM"
        %% Casos de Uso - Visitante
        UC1[Visualizar Notícias Públicas]
        UC2[Filtrar Notícias por Categoria]
        UC3[Ver Detalhes da Notícia]
        UC4[Visualizar Eventos]
        UC5[Ver Detalhes do Evento]
        UC6[Criar Conta de Aluno]
        UC7[Fazer Login]
        
        %% Casos de Uso - Aluno
        UC8[Visualizar Notícias Exclusivas]
        UC9[Inscrever-se em Evento]
        UC10[Cancelar Inscrição]
        UC11[Ver Minhas Inscrições]
        UC12[Visualizar Meu Perfil]
        UC13[Fazer Logout]
        
        %% Casos de Uso - Admin
        UC14[Criar Notícia]
        UC15[Editar Notícia]
        UC16[Excluir Notícia]
        UC17[Criar Evento]
        UC18[Editar Evento]
        UC19[Excluir Evento]
        UC20[Gerenciar Categorias]
        UC21[Gerenciar Alunos]
        UC22[Ver Inscritos em Evento]
    end
    
    %% Atores
    Visitante((Visitante))
    Aluno((Aluno))
    Admin((Administrador))
    
    %% Relacionamentos - Visitante
    Visitante --> UC1
    Visitante --> UC2
    Visitante --> UC3
    Visitante --> UC4
    Visitante --> UC5
    Visitante --> UC6
    Visitante --> UC7
    
    %% Relacionamentos - Aluno (herda de Visitante)
    Aluno --> UC1
    Aluno --> UC2
    Aluno --> UC3
    Aluno --> UC4
    Aluno --> UC5
    Aluno --> UC8
    Aluno --> UC9
    Aluno --> UC10
    Aluno --> UC11
    Aluno --> UC12
    Aluno --> UC13
    
    %% Relacionamentos - Admin
    Admin --> UC14
    Admin --> UC15
    Admin --> UC16
    Admin --> UC17
    Admin --> UC18
    Admin --> UC19
    Admin --> UC20
    Admin --> UC21
    Admin --> UC22
    
    %% Extends e Includes
    UC9 -.->|extends| UC5
    UC10 -.->|extends| UC11
    UC3 -.->|includes| UC2
```

### Descrição dos Casos de Uso

#### **Visitante:**
1. **UC1 - Visualizar Notícias Públicas**: Ver lista de notícias não exclusivas
2. **UC2 - Filtrar Notícias por Categoria**: Filtrar notícias por categoria específica
3. **UC3 - Ver Detalhes da Notícia**: Visualizar conteúdo completo de uma notícia
4. **UC4 - Visualizar Eventos**: Ver lista de eventos (próximos e passados)
5. **UC5 - Ver Detalhes do Evento**: Visualizar informações completas do evento
6. **UC6 - Criar Conta de Aluno**: Registrar-se como aluno no sistema
7. **UC7 - Fazer Login**: Autenticar-se no sistema

#### **Aluno (herda funcionalidades do Visitante):**
8. **UC8 - Visualizar Notícias Exclusivas**: Acessar notícias marcadas como exclusivas
9. **UC9 - Inscrever-se em Evento**: Fazer inscrição em evento com vagas disponíveis
10. **UC10 - Cancelar Inscrição**: Cancelar inscrição em evento
11. **UC11 - Ver Minhas Inscrições**: Listar todos os eventos inscritos
12. **UC12 - Visualizar Meu Perfil**: Ver dados pessoais e histórico
13. **UC13 - Fazer Logout**: Sair do sistema

#### **Administrador:**
14. **UC14 - Criar Notícia**: Adicionar nova notícia ao sistema
15. **UC15 - Editar Notícia**: Modificar notícia existente
16. **UC16 - Excluir Notícia**: Remover notícia do sistema
17. **UC17 - Criar Evento**: Adicionar novo evento
18. **UC18 - Editar Evento**: Modificar evento existente
19. **UC19 - Excluir Evento**: Remover evento
20. **UC20 - Gerenciar Categorias**: CRUD de categorias de notícias
21. **UC21 - Gerenciar Alunos**: Visualizar e gerenciar alunos cadastrados
22. **UC22 - Ver Inscritos em Evento**: Listar alunos inscritos em cada evento

---

## 2. DIAGRAMA DE CLASSES

### Descrição
Representa a estrutura estática do sistema, mostrando classes, atributos, métodos e relacionamentos.

```mermaid
classDiagram
    %% Classe User (Django padrão)
    class User {
        +int id
        +string username
        +string email
        +string first_name
        +string last_name
        +string password
        +boolean is_staff
        +boolean is_active
        +datetime date_joined
        +get_full_name()
        +check_password()
    }
    
    %% Classe Aluno
    class Aluno {
        +UUID id
        +User user
        +string numero_estudante
        +string curso
        +int ano_ingresso
        +string telefone
        +ImageField foto
        +datetime criado_em
        +__str__()
    }
    
    %% Classe Categoria
    class Categoria {
        +UUID id
        +string categoria
        +datetime criado_em
        +__str__()
    }
    
    %% Classe Noticia
    class Noticia {
        +UUID id
        +string titulo
        +string subtitulo
        +TextField conteudo
        +Categoria categoria
        +ImageField imagem
        +datetime publicado_em
        +boolean status
        +boolean exclusivo_alunos
        +datetime criado_em
        +datetime atualizado_em
        +__str__()
    }
    
    %% Classe Evento
    class Evento {
        +UUID id
        +string titulo
        +TextField descricao
        +date data
        +int vagas
        +datetime criado_em
        +vagas_disponiveis()
        +__str__()
    }
    
    %% Classe InscricaoEvento
    class InscricaoEvento {
        +UUID id
        +Aluno aluno
        +Evento evento
        +datetime data_inscricao
        +boolean confirmado
        +__str__()
    }
    
    %% Relacionamentos
    User "1" --> "1" Aluno : possui
    Categoria "1" --> "0..*" Noticia : categoriza
    Evento "1" --> "0..*" InscricaoEvento : tem
    Aluno "1" --> "0..*" InscricaoEvento : faz
    
    %% Notas
    note for User "Modelo padrão do Django\ndjango.contrib.auth.models"
    note for InscricaoEvento "Relacionamento Many-to-Many\nentre Aluno e Evento"
```

### Detalhamento das Classes

#### **User (Django Auth)**
- Modelo padrão do Django para autenticação
- Gerencia credenciais e permissões

#### **Aluno**
- Estende User com informações acadêmicas
- Relacionamento OneToOne com User
- Armazena dados específicos do estudante

#### **Categoria**
- Classifica notícias por tema
- Relacionamento OneToMany com Notícia

#### **Noticia**
- Conteúdo principal do portal
- Pode ser pública ou exclusiva para alunos
- Possui categoria, imagem e status

#### **Evento**
- Eventos institucionais do IPM
- Controla vagas disponíveis
- Método `vagas_disponiveis()` calcula vagas restantes

#### **InscricaoEvento**
- Tabela de associação entre Aluno e Evento
- Implementa Many-to-Many com dados extras
- Unique constraint: um aluno não pode se inscrever duas vezes no mesmo evento

---

## 3. DIAGRAMA DE OBJETOS

### Descrição
Mostra instâncias específicas das classes em um momento particular do sistema.

```mermaid
graph TB
    subgraph "Instâncias do Sistema - 04/02/2026"
        %% Objetos User
        user1["user1: User<br/>username: 'joao.silva'<br/>email: 'joao@ipm.edu.ao'<br/>first_name: 'João'<br/>last_name: 'Silva'"]
        
        user2["user2: User<br/>username: 'maria.costa'<br/>email: 'maria@ipm.edu.ao'<br/>first_name: 'Maria'<br/>last_name: 'Costa'"]
        
        %% Objetos Aluno
        aluno1["aluno1: Aluno<br/>numero_estudante: '20240001'<br/>curso: 'Informática'<br/>ano_ingresso: 2024<br/>telefone: '+244 923 456 789'"]
        
        aluno2["aluno2: Aluno<br/>numero_estudante: '20240002'<br/>curso: 'Gestão'<br/>ano_ingresso: 2024<br/>telefone: '+244 923 456 790'"]
        
        %% Objetos Categoria
        cat1["cat1: Categoria<br/>categoria: 'Esportes'"]
        cat2["cat2: Categoria<br/>categoria: 'Tecnologia'"]
        
        %% Objetos Noticia
        noticia1["noticia1: Noticia<br/>titulo: 'Aluno do IPM Vence...'<br/>categoria: cat1<br/>status: True<br/>exclusivo_alunos: False"]
        
        noticia2["noticia2: Noticia<br/>titulo: 'Hackathon IPM 2026'<br/>categoria: cat2<br/>status: True<br/>exclusivo_alunos: True"]
        
        %% Objetos Evento
        evento1["evento1: Evento<br/>titulo: 'Hackathon IPM 2026'<br/>data: 2026-03-16<br/>vagas: 50"]
        
        %% Objetos InscricaoEvento
        insc1["insc1: InscricaoEvento<br/>aluno: aluno1<br/>evento: evento1<br/>confirmado: True<br/>data_inscricao: 2026-02-04"]
        
        insc2["insc2: InscricaoEvento<br/>aluno: aluno2<br/>evento: evento1<br/>confirmado: True<br/>data_inscricao: 2026-02-04"]
    end
    
    %% Links entre objetos
    user1 -.-> aluno1
    user2 -.-> aluno2
    cat1 -.-> noticia1
    cat2 -.-> noticia2
    aluno1 -.-> insc1
    aluno2 -.-> insc2
    evento1 -.-> insc1
    evento1 -.-> insc2
```

### Cenário Representado
- **2 Alunos** cadastrados no sistema
- **2 Categorias** de notícias
- **2 Notícias** publicadas (1 pública, 1 exclusiva)
- **1 Evento** (Hackathon IPM 2026)
- **2 Inscrições** no evento

---

## 4. DIAGRAMA ENTIDADE-RELACIONAMENTO (ER)

### Descrição
Modelo de dados do banco de dados relacional (SQLite3).

```mermaid
erDiagram
    USER ||--|| ALUNO : possui
    CATEGORIA ||--o{ NOTICIA : categoriza
    EVENTO ||--o{ INSCRICAO_EVENTO : tem
    ALUNO ||--o{ INSCRICAO_EVENTO : faz
    
    USER {
        int id PK
        string username UK
        string email
        string first_name
        string last_name
        string password
        boolean is_staff
        boolean is_active
        boolean is_superuser
        datetime date_joined
        datetime last_login
    }
    
    ALUNO {
        uuid id PK
        int user_id FK
        string numero_estudante UK
        string curso
        int ano_ingresso
        string telefone
        string foto
        datetime criado_em
    }
    
    CATEGORIA {
        uuid id PK
        string categoria UK
        datetime criado_em
    }
    
    NOTICIA {
        uuid id PK
        string titulo
        string subtitulo
        text conteudo
        uuid categoria_id FK
        string imagem
        datetime publicado_em
        boolean status
        boolean exclusivo_alunos
        datetime criado_em
        datetime atualizado_em
    }
    
    EVENTO {
        uuid id PK
        string titulo
        text descricao
        date data
        int vagas
        datetime criado_em
    }
    
    INSCRICAO_EVENTO {
        uuid id PK
        uuid aluno_id FK
        uuid evento_id FK
        datetime data_inscricao
        boolean confirmado
    }
```

### Cardinalidades e Restrições

#### **USER ↔ ALUNO** (1:1)
- Um User possui exatamente um Aluno
- Um Aluno pertence a exatamente um User
- `ON DELETE CASCADE`: Se User for deletado, Aluno também é

#### **CATEGORIA ↔ NOTICIA** (1:N)
- Uma Categoria pode ter várias Notícias
- Uma Notícia pertence a uma Categoria
- `ON DELETE PROTECT`: Não pode deletar Categoria com Notícias

#### **EVENTO ↔ INSCRICAO_EVENTO** (1:N)
- Um Evento pode ter várias Inscrições
- Uma Inscrição pertence a um Evento
- `ON DELETE CASCADE`: Se Evento for deletado, Inscrições também são

#### **ALUNO ↔ INSCRICAO_EVENTO** (1:N)
- Um Aluno pode ter várias Inscrições
- Uma Inscrição pertence a um Aluno
- `ON DELETE CASCADE`: Se Aluno for deletado, Inscrições também são

#### **Constraints Únicos:**
- `USER.username`: Único
- `ALUNO.numero_estudante`: Único
- `CATEGORIA.categoria`: Único
- `INSCRICAO_EVENTO(aluno_id, evento_id)`: Único (um aluno não pode se inscrever duas vezes no mesmo evento)

---

## 5. DIAGRAMA DE IMPLEMENTAÇÃO

### Descrição
Mostra a arquitetura física do sistema, componentes de hardware e software.

```mermaid
graph TB
    subgraph "Cliente - Navegador Web"
        Browser[Navegador<br/>Chrome/Firefox/Edge]
        HTML[HTML5]
        CSS[CSS3]
        JS[JavaScript]
        
        Browser --> HTML
        Browser --> CSS
        Browser --> JS
    end
    
    subgraph "Servidor Web - Windows"
        subgraph "Django Application Server"
            Django[Django 5.2.7<br/>Python 3.11]
            
            subgraph "Apps Django"
                PagesApp[pages app]
                CoreApp[core app]
            end
            
            subgraph "Middleware"
                Auth[Authentication]
                Session[Session Management]
                CSRF[CSRF Protection]
                Static[Static Files]
            end
            
            subgraph "Templates"
                Jinja[Django Templates]
            end
            
            Django --> PagesApp
            Django --> CoreApp
            Django --> Auth
            Django --> Session
            Django --> CSRF
            Django --> Static
            Django --> Jinja
        end
        
        subgraph "Admin Interface"
            Jazzmin[Django Jazzmin<br/>Admin Theme]
        end
        
        subgraph "Banco de Dados"
            SQLite[(SQLite3<br/>projecto_fim_curso.sqlite3)]
        end
        
        subgraph "Arquivos Estáticos"
            StaticFiles[/static/<br/>CSS, JS, Images]
            MediaFiles[/media/<br/>Uploads]
        end
    end
    
    subgraph "Bibliotecas Python"
        Pillow[Pillow<br/>Image Processing]
        UUID[UUID<br/>Unique IDs]
    end
    
    %% Conexões
    Browser -->|HTTP/HTTPS| Django
    Django --> SQLite
    Django --> StaticFiles
    Django --> MediaFiles
    Django --> Jazzmin
    Django --> Pillow
    Django --> UUID
    
    %% Protocolo
    Browser -.->|Request/Response| Django
```

### Componentes do Sistema

#### **Cliente (Browser)**
- **Tecnologias**: HTML5, CSS3, JavaScript
- **Navegadores Suportados**: Chrome, Firefox, Edge, Safari
- **Responsivo**: Mobile, Tablet, Desktop

#### **Servidor de Aplicação**
- **Framework**: Django 5.2.7
- **Linguagem**: Python 3.11.9
- **SO**: Windows
- **Servidor Web**: Django Development Server (Produção: Gunicorn/uWSGI)

#### **Apps Django**
- **pages**: Lógica de negócio (views, models, forms)
- **core**: Configurações do projeto

#### **Middleware**
- **Authentication**: django.contrib.auth
- **Session**: django.contrib.sessions
- **CSRF**: django.middleware.csrf
- **Static Files**: django.contrib.staticfiles

#### **Banco de Dados**
- **SGBD**: SQLite3
- **Arquivo**: `projecto_fim_curso.sqlite3`
- **ORM**: Django ORM

#### **Interface Admin**
- **Framework**: Django Admin
- **Tema**: Jazzmin (darkly theme)

#### **Arquivos**
- **Static**: CSS, JavaScript, Imagens (logo, ícones)
- **Media**: Uploads de usuários (fotos de perfil, imagens de notícias)

#### **Bibliotecas**
- **Pillow**: Processamento de imagens
- **UUID**: Geração de IDs únicos

---

## 6. DIAGRAMA DE SEQUÊNCIA

### Caso de Uso: Inscrever-se em Evento

```mermaid
sequenceDiagram
    actor Aluno
    participant Browser
    participant Django
    participant View as InscreverEventoView
    participant Model as Evento/InscricaoEvento
    participant DB as SQLite3
    
    Aluno->>Browser: Clica em "Inscrever-me"
    Browser->>Django: POST /evento/{id}/inscrever/
    Django->>View: Processa requisição
    
    View->>View: Verifica autenticação
    alt Não autenticado
        View-->>Browser: Redirect para login
        Browser-->>Aluno: Página de login
    else Autenticado
        View->>Model: Busca Evento(id)
        Model->>DB: SELECT * FROM evento WHERE id=?
        DB-->>Model: Dados do evento
        Model-->>View: Objeto Evento
        
        View->>View: Verifica se é aluno
        alt Não é aluno
            View-->>Browser: Mensagem de erro
            Browser-->>Aluno: "Apenas alunos podem se inscrever"
        else É aluno
            View->>Model: Verifica inscrição existente
            Model->>DB: SELECT * FROM inscricao WHERE aluno=? AND evento=?
            DB-->>Model: Resultado
            
            alt Já inscrito
                View-->>Browser: Mensagem de aviso
                Browser-->>Aluno: "Você já está inscrito"
            else Não inscrito
                View->>Model: Verifica vagas disponíveis
                Model->>DB: COUNT inscrições
                DB-->>Model: Total de inscritos
                Model-->>View: Vagas disponíveis
                
                alt Sem vagas
                    View-->>Browser: Mensagem de erro
                    Browser-->>Aluno: "Vagas esgotadas"
                else Com vagas
                    View->>Model: Cria InscricaoEvento
                    Model->>DB: INSERT INTO inscricao_evento
                    DB-->>Model: Sucesso
                    Model-->>View: Inscrição criada
                    View-->>Browser: Mensagem de sucesso
                    Browser-->>Aluno: "Inscrição realizada com sucesso!"
                end
            end
        end
    end
```

---

## 7. DIAGRAMA DE ATIVIDADES

### Fluxo: Publicar Notícia (Administrador)

```mermaid
flowchart TD
    Start([Início]) --> Login{Admin<br/>logado?}
    Login -->|Não| RedirectLogin[Redirecionar para Login]
    RedirectLogin --> End([Fim])
    
    Login -->|Sim| AccessAdmin[Acessar Django Admin]
    AccessAdmin --> SelectNoticias[Selecionar 'Notícias']
    SelectNoticias --> ClickAdd[Clicar 'Adicionar Notícia']
    
    ClickAdd --> FillForm[Preencher Formulário]
    FillForm --> FillTitle[Título]
    FillTitle --> FillSubtitle[Subtítulo]
    FillSubtitle --> FillContent[Conteúdo]
    FillContent --> SelectCategory[Selecionar Categoria]
    SelectCategory --> UploadImage{Upload<br/>Imagem?}
    
    UploadImage -->|Sim| AddImage[Adicionar Imagem]
    UploadImage -->|Não| SetDate
    AddImage --> SetDate[Definir Data de Publicação]
    
    SetDate --> SetStatus{Publicar<br/>agora?}
    SetStatus -->|Sim| StatusActive[Status = Ativo]
    SetStatus -->|Não| StatusInactive[Status = Inativo]
    
    StatusActive --> SetExclusive{Exclusivo<br/>para alunos?}
    StatusInactive --> SetExclusive
    
    SetExclusive -->|Sim| ExclusiveTrue[Exclusivo = True]
    SetExclusive -->|Não| ExclusiveFalse[Exclusivo = False]
    
    ExclusiveTrue --> ValidateForm{Formulário<br/>válido?}
    ExclusiveFalse --> ValidateForm
    
    ValidateForm -->|Não| ShowErrors[Mostrar Erros]
    ShowErrors --> FillForm
    
    ValidateForm -->|Sim| SaveDB[Salvar no Banco de Dados]
    SaveDB --> ShowSuccess[Mostrar Mensagem de Sucesso]
    ShowSuccess --> NotifyUsers{Notificar<br/>usuários?}
    
    NotifyUsers -->|Sim| SendNotification[Enviar Notificações]
    NotifyUsers -->|Não| End
    SendNotification --> End
```

---

## 📝 NOTAS IMPORTANTES

### Convenções Utilizadas
- **PK**: Primary Key (Chave Primária)
- **FK**: Foreign Key (Chave Estrangeira)
- **UK**: Unique Key (Chave Única)
- **UUID**: Universally Unique Identifier
- **1:1**: Relacionamento Um para Um
- **1:N**: Relacionamento Um para Muitos
- **N:M**: Relacionamento Muitos para Muitos

### Tecnologias de Diagramação
- **Mermaid**: Linguagem de diagramação em texto
- **Markdown**: Formato de documentação
- **GitHub/GitLab**: Renderização automática de diagramas

### Manutenção dos Diagramas
Estes diagramas devem ser atualizados sempre que houver:
- ✅ Novos modelos de dados
- ✅ Novos casos de uso
- ✅ Mudanças na arquitetura
- ✅ Novas funcionalidades
- ✅ Alterações em relacionamentos

---

**Última Atualização:** 04/02/2026 01:04  
**Desenvolvido por:** Grupo Número 6  
**Instituição:** Instituto Politécnico do Mayombe
