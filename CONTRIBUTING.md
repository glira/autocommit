# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com o AutoCommit! Este documento fornece diretrizes para contribuir com o projeto.

## 📋 Como Contribuir

### Reportando Bugs

Se você encontrou um bug, por favor:

1. Verifique se o bug já não foi reportado nas [Issues](https://github.com/glira/autocommit/issues)
2. Se não foi reportado, abra uma nova issue com:
   - Descrição clara do problema
   - Passos para reproduzir o bug
   - Comportamento esperado vs. comportamento atual
   - Versão do Python e sistema operacional
   - Logs de erro (se houver)

### Sugerindo Melhorias

Tem uma ideia para melhorar o projeto? Adoraríamos ouvir!

1. Verifique se a sugestão já não existe nas [Issues](https://github.com/glira/autocommit/issues)
2. Abra uma nova issue com:
   - Descrição detalhada da funcionalidade
   - Casos de uso e exemplos
   - Benefícios para os usuários

### Enviando Pull Requests

1. **Fork o repositório**

2. **Clone seu fork**:
   ```bash
   git clone https://github.com/SEU_USUARIO/autocommit.git
   cd autocommit
   ```

3. **Crie uma branch para sua feature**:
   ```bash
   git checkout -b feature/minha-feature
   # ou
   git checkout -b fix/correcao-bug
   ```

4. **Faça suas alterações**:
   - Siga o estilo de código existente
   - Adicione comentários quando necessário
   - Teste suas alterações

5. **Commit suas mudanças**:
   ```bash
   git commit -m "feat: adiciona nova funcionalidade"
   ```
   
   Use mensagens de commit descritivas. Prefixos recomendados:
   - `feat:` para novas funcionalidades
   - `fix:` para correções de bugs
   - `docs:` para documentação
   - `style:` para formatação
   - `refactor:` para refatoração
   - `test:` para testes
   - `chore:` para tarefas de manutenção

6. **Push para sua branch**:
   ```bash
   git push origin feature/minha-feature
   ```

7. **Abra um Pull Request** no repositório original

## 📝 Padrões de Código

### Python

- Use Python 3.8+
- Siga o PEP 8 para estilo de código
- Use type hints quando apropriado
- Mantenha funções pequenas e focadas
- Adicione docstrings para funções e classes

### Estrutura de Arquivos

- Mantenha o código organizado e modular
- Adicione comentários explicativos quando necessário
- Use nomes descritivos para variáveis e funções

### Tratamento de Erros

- Use try/except apropriadamente
- Forneça mensagens de erro claras e úteis
- Considere casos extremos e erros de entrada

## 🧪 Testando

Antes de enviar um Pull Request:

1. Teste suas alterações manualmente
2. Verifique se não quebrou funcionalidades existentes
3. Teste em diferentes cenários:
   - Com e sem repositório Git
   - Com versionamento habilitado/desabilitado
   - Com diferentes tipos de alterações

## 📚 Documentação

Se você adicionar novas funcionalidades:

- Atualize o README.md se necessário
- Adicione exemplos de uso
- Documente novas configurações no .env.example
- Atualize o CHANGELOG.md

## 🔍 Processo de Review

1. Aguarde feedback nos Pull Requests
2. Esteja aberto a sugestões e mudanças
3. Responda a comentários e faça ajustes se necessário
4. Mantenha discussões construtivas e respeitosas

## 💡 Áreas que Precisam de Ajuda

Sempre estamos procurando ajuda em:

- 🐛 Correção de bugs
- ✨ Novas funcionalidades
- 📖 Melhorias na documentação
- 🌐 Traduções
- ⚡ Otimizações de performance
- 🧪 Testes automatizados
- 🎨 Melhorias na interface do usuário (mensagens, output)

## 📞 Dúvidas?

Se tiver dúvidas sobre como contribuir:

- Abra uma issue para discussão
- Verifique as issues existentes
- Entre em contato através do GitHub

## 📜 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a mesma licença MIT do projeto.

---

Obrigado por tornar o AutoCommit melhor! 🙏

