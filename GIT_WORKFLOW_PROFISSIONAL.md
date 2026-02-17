# 🎯 GUIA PROFISSIONAL: GIT WORKFLOW COMPLETO
## Do Zero ao Pull Request Aprovado

**Data:** 04 de Fevereiro de 2026  
**Projeto:** Portal de Notícias IPM  
**Metodologia:** Git Flow Profissional

---

## 📋 ÍNDICE

1. [Preparação Inicial](#1-preparação-inicial)
2. [Criar Nova Branch](#2-criar-nova-branch)
3. [Desenvolver Funcionalidade](#3-desenvolver-funcionalidade)
4. [Commits Profissionais](#4-commits-profissionais)
5. [Sincronizar com Remoto](#5-sincronizar-com-remoto)
6. [Criar Pull Request](#6-criar-pull-request)
7. [Code Review](#7-code-review)
8. [Merge e Finalização](#8-merge-e-finalização)

---

## 1. PREPARAÇÃO INICIAL

### 1.1 Verificar Estado Atual

```bash
# Ver branch atual e status
git status

# Ver todas as branches
git branch -a

# Ver histórico de commits
git log --oneline -5
```

**Saída esperada:**
```
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

### 1.2 Atualizar Branch Principal

```bash
# Garantir que estás na branch main
git checkout main

# Baixar últimas alterações do GitHub
git pull origin main

# Verificar se está atualizado
git status
```

**⚠️ IMPORTANTE:** Sempre começa de uma branch main atualizada!

---

## 2. CRIAR NOVA BRANCH

### 2.1 Nomenclatura de Branches (Padrão Profissional)

**Formato:** `tipo/descrição-curta`

**Tipos:**
- `feature/` - Nova funcionalidade
- `bugfix/` - Correção de bug
- `hotfix/` - Correção urgente em produção
- `refactor/` - Refatoração de código
- `docs/` - Documentação
- `test/` - Testes

**Exemplos:**
```
feature/sistema-inscricao-eventos
feature/perfil-aluno
bugfix/corrigir-logout-405
hotfix/admin-arquivos-estaticos
docs/atualizar-diagramas-uml
```

### 2.2 Criar e Mudar para Nova Branch

```bash
# Método 1: Criar e mudar em um comando (RECOMENDADO)
git checkout -b feature/sistema-inscricao-eventos

# Método 2: Criar e depois mudar (2 comandos)
git branch feature/sistema-inscricao-eventos
git checkout feature/sistema-inscricao-eventos

# Verificar que mudou de branch
git branch
# Saída: * feature/sistema-inscricao-eventos (o * indica branch atual)
```

**✅ Agora estás numa nova branch limpa, baseada na main!**

---

## 3. DESENVOLVER FUNCIONALIDADE

### 3.1 Fazer Alterações no Código

Desenvolve normalmente:
- Cria novos arquivos
- Modifica arquivos existentes
- Testa localmente

**Exemplo:**
```bash
# Criar novo template
# Editar views.py
# Atualizar urls.py
# etc.
```

### 3.2 Verificar Alterações

```bash
# Ver arquivos modificados
git status

# Ver diferenças detalhadas
git diff

# Ver diferenças de um arquivo específico
git diff pages/views.py
```

**Saída exemplo:**
```
Changes not staged for commit:
  modified:   pages/views.py
  modified:   pages/urls.py

Untracked files:
  pages/templates/pages/evento_detail.html
  pages/templates/pages/perfil.html
```

---

## 4. COMMITS PROFISSIONAIS

### 4.1 Padrão de Mensagens de Commit (Conventional Commits)

**Formato:**
```
tipo(escopo): descrição curta

Descrição detalhada (opcional)

Rodapé (opcional)
```

**Tipos:**
- `feat` - Nova funcionalidade
- `fix` - Correção de bug
- `docs` - Documentação
- `style` - Formatação (sem mudança de lógica)
- `refactor` - Refatoração
- `test` - Testes
- `chore` - Tarefas de manutenção

**Exemplos de boas mensagens:**
```
feat(eventos): adicionar página de detalhes do evento

- Criar template evento_detail.html
- Implementar EventoDetailView
- Adicionar validação de vagas disponíveis
- Configurar rota /evento/<id>/

Closes #42
```

```
fix(auth): corrigir erro 405 no logout

Alterar método de logout de GET para POST conforme
requisitos de segurança do Django.

Fixes #38
```

```
docs(uml): atualizar diagramas do sistema

- Adicionar diagrama de casos de uso
- Atualizar diagrama de classes
- Criar diagrama ER
```

### 4.2 Processo de Commit

#### **Opção A: Commit de Tudo (Desenvolvimento Rápido)**

```bash
# Adicionar TODOS os arquivos modificados
git add .

# Fazer commit com mensagem
git commit -m "feat(eventos): implementar sistema completo de inscrição

- Adicionar página de detalhes do evento
- Criar views de inscrição e cancelamento
- Implementar validação de vagas
- Adicionar página 'Minhas Inscrições'
- Criar página de perfil do aluno
- Corrigir logout para usar POST method
- Adicionar menu ativo dinâmico
- Configurar arquivos estáticos do admin"
```

#### **Opção B: Commits Atômicos (PROFISSIONAL)** ⭐

Fazer commits pequenos e focados:

```bash
# Commit 1: Views
git add pages/views.py
git commit -m "feat(eventos): adicionar views de inscrição

- EventoDetailView
- InscreverEventoView
- CancelarInscricaoView
- MinhasInscricoesView
- PerfilView"

# Commit 2: Templates
git add pages/templates/pages/evento_detail.html
git add pages/templates/pages/minhas_inscricoes.html
git add pages/templates/pages/perfil.html
git commit -m "feat(eventos): criar templates de eventos e perfil

- Template de detalhes do evento
- Template de minhas inscrições
- Template de perfil do aluno"

# Commit 3: URLs
git add pages/urls.py
git commit -m "feat(eventos): configurar rotas de eventos

- /evento/<id>/
- /evento/<id>/inscrever/
- /evento/<id>/cancelar/
- /perfil/
- /minhas-inscricoes/"

# Commit 4: Correção de logout
git add pages/templates/pages/index.html
git add pages/templates/pages/noticia.html
git commit -m "fix(auth): corrigir método de logout para POST

Alterar links de logout para formulários POST
para evitar erro HTTP 405."

# Commit 5: Menu ativo
git add static/js/mobile-menu.js
git add pages/templates/pages/evento_detail.html
git commit -m "feat(ui): adicionar menu ativo dinâmico

JavaScript detecta URL atual e marca menu correto."

# Commit 6: Admin
git add core/settings.py
git commit -m "fix(admin): configurar STATIC_ROOT para arquivos estáticos

Adicionar STATIC_ROOT para Django Admin funcionar corretamente."

# Commit 7: Documentação
git add DIAGRAMAS_UML.md
git add RELATORIO_PROGRESSO.md
git add IMPLEMENTACAO_FASE1.md
git commit -m "docs: atualizar documentação do projeto

- Adicionar 7 diagramas UML completos
- Atualizar relatório de progresso (95%)
- Documentar implementação da Fase 1"
```

### 4.3 Verificar Commits

```bash
# Ver histórico de commits
git log --oneline

# Ver último commit com detalhes
git show

# Ver commits de forma gráfica
git log --graph --oneline --all
```

---

## 5. SINCRONIZAR COM REMOTO

### 5.1 Primeira Vez: Criar Branch no GitHub

```bash
# Enviar branch para GitHub pela primeira vez
git push -u origin feature/sistema-inscricao-eventos
```

**Saída esperada:**
```
Enumerating objects: 45, done.
Counting objects: 100% (45/45), done.
Delta compression using up to 8 threads
Compressing objects: 100% (30/30), done.
Writing objects: 100% (30/30), 15.23 KiB | 1.52 MiB/s, done.
Total 30 (delta 20), reused 0 (delta 0)
remote: Resolving deltas: 100% (20/20), completed with 10 local objects.
To github.com:SEU_USUARIO/Portal_NoticiasIPM.git
 * [new branch]      feature/sistema-inscricao-eventos -> feature/sistema-inscricao-eventos
Branch 'feature/sistema-inscricao-eventos' set up to track remote branch 'feature/sistema-inscricao-eventos' from 'origin'.
```

**✅ Branch criada no GitHub!**

### 5.2 Pushes Subsequentes

```bash
# Depois do primeiro push, basta:
git push
```

### 5.3 Se Houver Novos Commits na Main

```bash
# Atualizar sua branch com mudanças da main
git checkout main
git pull origin main

git checkout feature/sistema-inscricao-eventos
git merge main

# Se houver conflitos, resolve e depois:
git add .
git commit -m "merge: resolver conflitos com main"
git push
```

---

## 6. CRIAR PULL REQUEST

### 6.1 Via GitHub Web (RECOMENDADO)

#### Passo 1: Acessar GitHub
1. Abre: `https://github.com/SEU_USUARIO/Portal_NoticiasIPM`
2. Verás banner amarelo:
   ```
   feature/sistema-inscricao-eventos had recent pushes
   [Compare & pull request]
   ```

#### Passo 2: Clicar "Compare & pull request"

#### Passo 3: Preencher Formulário do PR

**Título (Formato Profissional):**
```
✨ Feature: Sistema de Inscrição em Eventos e Perfil do Aluno
```

**Descrição (Template Profissional):**
```markdown
## 📋 Resumo

Implementação completa do sistema de inscrição em eventos e perfil do aluno.

## 🎯 Objetivo

Permitir que alunos se inscrevam em eventos institucionais, gerenciem suas inscrições e visualizem seu perfil.

## ✅ Funcionalidades Implementadas

### Sistema de Inscrição em Eventos
- [x] Página de detalhes do evento com informações completas
- [x] Botão de inscrição com validação de vagas
- [x] Cancelamento de inscrição
- [x] Verificação de inscrições duplicadas
- [x] Mensagens de feedback em português
- [x] Estados visuais (disponível/esgotado/inscrito)

### Perfil do Aluno
- [x] Página de perfil com informações pessoais
- [x] Foto de perfil (ou iniciais)
- [x] Estatísticas de eventos (futuros e participados)
- [x] Histórico de participação

### Minhas Inscrições
- [x] Lista de todos os eventos inscritos
- [x] Cards com informações do evento
- [x] Botões de ação (ver detalhes, cancelar)
- [x] Mensagem quando não há inscrições

### Melhorias Gerais
- [x] Correção do logout (método POST)
- [x] Menu ativo dinâmico baseado na URL
- [x] Configuração de arquivos estáticos do admin
- [x] Design moderno e responsivo

## 🗂️ Arquivos Modificados

### Novos Arquivos
- `pages/templates/pages/evento_detail.html`
- `pages/templates/pages/minhas_inscricoes.html`
- `pages/templates/pages/perfil.html`
- `DIAGRAMAS_UML.md`
- `IMPLEMENTACAO_FASE1.md`
- `GUIA_PULL_REQUEST.md`

### Arquivos Modificados
- `pages/views.py` - 5 novas views
- `pages/urls.py` - 5 novas rotas
- `pages/templates/pages/index.html` - Logout POST
- `pages/templates/pages/noticia.html` - Logout POST
- `pages/templates/pages/eventos.html` - Link para detalhes
- `static/js/mobile-menu.js` - Menu ativo dinâmico
- `core/settings.py` - STATIC_ROOT
- `RELATORIO_PROGRESSO.md` - Atualizado para 95%

## 📊 Impacto

### Antes
- Progresso: 85%
- Eventos: Apenas listagem
- Perfil: Não implementado
- Inscrições: Não funcional

### Depois
- Progresso: 95%
- Eventos: Sistema completo de inscrição
- Perfil: Página completa com histórico
- Inscrições: Totalmente funcional

## 🧪 Testes Realizados

- [x] Inscrição em evento com vagas
- [x] Tentativa de inscrição sem vagas
- [x] Inscrição duplicada (bloqueada)
- [x] Cancelamento de inscrição
- [x] Visualização de perfil
- [x] Listagem de inscrições
- [x] Logout com POST
- [x] Menu ativo em todas as páginas
- [x] Admin panel com estilos

## 🔗 Issues Relacionadas

Closes #XX (se houver)

## 📸 Screenshots

(Adicionar se possível)

## ✅ Checklist de Qualidade

- [x] Código testado localmente
- [x] Sem erros no console
- [x] Sem warnings do Django
- [x] Documentação atualizada
- [x] Commits bem organizados
- [x] Mensagens de commit descritivas
- [x] Branch atualizada com main
- [x] Código segue padrões do projeto

## 👥 Reviewers

@membro1 @membro2 @membro3

## 📝 Notas Adicionais

- Sistema pronto para produção
- Faltam apenas funcionalidades opcionais (busca, edição de perfil)
- Design moderno e profissional implementado

---

**Desenvolvido por:** Grupo Número 6  
**Data:** 04/02/2026  
**Tempo de desenvolvimento:** ~8 horas
```

#### Passo 4: Configurações do PR

- **Reviewers**: Seleciona membros do grupo
- **Assignees**: Atribui a ti mesmo
- **Labels**: `feature`, `enhancement`
- **Projects**: Adiciona ao projeto (se houver)
- **Milestone**: Adiciona ao milestone (se houver)

#### Passo 5: Criar PR

Clica em **"Create pull request"** 🎉

### 6.2 Via GitHub CLI (Alternativo)

```bash
# Instalar GitHub CLI (se não tiver)
# Windows: winget install GitHub.cli

# Fazer login
gh auth login

# Criar PR
gh pr create \
  --title "✨ Feature: Sistema de Inscrição em Eventos e Perfil do Aluno" \
  --body-file .github/PULL_REQUEST_TEMPLATE.md \
  --reviewer membro1,membro2 \
  --label feature,enhancement
```

---

## 7. CODE REVIEW

### 7.1 Aguardar Review

**O que acontece:**
1. Reviewers recebem notificação
2. Analisam o código
3. Deixam comentários
4. Aprovam ou solicitam mudanças

### 7.2 Responder a Comentários

**Se houver solicitação de mudanças:**

```bash
# Fazer as alterações solicitadas
# Editar arquivos conforme feedback

# Adicionar e commitar
git add .
git commit -m "refactor: aplicar sugestões do code review

- Melhorar validação de vagas
- Adicionar tratamento de erro
- Corrigir indentação"

# Enviar para GitHub
git push

# O PR é atualizado automaticamente!
```

### 7.3 Aprovar PR

**Quando aprovado:**
- ✅ Pelo menos 1 aprovação (depende das regras do repo)
- ✅ Todos os checks passaram (CI/CD se houver)
- ✅ Sem conflitos com a main

---

## 8. MERGE E FINALIZAÇÃO

### 8.1 Fazer Merge

**No GitHub, tens 3 opções:**

#### **Opção 1: Merge Commit** (Padrão)
```
Mantém todo o histórico de commits
Cria um commit de merge
Histórico completo preservado
```

#### **Opção 2: Squash and Merge** (Recomendado para muitos commits)
```
Combina todos os commits em um único
Histórico mais limpo
Perde detalhes dos commits individuais
```

#### **Opção 3: Rebase and Merge** (Avançado)
```
Reaplica commits na base
Histórico linear
Sem commit de merge
```

**Escolhe e clica em "Confirm merge"** ✅

### 8.2 Deletar Branch Remota

No GitHub, após o merge:
- Clica em "Delete branch"

### 8.3 Limpar Localmente

```bash
# Voltar para main
git checkout main

# Atualizar main com o merge
git pull origin main

# Deletar branch local
git branch -d feature/sistema-inscricao-eventos

# Verificar branches
git branch
# Deve mostrar apenas: * main
```

### 8.4 Verificar Merge

```bash
# Ver últimos commits na main
git log --oneline -5

# Deve incluir o merge do PR
```

---

## 🎯 WORKFLOW COMPLETO (RESUMO)

```bash
# 1. PREPARAÇÃO
git checkout main
git pull origin main

# 2. CRIAR BRANCH
git checkout -b feature/nome-da-funcionalidade

# 3. DESENVOLVER
# ... fazer alterações no código ...

# 4. COMMITS
git add .
git commit -m "feat(escopo): descrição clara"

# 5. PUSH
git push -u origin feature/nome-da-funcionalidade

# 6. CRIAR PR (no GitHub)
# ... preencher formulário ...

# 7. CODE REVIEW
# ... aguardar aprovação ...

# 8. MERGE (no GitHub)
# ... fazer merge ...

# 9. LIMPAR
git checkout main
git pull origin main
git branch -d feature/nome-da-funcionalidade
```

---

## 📚 RECURSOS ADICIONAIS

### Comandos Git Úteis

```bash
# Ver diferenças antes de commitar
git diff

# Desfazer último commit (mantém alterações)
git reset --soft HEAD~1

# Desfazer último commit (descarta alterações)
git reset --hard HEAD~1

# Ver histórico de um arquivo
git log --follow arquivo.py

# Buscar em commits
git log --grep="palavra-chave"

# Ver quem modificou cada linha
git blame arquivo.py

# Criar tag de versão
git tag -a v1.0.0 -m "Versão 1.0.0"
git push origin v1.0.0
```

### Boas Práticas

✅ **FAZER:**
- Commits pequenos e focados
- Mensagens descritivas
- Testar antes de commitar
- Atualizar branch com main regularmente
- Responder a code reviews rapidamente

❌ **NÃO FAZER:**
- Commits gigantes com muitas mudanças
- Mensagens vagas ("fix", "update")
- Commitar código que não funciona
- Ignorar conflitos
- Fazer force push em branches compartilhadas

---

## 🆘 PROBLEMAS COMUNS E SOLUÇÕES

### Problema 1: "fatal: not a git repository"
```bash
# Solução: Inicializar repositório
git init
```

### Problema 2: Conflitos de Merge
```bash
# Solução: Resolver manualmente
git status  # Ver arquivos em conflito
# Editar arquivos, remover marcadores <<<< ==== >>>>
git add .
git commit -m "merge: resolver conflitos"
```

### Problema 3: Commit Errado
```bash
# Solução: Desfazer último commit
git reset --soft HEAD~1
# Fazer correções
git add .
git commit -m "mensagem correta"
```

### Problema 4: Push Rejeitado
```bash
# Solução: Atualizar branch primeiro
git pull origin feature/sua-branch
# Resolver conflitos se houver
git push
```

### Problema 5: Esqueci de Criar Branch
```bash
# Solução: Criar branch agora
git checkout -b feature/nome-correto
# Commits vão para a nova branch
```

---

**Criado em:** 04/02/2026 01:18  
**Autor:** Grupo Número 6  
**Versão:** 1.0
