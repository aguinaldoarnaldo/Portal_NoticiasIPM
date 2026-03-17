# 📊 DIAGRAMAS UML DO SISTEMA
## Portal de Notícias IPM

**Data:** 17 de Março de 2026  
**Versão:** 3.0 (Atualizada)  
**Status:** Sistema em Produção (Concluído)

---

## 📋 ÍNDICE

1. [Diagrama de Casos de Uso](#diagrama-de-casos-de-uso)
2. [Diagrama de Classes](#diagrama-de-classes)
3. [Diagrama de Objetos](#diagrama-de-objetos)
4. [Diagrama Entidade-Relacionamento (ER)](#diagrama-entidade-relacionamento)
5. [Diagrama de Implementação](#diagrama-de-implementação)
6. [Diagrama de Sequência](#diagrama-de-sequência)
7. [Diagrama de Atividades](#diagrama-de-atividades)
8. [Diagrama de Navegação e Fluxo do Sistema](#diagrama-de-navegação-e-fluxo-do-sistema)

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
        UC21[Gerenciar Alunos]
        UC22[Ver Inscritos em Evento]
        UC23[Editar Meu Perfil]
        UC24[Inscrever-se como Visitante]
    end
    
    %% Atores
    Visitante((Visitante))
    Aluno((Aluno))
    Gestor((Gestor de Conteúdo))
    Admin((Administrador Geral))
    
    %% Relacionamentos - Visitante
    Visitante --> UC1
    Visitante --> UC2
    Visitante --> UC3
    Visitante --> UC4
    Visitante --> UC5
    Visitante --> UC6
    Visitante --> UC7
    Visitante --> UC24
    
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
    Aluno --> UC23

    %% Relacionamentos - Gestor (Focado em Conteúdo)
    Gestor --> UC7
    Gestor --> UC14
    Gestor --> UC15
    Gestor --> UC17
    Gestor --> UC18
    Gestor --> UC20
    Gestor --> UC22
    
    %% Relacionamentos - Admin (Controle Total)
    Admin --> UC7
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
23. **UC23 - Editar Meu Perfil**: Atualizar dados cadastrais e foto

#### **Visitante (Funcionalidades Adicionais):**
24. **UC24 - Inscrever-se como Visitante**: Inscrição em eventos não exclusivos preenchendo formulário externo.

#### **Gestor de Conteúdo (Staff):**
- Operador do sistema focado em manter o portal atualizado.
14. **UC14 - Criar Notícia**
15. **UC15 - Editar Notícia**
17. **UC17 - Criar Evento**
20. **UC20 - Gerenciar Categorias**

#### **Administrador Geral (Superuser):**
- Possui controle total, incluindo gestão de pessoas e exclusões críticas.
16. **UC16 - Excluir Notícia** (Apenas Admin pode apagar permanentemente)
19. **UC19 - Excluir Evento**
21. **UC21 - Gerenciar Alunos** (Aprovação de contas e perfis)
22. **UC22 - Ver Inscritos em Evento**

---

## 2. DIAGRAMA DE CLASSES

### Descrição
Representa a estrutura estática do sistema, mostrando classes, atributos, métodos e relacionamentos.

```mermaid
classDiagram
    %% Classe User (Django padrão)
    class User {
        -int id
        -string username
        -string email
        -string first_name
        -string last_name
        -string password
        -boolean is_staff
        -boolean is_active
        -datetime date_joined
        +obter_nome_completo()
        +obter_nome_curto()
        +verificar_senha(senha)
        +definir_senha(senha)
    }
    
    %% Classe Aluno
    class Aluno {
        -UUID id
        -User user
        -string nome
        -string numero_estudante
        -string curso
        -int ano_ingresso
        -string telefone
        -ImageField foto
        -datetime criado_em
        +__str__()
        +obter_meus_eventos()
        +atualizar_dados_perfil()
    }
    
    %% Classe Categoria
    class Categoria {
        -UUID id
        -string categoria
        -datetime criado_em
        +__str__()
        +contar_noticias()
    }
    
    %% Classe Noticia
    class Noticia {
        -UUID id
        -string titulo
        -string subtitulo
        -TextField conteudo
        -string autor
        -Categoria categoria
        -ImageField imagem
        -datetime publicado_em
        -datetime atualizado_em
        -boolean status
        -boolean exclusivo_alunos
        -datetime criado_em
        +__str__()
        +obter_url_absoluta()
        +e_recente()
    }
    
    %% Classe Evento
    class Evento {
        -UUID id
        -string titulo
        -TextField descricao
        -date data
        -int vagas
        -boolean exclusivo_alunos
        -datetime criado_em
        +__str__()
        +vagas_disponiveis()
        +esta_lotado()
    }
    
    %% Classe InscricaoEvento
    class InscricaoEvento {
        -UUID id
        -Aluno aluno
        -Evento evento
        -string nome_externo
        -string email_externo
        -string telefone_externo
        -datetime data_inscricao
        -boolean confirmado
        +__str__()
        +confirmar_inscricao()
        +e_externo()
    }
    
    %% Relacionamentos
    User "1" <|-- "1" Administrador_Geral : é um (Superuser)
    User "1" <|-- "1" Gestor_Conteudo : é um (Staff)
    User "1" --> "0..1" Aluno : possui
    
    Gestor_Conteudo "1" --> "0..*" Noticia : cria/edita
    Gestor_Conteudo "1" --> "0..*" Evento : cria/edita
    
    Administrador_Geral "1" --> "1" Gestor_Conteudo : supervisiona
    Administrador_Geral "1" --> "0..*" Aluno : gerencia
    Administrador_Geral "1" --> "0..*" Noticia : modera/exclui
    
    Categoria "1" --> "0..*" Noticia : categoriza
    
    Evento "1" --> "0..*" InscricaoEvento : possui
    Aluno "1" --> "0..*" InscricaoEvento : realiza
    Visitante "1" --> "0..*" InscricaoEvento : realiza (externo)
    
    %% Notas
    note for User "Modelo central de Autenticação"
    note for Administrador "Usuário com is_staff=True\nAcesso total ao Back-office"
    note for Visitante "Usuário não autenticado\nPode ver notícias e se inscrever em eventos"
    note for InscricaoEvento "Pode estar ligada a um Aluno\nOU conter dados de um Visitante"
```

### Detalhamento das Classes

#### **User (Django Auth)**
- Modelo central do Django para autenticação.
- Gerencia credenciais e permissões.

#### **Administrador**
- Especialização do `User` com permissões elevadas.
- Responsável por todo o CRUD (Criar, Ler, Atualizar, Deletar) do sistema.

#### **Visitante**
- Representa o público externo.
- Embora não tenha conta no banco, interage com o sistema através de inscrições em eventos (usando campos externos na tabela `InscricaoEvento`).

#### **Aluno**
- Estende `User` com informações acadêmicas.
- Relacionamento Opcional (0..1) com `User` (pois o perfil pode ser criado depois ou o aluno pode ser pré-cadastrado).
- Armazena dados específicos do estudante.

#### **Categoria**
- Classifica notícias por tema.
- Relacionamento Um-para-Muitos com Notícia.

#### **Noticia**
- Conteúdo principal do portal.
- Pode ser pública ou exclusiva para alunos.
- Possui categoria, imagem e status.

#### **Evento**
- Eventos institucionais do IPM.
- Controla vagas disponíveis e visibilidade.

#### **InscricaoEvento**
- Tabela que registra o interesse em um evento.
- **Flexível**: Pode apontar para um `Aluno` cadastrado OU armazenar `nome/email` de um `Visitante`.
- Implementa Many-to-Many ou Inscrição Singular
- Possui campos para dados externos (`nome`, `email`, `telefone`) caso o inscrito não seja um Aluno logado.
- Unique constraint: um aluno (ou email externo) não pode se inscrever duas vezes no mesmo evento

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
- **2 Inscrições** no evento (podendo ser Alunos ou Externos)

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
        uuid aluno_id FK "pode ser null"
        uuid evento_id FK
        string nome_externo
        string email_externo
        string telefone_externo
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
            View->>Model: Verifica se evento é exclusivo
            alt Exclusivo para Alunos
                View-->>Browser: Mensagem de erro
                Browser-->>Aluno: "Apenas alunos podem se inscrever"
            else Aberto ao Público
                View->>View: Processa inscrição externa (nome, email)
                View->>Model: Salva InscricaoEvento com dados externos
                Model->>DB: INSERT INTO inscricao_evento
                DB-->>Model: Sucesso
                View-->>Browser: Mensagem de sucesso
                Browser-->>Aluno: "Inscrição realizada com sucesso!"
            end
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
                    View->>Model: Cria InscricaoEvento para Aluno
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

## 8. DIAGRAMA DE NAVEGAÇÃO E FLUXO DO SISTEMA

### Descrição
Representa a jornada do dado, desde a criação na **Parte Administrativa (Back-Office)** até o consumo e interação no **Portal Público (Front-Office)**.

```mermaid
graph TD
    subgraph AdminSection ["🛡️ PARTE ADMINISTRATIVA (DJANGO ADMIN - JAZZMIN)"]
        A1[Login Admin] --> A2[Painel de Controle]
        A2 --> A3{Gerenciar Dados}
        A3 -->|CRUD| A4[Notícias e Categorias]
        A3 -->|CRUD| A5[Eventos e Vagas]
        A3 -->|CRUD| A6[Usuários e Alunos]
        
        A4 & A5 & A6 --> DB[(Banco de Dados<br/>SQLite3)]
    end

    subgraph PortalSection ["🌐 PORTAL DE NOTÍCIAS (FRONT-OFFICE)"]
        P1[Usuário Acessa Home] --> P2{Tipo de Usuário?}
        
        P2 -->|Visitante| P3[Home / Notícias Públicas]
        P2 -->|Aluno Logado| P4[Home / Todas as Notícias]
        
        P3 --> P5[Filtrar por Categoria]
        P3 --> P6[Ver Eventos Públicos]
        P3 --> P7[Assistir Banner Destaque]
        
        P4 --> P8[Acessar Notícias Exclusivas]
        P4 --> P9[Inscrição em Eventos]
        P4 --> P10[Meu Perfil / Histórico]
        
        P9 --> P11{Inscrição Válida?}
        P11 -->|Sim| DB
        P11 -->|Não| P9
    end

    %% Conexão entre mundos
    DB -.->|Provê dados| P1
    DB -.->|Armazena| A4
    DB -.->|Armazena| A5
    DB -.->|Armazena| A6

    %% Estilos
    style AdminSection fill:#f9f,stroke:#333,stroke-width:2px
    style PortalSection fill:#bbf,stroke:#333,stroke-width:2px
    style DB fill:#ff9,stroke:#333,stroke-width:4px
```

### Explicação do Fluxo:
1. **Alimentação (Admin):** O Administrador preenche as notícias, cria eventos e gerencia as categorias através do tema **Jazzmin**. Todos esses dados são persistidos no **SQLite3**.
2. **Consumo (Portal):** Quando um Visitante ou Aluno acessa o portal, o Django verifica no banco o que pode ser exibido (ex: `status=True`, `exclusivo_alunos=False`).
3. **Interação (Portal -> Admin):** As inscrições realizadas por alunos ou visitantes externos circulam do Portal para o Banco de Dados, onde ficam disponíveis no Admin para conferência.
4. **Segregação:** Este fluxo demonstra como as configurações feitas no **Back-office** impactam diretamente a experiência do usuário no **Front-office**.

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

**Última Atualização:** 17/03/2026 17:55  
**Desenvolvido por:** Grupo Número 6  
**Instituição:** Instituto Politécnico do Mayombe
