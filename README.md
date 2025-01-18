# 🤖 AutoCommit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

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

- 🎯 Geração automática de mensagens de commit significativas
- 🔄 Integração contínua com seu fluxo de trabalho
- 🛡️ Configuração segura através de variáveis de ambiente
- 📊 Análise inteligente de alterações no código
- 🌐 Suporte multilíngue

## 🚀 Como Começar

### Pré-requisitos

- Python 3.8 ou superior
- Git instalado em sua máquina
- API Key do Google Gemini (gratuita)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/autocommit.git
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
     ```
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

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

Aceito sugestões de melhorias! Se você tem uma ideia para tornar este projeto melhor, não hesite em:
- Abrir uma [Issue](https://github.com/glira/autocommit/issues)
- Enviar um Pull Request
- Entrar em contato diretamente comigo

Toda contribuição é valiosa, seja ela:
- Correção de bugs
- Novas funcionalidades
- Melhorias na documentação
- Sugestões de recursos
- Otimizações de código

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📬 Contato


Link do Projeto: [https://github.com/glira/autocommit](https://github.com/glira/autocommit)

---

⭐️ Se este projeto te ajudou, considere dar uma estrela!
