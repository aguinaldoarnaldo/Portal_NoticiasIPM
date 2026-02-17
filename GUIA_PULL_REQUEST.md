# 🔀 GUIA: CRIAR PULL REQUEST

## Status Atual
✅ Branch: `LoginPage`  
✅ Push: Completo  
✅ Commits: Sincronizados com GitHub

---

## 📝 PASSOS PARA CRIAR PULL REQUEST

### **Método 1: Via GitHub Web (Recomendado)**

#### 1️⃣ Aceder ao Repositório
1. Abre o navegador
2. Vai para: `https://github.com/SEU_USUARIO/Portal_NoticiasIPM`
3. Faz login (se necessário)

#### 2️⃣ Criar Pull Request
1. Verás um banner amarelo dizendo:
   ```
   LoginPage had recent pushes X minutes ago
   [Compare & pull request]
   ```
2. Clica no botão **"Compare & pull request"**

   **OU**

3. Clica na aba **"Pull requests"**
4. Clica no botão verde **"New pull request"**
5. Seleciona:
   - **Base**: `main` (ou `master`)
   - **Compare**: `LoginPage`

#### 3️⃣ Preencher Informações do PR

**Título sugerido:**
```
✨ Feature: Sistema de Inscrição em Eventos e Perfil do Aluno
```

**Descrição sugerida:**
```markdown
## 📋 Resumo das Alterações

Esta PR adiciona funcionalidades essenciais ao Portal de Notícias IPM:

### ✅ Funcionalidades Implementadas

#### 1. Sistema de Inscrição em Eventos
- ✅ Página de detalhes do evento
- ✅ Inscrição em eventos com validação de vagas
- ✅ Cancelamento de inscrição
- ✅ Verificação de duplicatas
- ✅ Mensagens de feedback em português

#### 2. Perfil do Aluno
- ✅ Página de perfil completa
- ✅ Informações pessoais
- ✅ Estatísticas de eventos
- ✅ Histórico de participação

#### 3. Minhas Inscrições
- ✅ Lista de eventos inscritos
- ✅ Botões de ação (ver detalhes, cancelar)
- ✅ Estados visuais claros

#### 4. Melhorias Gerais
- ✅ Correção do logout (POST method)
- ✅ Menu ativo dinâmico (JavaScript)
- ✅ Arquivos estáticos do admin configurados
- ✅ Design moderno e responsivo

### 📊 Progresso do Projeto
- **Antes:** 85%
- **Agora:** 95%

### 🗂️ Arquivos Principais Modificados/Criados

**Templates:**
- `pages/templates/pages/evento_detail.html` (novo)
- `pages/templates/pages/minhas_inscricoes.html` (novo)
- `pages/templates/pages/perfil.html` (novo)
- `pages/templates/pages/index.html` (modificado)
- `pages/templates/pages/noticia.html` (modificado)
- `pages/templates/pages/eventos.html` (modificado)

**Views:**
- `pages/views.py` - Adicionadas 5 novas views:
  - `EventoDetailView`
  - `InscreverEventoView`
  - `CancelarInscricaoView`
  - `MinhasInscricoesView`
  - `PerfilView`

**URLs:**
- `pages/urls.py` - 5 novas rotas configuradas

**JavaScript:**
- `static/js/mobile-menu.js` - Menu ativo dinâmico

**Configurações:**
- `core/settings.py` - STATIC_ROOT adicionado

**Documentação:**
- `DIAGRAMAS_UML.md` (novo) - 7 diagramas completos
- `RELATORIO_PROGRESSO.md` (atualizado)
- `IMPLEMENTACAO_FASE1.md` (novo)

### 🧪 Testes Realizados
- ✅ Inscrição em evento
- ✅ Cancelamento de inscrição
- ✅ Validação de vagas
- ✅ Logout com POST
- ✅ Menu ativo
- ✅ Admin panel funcionando

### 📸 Screenshots
(Adicionar screenshots se tiveres)

### 🔗 Issues Relacionadas
Closes #X (se houver issue)

### ✅ Checklist
- [x] Código testado localmente
- [x] Sem erros no console
- [x] Documentação atualizada
- [x] Commits organizados
- [x] Branch atualizada com main

---

**Desenvolvido por:** Grupo Número 6  
**Data:** 04/02/2026
```

#### 4️⃣ Criar o PR
1. Revisa as informações
2. Clica em **"Create pull request"**
3. ✅ Pull Request criado!

---

### **Método 2: Via GitHub CLI (Alternativo)**

Se tiveres o GitHub CLI instalado:

```bash
gh pr create --title "✨ Feature: Sistema de Inscrição em Eventos" --body "Ver descrição completa no PR"
```

---

### **Método 3: Via Git Command (Não Recomendado)**

O Git não tem comando nativo para PR. Tens que usar a interface web do GitHub.

---

## 🎯 PRÓXIMOS PASSOS APÓS CRIAR O PR

### 1️⃣ Aguardar Review
- Outros membros do grupo podem revisar
- Podem deixar comentários
- Podem aprovar ou solicitar mudanças

### 2️⃣ Fazer Merge
Quando aprovado, tens 3 opções:

**a) Merge Commit** (Recomendado)
- Mantém todo o histórico
- Cria um commit de merge

**b) Squash and Merge**
- Combina todos os commits em um
- Histórico mais limpo

**c) Rebase and Merge**
- Reaplica commits na base
- Histórico linear

### 3️⃣ Deletar Branch (Opcional)
Após o merge, podes deletar a branch `LoginPage`:
```bash
git branch -d LoginPage
git push origin --delete LoginPage
```

---

## 📌 DICAS IMPORTANTES

### ✅ Boas Práticas
- Título claro e descritivo
- Descrição detalhada das mudanças
- Mencionar issues relacionadas
- Adicionar screenshots se possível
- Marcar reviewers

### ⚠️ Antes de Fazer Merge
- Resolver todos os conflitos
- Garantir que os testes passam
- Obter aprovação de pelo menos 1 reviewer
- Verificar que o código está funcionando

### 🔄 Se Houver Conflitos
```bash
# Atualizar branch main local
git checkout main
git pull origin main

# Voltar para sua branch
git checkout LoginPage

# Fazer merge da main
git merge main

# Resolver conflitos manualmente
# Depois:
git add .
git commit -m "Resolve merge conflicts"
git push origin LoginPage
```

---

## 🌐 LINKS ÚTEIS

- **GitHub Docs - Pull Requests**: https://docs.github.com/en/pull-requests
- **Como Escrever um Bom PR**: https://github.blog/2015-01-21-how-to-write-the-perfect-pull-request/
- **GitHub CLI**: https://cli.github.com/

---

## ❓ PROBLEMAS COMUNS

### "No changes to commit"
- Já fizeste push de tudo
- Verifica: `git status`

### "Conflicts"
- Alguém modificou os mesmos arquivos
- Resolve manualmente os conflitos

### "Branch protection rules"
- Repositório pode exigir reviews
- Contacta o administrador

---

**Criado em:** 04/02/2026 01:13  
**Última Atualização:** 04/02/2026 01:13
