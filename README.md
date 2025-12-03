# 🤖 AutoCommit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-success.svg)](https://opensource.org/)

Uma ferramenta automatizada para gerar mensagens de commit inteligentes usando IA e gerenciar versionamento automático de projetos.

## 📑 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologia](#-tecnologia)
- [Principais Características](#-principais-características)
- [Como Começar](#-como-começar)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
- [Como Usar](#-como-usar)
- [Versionamento Automático](#-versionamento-automático)
- [Vantagens de Uso](#-vantagens-de-uso)
- [Perguntas Frequentes](#-perguntas-frequentes-faq)
- [Contribuindo](#-contribuindo)
- [Documentação Adicional](#-documentação-adicional)
- [Licença](#-licença)

## 📋 Sobre o Projeto

AutoCommit é uma ferramenta automatizada que simplifica o processo de gerenciamento de commits em seus projetos. Nasceu da necessidade de poupar tempo na criação de mensagens de commit detalhadas e significativas, eliminando a tarefa repetitiva de escrever descritivos elaborados manualmente.

A inspiração veio da necessidade diária de manter um histórico de alterações claro e profissional, sem comprometer tempo valioso do desenvolvimento. Com o AutoCommit, você obtém mensagens de commit descritivas e bem estruturadas em segundos, mantendo a qualidade da documentação do seu código.

### 🎥 Demonstração

<img src="https://raw.githubusercontent.com/glira/autocommit/main/example.gif" alt="Demonstração do AutoCommit" width="1280">

### 🤖 Tecnologia

O AutoCommit utiliza o Google Gemini, um poderoso modelo de linguagem da Google, para gerar mensagens de commit inteligentes. Algumas vantagens de usar o Gemini incluem:

- 🆓 **Gratuito para Usar**: O Google Gemini oferece uma generosa cota gratuita
- 🚀 **Rápido e Eficiente**: Respostas quase instantâneas
- 🎯 **Alta Precisão**: Gera mensagens de commit contextualizadas e relevantes
- 🌐 **Fácil Integração**: API simples e bem documentada

## ✨ Principais Características

- 🎯 **Geração automática de mensagens de commit** significativas usando IA
- 📦 **Versionamento automático** seguindo Semantic Versioning (SemVer)
- 🔄 **Integração contínua** com seu fluxo de trabalho Git
- 🛡️ **Configuração segura** através de variáveis de ambiente
- 📊 **Análise inteligente** de alterações no código
- ↩️ **Sistema de rollback** que restaura versões em caso de erro
- 🌐 **Suporte multilíngue** (português e outros idiomas)
- 🚀 **Inicialização automática** de repositórios Git quando necessário

## 🚀 Como Começar

### Pré-requisitos

- Python 3.8 ou superior
- Git instalado em sua máquina
- API Key do Google Gemini (gratuita)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/glira/autocommit.git
cd autocommit
```

2. Instale as dependências:
```bash
pip install requests python-dotenv
```

3. Configure suas credenciais:
   - Copie o arquivo de exemplo para criar seu arquivo de configuração:
     ```bash
     cp .env.example .env
     ```
   - Edite o arquivo `.env` com suas informações:
     ```env
     API_KEY=sua_api_key_do_gemini_aqui
     GIT_USER_NAME=seu_nome_para_commits
     GIT_USER_EMAIL=seu_email_para_commits
     ENABLE_VERSIONING=true
     ```
   - **Configurações disponíveis:**
     - `API_KEY`: Sua chave da API do Google Gemini (obrigatório)
     - `GIT_USER_NAME`: Nome que aparecerá nos commits (obrigatório)
     - `GIT_USER_EMAIL`: Email que aparecerá nos commits (obrigatório)
     - `ENABLE_VERSIONING`: Habilita/desabilita versionamento automático (`true` ou `false`, padrão: `false`)
   - Obtenha sua API key gratuita em: https://makersuite.google.com/app/apikey

## 🛠️ Como Usar

```bash
python autocommit.py
```

### Dica de Produtividade 🚀

Para tornar o uso ainda mais prático, você pode criar um alias no seu sistema. Adicione a seguinte linha ao seu arquivo `~/.bashrc` ou `~/.zshrc`:

```bash
alias autocommit="python /caminho/para/seu/autocommit.py"
```

Por exemplo:
```bash
alias autocommit="python /home/glira/projetos/autocommit/autocommit.py"
```

Após adicionar o alias, recarregue seu arquivo de configuração:
```bash
source ~/.bashrc  # ou source ~/.zshrc
```

Agora você pode simplesmente digitar `autocommit` em qualquer diretório git para usar a ferramenta!

## 📦 Versionamento Automático

O AutoCommit inclui um sistema inteligente de versionamento automático que segue o padrão [Semantic Versioning](https://semver.org/) (SemVer).

### Como Funciona

1. **Análise Inteligente**: O sistema analisa suas alterações usando IA para determinar o tipo de mudança
2. **Incremento Automático**: A versão é incrementada automaticamente no arquivo `VERSION`:
   - **MAJOR** (x.0.0): Mudanças incompatíveis que quebram a API
   - **MINOR** (x.y.0): Novas funcionalidades compatíveis
   - **PATCH** (x.y.z): Correções de bugs e pequenas alterações
3. **Integração no Commit**: A versão é incluída automaticamente na mensagem do commit
4. **Sistema de Rollback**: Se algo der errado, a versão anterior é restaurada automaticamente

### Habilitando o Versionamento

No arquivo `.env`, configure:

```env
ENABLE_VERSIONING=true
```

Para desabilitar:

```env
ENABLE_VERSIONING=false
```

### Arquivo VERSION

O projeto mantém um arquivo `VERSION` na raiz do projeto com a versão atual no formato `MAJOR.MINOR.PATCH` (ex: `1.0.0`).

**Nota**: Se o arquivo `VERSION` não existir, ele será criado automaticamente com a versão inicial `1.0.0`.

### Exemplo de Uso

```bash
# Com versionamento habilitado
📦 Versão atual: 1.0.0
🔄 Analisando tipo de alteração para versionamento...
📈 Incremento MINOR: 1.0.0 → 1.1.0

# A mensagem do commit incluirá a versão:
# "Adiciona nova funcionalidade (v1.1.0)"
```

### Proteção Contra Erros

O sistema possui proteção automática:
- ✅ Se você cancelar o commit, a versão é restaurada
- ✅ Se houver erro no commit, a versão é restaurada
- ✅ Se você interromper o processo (Ctrl+C), a versão é restaurada

A versão só é mantida se o commit for bem-sucedido!

## 🌟 Vantagens de Uso

1. **Produtividade Aumentada**
   - Economize tempo automatizando a criação de mensagens de commit
   - Mantenha um padrão consistente em seus commits

2. **Melhor Organização**
   - Histórico de versão mais limpo e profissional
   - Facilita a revisão de código e colaboração em equipe

3. **Segurança**
   - Credenciais protegidas através de variáveis de ambiente
   - Sem exposição de dados sensíveis no código

4. **Flexibilidade**
   - Personalizável de acordo com suas necessidades
   - Fácil integração com diferentes projetos

## ❓ Perguntas Frequentes (FAQ)

### Como desabilitar o versionamento automático?

Simplesmente configure `ENABLE_VERSIONING=false` no arquivo `.env`. O AutoCommit continuará funcionando normalmente para gerar mensagens de commit, mas não atualizará o arquivo VERSION.

### Posso usar o AutoCommit sem API Key do Gemini?

Não, a API Key é obrigatória para o funcionamento do AutoCommit, pois é usada para gerar as mensagens de commit inteligentes.

### O que acontece se eu cancelar o commit após a versão ser atualizada?

O sistema automaticamente restaura a versão anterior. Não há necessidade de fazer nada manualmente - a proteção é automática!

### Posso usar em projetos que já têm versionamento?

Sim! Se você já tem um sistema de versionamento, você pode:
- Desabilitar o versionamento do AutoCommit (`ENABLE_VERSIONING=false`)
- Ou manter ambos (o arquivo VERSION do AutoCommit será independente)

### O AutoCommit funciona com qualquer linguagem de programação?

Sim! O AutoCommit analisa as alterações no código independentemente da linguagem, usando IA para entender o contexto das mudanças.

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

Veja nosso [Guia de Contribuição](CONTRIBUTING.md) para mais detalhes sobre como contribuir!

Aceito sugestões de melhorias! Se você tem uma ideia para tornar este projeto melhor, não hesite em:
- Abrir uma [Issue](https://github.com/glira/autocommit/issues)
- Enviar um Pull Request
- Entrar em contato diretamente

Toda contribuição é valiosa, seja ela:
- 🐛 Correção de bugs
- ✨ Novas funcionalidades
- 📚 Melhorias na documentação
- 💡 Sugestões de recursos
- ⚡ Otimizações de código
- 🌐 Traduções

## 📚 Documentação Adicional

- [Guia de Contribuição](CONTRIBUTING.md) - Saiba como contribuir com o projeto
- [Changelog](CHANGELOG.md) - Histórico de mudanças e versões

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🗺️ Roadmap

Funcionalidades planejadas para futuras versões:

- [ ] Suporte para múltiplos formatos de mensagem de commit (Conventional Commits, etc.)
- [ ] Integração com hooks do Git (pre-commit, post-commit)
- [ ] Modo não-interativo para CI/CD
- [ ] Suporte para múltiplas APIs de IA (OpenAI, Claude, etc.)
- [ ] Interface web opcional
- [ ] Histórico de versões no arquivo CHANGELOG.md automático
- [ ] Suporte para tags Git automáticas baseadas na versão

## 📬 Contato

Link do Projeto: [https://github.com/glira/autocommit](https://github.com/glira/autocommit)

---

⭐️ **Se este projeto te ajudou, considere dar uma estrela!**

💬 **Encontrou um bug ou tem uma sugestão?** [Abra uma issue](https://github.com/glira/autocommit/issues)!
