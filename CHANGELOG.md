# 📝 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.1.0] - 2024-XX-XX

### ✨ Adicionado
- Sistema de versionamento automático seguindo Semantic Versioning (SemVer)
- Arquivo `VERSION` para controle de versão do projeto
- Função de análise inteligente de alterações para determinar tipo de incremento (MAJOR, MINOR, PATCH)
- Sistema de rollback automático que restaura versão anterior em caso de erro ou cancelamento
- Variável de ambiente `ENABLE_VERSIONING` para habilitar/desabilitar versionamento
- Integração automática da versão nas mensagens de commit
- Documentação completa sobre versionamento no README.md
- Arquivo CONTRIBUTING.md com guia de contribuição
- Seção de FAQ no README.md
- Melhorias gerais na documentação

### 🔄 Modificado
- README.md atualizado com informações sobre versionamento
- Melhorias na estrutura de documentação do projeto

### 🛡️ Melhorias de Segurança
- Sistema de rollback protege contra perda de versão em caso de erros
- Validação aprimorada de versões

## [1.0.0] - Data Inicial

### ✨ Adicionado
- Geração automática de mensagens de commit usando Google Gemini API
- Suporte a múltiplos modelos do Gemini (gemini-2.0-flash, gemini-1.5-flash, gemini-1.5-pro)
- Verificação automática de variáveis de ambiente
- Inicialização automática de repositórios Git quando necessário
- Detecção inteligente de alterações no código
- Suporte multilíngue (português e outros idiomas)
- Configuração segura através de arquivo .env
- Mensagens de erro e feedback claros ao usuário
- Confirmação do usuário antes de criar commits
- Documentação inicial (README.md)

---

## Tipos de Mudanças

- **✨ Adicionado** - para novas funcionalidades
- **🔄 Modificado** - para mudanças em funcionalidades existentes
- **🗑️ Removido** - para funcionalidades removidas
- **🐛 Corrigido** - para correções de bugs
- **🛡️ Melhorias de Segurança** - para melhorias de segurança
- **⚡ Performance** - para melhorias de performance
- **📚 Documentação** - para mudanças na documentação

---

**Nota**: Este changelog começou a ser mantido a partir da versão 1.1.0. Versões anteriores podem não estar completamente documentadas.

