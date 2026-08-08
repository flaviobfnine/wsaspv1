# Diretrizes e Contexto do Projeto

## 👥 Cliente Ideal / Avatares (Bfnine Camisetas)
Sempre que criar páginas de vendas (landing pages), roteiros de anúncios, copys, campanhas ou qualquer conteúdo de marketing para este projeto, você **DEVE obrigatoriamente** ler e seguir as definições de público-alvo e avatares presentes no arquivo:
- [clilente_Ideal_bfnine.md](file:///d:/BACKUP_ARQUIVOS/SITES/ASIMOV/SITES/SITE%202/clilente_Ideal_bfnine.md)

## 🛠️ Orquestração de Habilidades (Fluxo Integrado)
Para garantir o melhor resultado e evitar erros, trabalhe sempre combinando as habilidades (`skills`) do projeto no seguinte fluxo:

### 🚀 Gatilhos de Automação de Fluxos

1. **Para Criar um Novo Projeto de Página de Vendas:**
   - **Gatilho:** Quando o usuário digitar **"Novo Projeto"**, **"Nova Página"**, **"Nova LP"** ou similar.
   - **Ação:** Verifique se o arquivo de briefing gerado pelo cliente (salvo como `briefing.md` ou similar) está na pasta de trabalho do cliente. Se o arquivo estiver presente, leia-o diretamente para obter as informações e pule para o **Passo 2**. Caso contrário, execute o **Passo 1** fazendo as perguntas no chat de forma contínua.

2. **Para Limpar e Organizar uma Página HTML Existente:**
   - **Gatilho:** Quando o usuário enviar um arquivo HTML e digitar **"Limpar HTML"**, **"Organizar página"**, **"Extrair Design System"** ou similar.
   - **Ação:** Execute detalhadamente os passos do arquivo [Extract HTML Design System v3.md](file:///d:/BACKUP_ARQUIVOS/SITES/ASIMOV/SITES/SITE%202/Extract%20HTML%20Design%20System%20v3.md) para analisar o arquivo, extrair o CSS e JS inline para arquivos na pasta `assets/`, classificar os SVGs, reescrever a página principal limpa e traduzida (PT-BR) e gerar o `STACK.md`.

---

### 📋 Passos do Fluxo de Criação de Páginas:

1. **Passo 1: Planejamento / Leitura de Briefing**
   - O agente deve sempre buscar o arquivo `briefing.md` no diretório de trabalho. Se encontrado, deve realizar a leitura automática e extração de dados (avatar, produto, metas) sem intervenção manual. Se o arquivo não for encontrado, o agente deve notificar o usuário e solicitar a criação do arquivo ou guiar o usuário na definição do escopo.
2. **Passo 2: Copywriting e Criação (`landing-page-generator`)**
   - Use o gerador de landing pages para estruturar as seções (Hero, Features, Pricing, etc.).
   - Adapte os textos usando um framework de copy persuasivo (PAS, AIDA ou BAB) e use o tom de voz correto baseado no público-alvo escolhido do arquivo `clilente_Ideal_bfnine.md`.
3. **Passo 3: Otimização e Lançamento (`frontend-seo`)**
   - Aplique as regras de SEO técnico e as tags de compartilhamento social nas páginas criadas, garantindo que o carregamento seja rápido e o site apareça bem no Google.
4. **Passo 4: Criação do Carrossel de Apoio (Skills de Carrossel)**
   - **IMPORTANTE:** O carrossel **só** poderá ser criado após a página de vendas correspondente estar 100% concluída e mediante a autorização ou solicitação explícita do usuário.
   - Deve ser criado **um carrossel específico para cada versão de página**, ou seja, um carrossel sob medida para cada público/avatar de cada página.
   - Use os textos e argumentos de vendas da própria versão da página finalizada, seguindo as regras de hooks, copy e prompts das skills de carrossel.

## ✍️ Regras de Escrita e Tom de Voz
- Adapte a linguagem de acordo com o público-alvo selecionado (Públicos 1, 2, 3 ou 4) conforme detalhado no mapa de avatares.
- A linguagem deve ser persuasiva, focada em conversão, com ganchos fortes de comunicação e quebra de objeções baseadas nos dados fornecidos no arquivo.
- Mantenha a resposta em português brasileiro, simples, direta e de fácil compreensão.

## 🛑 Regras Críticas de Execução e Qualidade (OBRIGATÓRIO)
1. **Testes Rigorosos Antes de Entregar:** NUNCA peça ao usuário para conferir ou testar qualquer resultado sem antes ter testado e auditado minuciosamente a integridade do código HTML, CSS e JS (garantindo 100% que não existem tags abertas, textos de código vazando no DOM ou layouts quebrados).
2. **Respeito Estrito ao Escopo Solicitado:** NUNCA altere o layout, estrutura, estilos ou funcionalidades da página além daquilo que foi explicitamente solicitado pelo usuário no chat. Preserve intacto tudo o que não foi pedido para mudar.
3. **Autorização Obrigatória para Commits:** REGRA INVIOLÁVEL: Qualquer commit ou push para o GitHub neste projeto (incluindo repositórios como `wsp3`, `wsaspv1` e outros) SÓ pode ser realizado quando houver autorização ou solicitação explícita do usuário no chat.
4. **Alteração de Eventos de Conversão / Tracking:** REGRA INVIOLÁVEL: NUNCA alterar, adicionar ou remover scripts de eventos de conversão, pixels ou rastreamento sem solicitação explícita do usuário no chat.

