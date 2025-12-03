#!/usr/bin/env python3
import os
import sys
import subprocess
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura as variáveis de ambiente
API_KEY = os.getenv('API_KEY', '').strip()  # Remove espaços e caracteres extras
GIT_USER_NAME = os.getenv('GIT_USER_NAME')
GIT_USER_EMAIL = os.getenv('GIT_USER_EMAIL')
ENABLE_VERSIONING = os.getenv('ENABLE_VERSIONING', 'false').strip().lower() == 'true'

def verificar_variaveis_ambiente():
    """Verifica se todas as variáveis de ambiente necessárias estão configuradas"""
    variaveis = {
        'API_KEY': API_KEY,
        'GIT_USER_NAME': GIT_USER_NAME,
        'GIT_USER_EMAIL': GIT_USER_EMAIL
    }
    
    faltando = [var for var, valor in variaveis.items() if not valor]
    
    if faltando:
        print("❌ As seguintes variáveis de ambiente não estão configuradas:")
        print("\n".join(f"- {var}" for var in faltando))
        print("\nPor favor, copie o arquivo .env.example para .env e configure suas variáveis.")
        return False
    return True

def verificar_repositorio():
    """Verifica se o diretório atual é um repositório Git"""
    current_dir = os.getcwd()
    print(f"📂 Diretório atual: {current_dir}")

    if not os.path.exists(os.path.join(current_dir, ".git")):
        resposta = input("❓ Não é um repositório Git. Deseja iniciar um projeto Git aqui? (s/n): ").strip().lower()
        if resposta == 's':
            try:
                nome_projeto = os.path.basename(current_dir)
                subprocess.run(["git", "init"], check=True)
                subprocess.run(["git", "config", "user.name", GIT_USER_NAME], check=True)
                subprocess.run(["git", "config", "user.email", GIT_USER_EMAIL], check=True)
                print(f"✅ Repositório Git iniciado com o nome do projeto: {nome_projeto}")
                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao inicializar repositório: {e}")
                return False
        print("❌ Operação cancelada.")
        return False
    return True

def obter_alteracoes():
    """Obtém as alterações pendentes no Git"""
    try:
        current_dir = os.getcwd()
        is_git_repo = os.path.exists(os.path.join(current_dir, ".git"))
        
        # Se não for um repositório git, mostra todo o conteúdo como novo
        if not is_git_repo:
            status = "\n".join(f"?? {f}" for f in os.listdir(current_dir) 
                             if not f.startswith('.') and not f.startswith('__'))
            if not status:
                print("ℹ️ Nenhum arquivo encontrado para commit.")
                return None
                
            print("📝 Arquivos detectados:")
            print(status)
            
            # Usa diff --no-index para mostrar todo o conteúdo como novo
            diff = subprocess.run(["git", "diff", "--no-index", "/dev/null", "."],
                                capture_output=True, text=True, stderr=subprocess.DEVNULL).stdout.strip()
            return diff
        
        # Se for um repositório git, verifica alterações
        status = subprocess.run(["git", "status", "--porcelain"], 
                              capture_output=True, text=True).stdout.strip()
        
        if not status:
            print("ℹ️ Nenhuma alteração detectada para commit.")
            return None
        
        print("📝 Alterações detectadas:")
        print(status)
        
        # Se houver arquivos não rastreados (??) no status
        if "??" in status:
            # Adiciona arquivos não rastreados ao index temporariamente
            subprocess.run(["git", "add", "-N", "."], check=True)
            diff = subprocess.run(["git", "diff"], 
                                capture_output=True, text=True).stdout.strip()
            # Reseta o index
            subprocess.run(["git", "reset"], check=True)
        else:
            # Caso contrário, usa diff normal
            diff = subprocess.run(["git", "diff"], 
                                capture_output=True, text=True).stdout.strip()
        
        if not diff:
            print("ℹ️ Nenhuma diferença detectada para gerar o descritivo.")
            return None
            
        return diff
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao obter alterações: {e}")
        return None

def gerar_mensagem_commit(diff_text):
    """Gera uma mensagem de commit usando a API do Gemini"""
    # Lista de modelos para tentar em ordem
    modelos = [
        'gemini-2.0-flash',  # Modelo mais recente (funcionando)
        'gemini-1.5-flash',  # Versão estável
        'gemini-1.5-pro',  # Versão pro
    ]
    
    prompt = (
        "Faça em portugues, gere uma mensagem de commit detalhada "
        "com base nas seguintes diferenças entre os arquivos. "
        "Sua primeira linha na resposta deve ser o título:\n"
        f"{diff_text}"
    )
    
    print("🔄 Tentando gerar mensagem com API do Gemini...")
    
    # Limpa a API_KEY para garantir que não tenha caracteres extras
    api_key_limpa = API_KEY.strip().lstrip('=').rstrip('=')
    
    for modelo in modelos:
        try:
            # URL sem query parameter - a key vai no header
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"
            
            # Headers com a API key no formato correto
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": api_key_limpa
            }
            
            payload = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }]
            }
            
            response = requests.post(
                url, 
                headers=headers,
                json=payload,
                timeout=30
            )
            
            # Se receber 400 ou 404, tenta próximo modelo
            if response.status_code in [400, 404]:
                print(f"⚠️  Modelo {modelo} não disponível (erro {response.status_code}). Tentando próximo...")
                continue
            
            # Se receber 429, para de tentar
            if response.status_code == 429:
                print(f"⚠️  Limite de requisições atingido (429) para {modelo}.")
                break
            
            response.raise_for_status()
            
            # Processa a resposta
            data = response.json()
            mensagem = (data.get("candidates", [{}])[0]
                       .get("content", {})
                       .get("parts", [{}])[0]
                       .get("text", "").strip())
            
            if mensagem:
                print(f"✅ Sucesso com modelo: {modelo}")
                print("\n--- Descritivo Gerado ---")
                print(mensagem)
                print("-------------------------\n")
                return mensagem
                
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response else 0
            if status_code in [400, 404]:
                print(f"⚠️  Modelo {modelo} retornou erro {status_code}. Tentando próximo modelo...")
                continue
            elif status_code == 429:
                print(f"⚠️  Limite de requisições atingido (429) para {modelo}.")
                break
            else:
                print(f"⚠️  Erro HTTP {status_code} com {modelo}.")
                continue
        except Exception as e:
            print(f"⚠️  Erro ao tentar {modelo}: {str(e)[:100]}")
            continue
    
    print("\n❌ Não foi possível gerar mensagem com nenhum modelo do Gemini.")
    print("💡 Usando mensagem padrão: 'Commit automático'")
    return "Commit automático"

def ler_versao():
    """Lê a versão atual do arquivo VERSION"""
    try:
        version_file = os.path.join(os.getcwd(), "VERSION")
        if not os.path.exists(version_file):
            # Se o arquivo não existir, cria com versão inicial
            with open(version_file, 'w') as f:
                f.write("1.0.0\n")
            return "1.0.0"
        
        with open(version_file, 'r') as f:
            versao = f.read().strip()
            if not versao:
                versao = "1.0.0"
            return versao
    except Exception as e:
        print(f"⚠️  Erro ao ler arquivo VERSION: {e}")
        return "1.0.0"

def escrever_versao(versao):
    """Escreve a nova versão no arquivo VERSION"""
    try:
        version_file = os.path.join(os.getcwd(), "VERSION")
        with open(version_file, 'w') as f:
            f.write(f"{versao}\n")
        return True
    except Exception as e:
        print(f"❌ Erro ao escrever arquivo VERSION: {e}")
        return False

def analisar_tipo_alteracao(diff_text):
    """Analisa o tipo de alteração usando a API do Gemini para determinar o incremento de versão"""
    if not ENABLE_VERSIONING:
        return None
    
    modelos = [
        'gemini-2.0-flash',
        'gemini-1.5-flash',
        'gemini-1.5-pro',
    ]
    
    prompt = (
        "Analise as seguintes alterações de código e determine o tipo de mudança seguindo Semantic Versioning (SemVer).\n"
        "Responda APENAS com uma das três palavras: MAJOR, MINOR ou PATCH\n\n"
        "- MAJOR: mudanças incompatíveis que quebram a API ou funcionalidades existentes\n"
        "- MINOR: novas funcionalidades adicionadas de forma compatível com versões anteriores\n"
        "- PATCH: correções de bugs e pequenas alterações que não alteram funcionalidades\n\n"
        "Seja conservador: prefira PATCH para correções e MINOR para novas funcionalidades.\n"
        "Use MAJOR apenas se houver mudanças que quebram compatibilidade.\n\n"
        f"Alterações:\n{diff_text[:5000]}"  # Limita o tamanho do diff
    )
    
    api_key_limpa = API_KEY.strip().lstrip('=').rstrip('=')
    
    for modelo in modelos:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": api_key_limpa
            }
            
            payload = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }]
            }
            
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=15
            )
            
            if response.status_code in [400, 404]:
                continue
            if response.status_code == 429:
                break
                
            response.raise_for_status()
            
            data = response.json()
            resposta = (data.get("candidates", [{}])[0]
                       .get("content", {})
                       .get("parts", [{}])[0]
                       .get("text", "").strip().upper())
            
            if resposta in ['MAJOR', 'MINOR', 'PATCH']:
                return resposta
                
        except Exception:
            continue
    
    # Se não conseguir determinar, usa PATCH como padrão conservador
    return 'PATCH'

def incrementar_versao(versao_atual, tipo_incremento):
    """Incrementa a versão de acordo com o tipo de incremento (MAJOR, MINOR, PATCH)"""
    try:
        partes = versao_atual.split('.')
        if len(partes) != 3:
            # Se a versão não estiver no formato correto, retorna 1.0.0
            return "1.0.0"
        
        major = int(partes[0])
        minor = int(partes[1])
        patch = int(partes[2])
        
        if tipo_incremento == 'MAJOR':
            major += 1
            minor = 0
            patch = 0
        elif tipo_incremento == 'MINOR':
            minor += 1
            patch = 0
        elif tipo_incremento == 'PATCH':
            patch += 1
        else:
            # Padrão: PATCH
            patch += 1
        
        nova_versao = f"{major}.{minor}.{patch}"
        return nova_versao
    except Exception as e:
        print(f"⚠️  Erro ao incrementar versão: {e}")
        return versao_atual

def restaurar_versao(versao_anterior):
    """Restaura a versão anterior do arquivo VERSION e remove do stage do git"""
    if not versao_anterior:
        return
    
    try:
        print(f"↩️  Restaurando versão anterior: {versao_anterior}")
        
        # Remove o arquivo VERSION do index do git primeiro (se estiver lá)
        try:
            version_file = os.path.join(os.getcwd(), "VERSION")
            current_dir = os.getcwd()
            if os.path.exists(os.path.join(current_dir, ".git")):
                subprocess.run(["git", "reset", "HEAD", version_file], 
                             check=False, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                subprocess.run(["git", "restore", "--staged", version_file], 
                             check=False, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except Exception:
            pass  # Ignora erros (pode não ser um repo git)
        
        # Restaura o conteúdo do arquivo VERSION
        if escrever_versao(versao_anterior):
            print(f"✅ Versão restaurada para: {versao_anterior}")
    except Exception as e:
        print(f"⚠️  Erro ao restaurar versão: {e}")

def atualizar_versao(diff_text):
    """Atualiza a versão do projeto baseado nas alterações. Retorna (nova_versao, versao_anterior)"""
    if not ENABLE_VERSIONING:
        return (None, None)
    
    try:
        versao_atual = ler_versao()
        versao_anterior = versao_atual  # Salva a versão anterior para possível rollback
        print(f"📦 Versão atual: {versao_atual}")
        
        print("🔄 Analisando tipo de alteração para versionamento...")
        tipo_alteracao = analisar_tipo_alteracao(diff_text)
        
        if not tipo_alteracao:
            print("⚠️  Não foi possível determinar o tipo de alteração. Mantendo versão atual.")
            return (None, None)
        
        nova_versao = incrementar_versao(versao_atual, tipo_alteracao)
        
        if nova_versao != versao_atual:
            print(f"📈 Incremento {tipo_alteracao}: {versao_atual} → {nova_versao}")
            if escrever_versao(nova_versao):
                # Adiciona o arquivo VERSION ao index do git para garantir que seja commitado
                try:
                    version_file = os.path.join(os.getcwd(), "VERSION")
                    subprocess.run(["git", "add", version_file], check=True, stderr=subprocess.DEVNULL)
                except Exception:
                    pass  # Ignora erros ao adicionar ao git (pode não ser um repo git ainda)
                return (nova_versao, versao_anterior)
        else:
            print(f"ℹ️  Versão permanece: {versao_atual}")
        
        return (None, None)
    except Exception as e:
        print(f"⚠️  Erro ao atualizar versão: {e}")
        return (None, None)

def criar_commit(mensagem):
    """Cria um novo commit com a mensagem fornecida"""
    try:
        subprocess.run(["git", "add", "--all"], check=True)
        subprocess.run(["git", "commit", "-m", mensagem], check=True)
        print("✅ Commit realizado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar commit: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro ao criar commit: {e}")
        return False

def main():
    """Função principal do programa"""
    nova_versao = None
    versao_anterior = None
    
    try:
        print("🤖 AutoCommit iniciado...")

        # Verifica as variáveis de ambiente
        if not verificar_variaveis_ambiente():
            return

        # Verifica o repositório Git
        if not verificar_repositorio():
            return

        # Obtém alterações
        alteracoes = obter_alteracoes()
        if not alteracoes:
            return

        # Atualiza a versão se o versionamento estiver habilitado
        if ENABLE_VERSIONING:
            nova_versao, versao_anterior = atualizar_versao(alteracoes)
            # Não precisa reobter alterações pois o arquivo VERSION já foi adicionado ao index
            # e será incluído automaticamente no commit
        
        # Gera mensagem de commit
        mensagem = gerar_mensagem_commit(alteracoes)
        
        # Adiciona informação da versão na mensagem se houver atualização
        if nova_versao:
            # Adiciona a versão no início da mensagem
            primeira_linha = mensagem.split('\n')[0]
            resto_mensagem = '\n'.join(mensagem.split('\n')[1:]) if '\n' in mensagem else ""
            mensagem = f"{primeira_linha} (v{nova_versao})"
            if resto_mensagem:
                mensagem += f"\n{resto_mensagem}"
        
        # Mostra a mensagem que será usada
        if mensagem == "Commit automático":
            print(f"\n📝 Mensagem que será usada: '{mensagem}'")
        else:
            print(f"\n📝 Mensagem gerada: '{mensagem}'")

        # Confirma com o usuário
        confirmar = input("❓ Deseja usar esta mensagem para o commit? (s/n): ").strip().lower()
        if confirmar != 's':
            print("❌ Commit cancelado.")
            # Restaura a versão anterior se foi atualizada
            if nova_versao and versao_anterior:
                restaurar_versao(versao_anterior)
            return

        # Cria o commit
        commit_sucesso = criar_commit(mensagem)
        
        # Se o commit falhou, restaura a versão anterior
        if not commit_sucesso and nova_versao and versao_anterior:
            restaurar_versao(versao_anterior)

    except KeyboardInterrupt:
        print("\n❌ Operação cancelada pelo usuário.")
        # Restaura a versão anterior se foi atualizada
        if nova_versao and versao_anterior:
            restaurar_versao(versao_anterior)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        # Restaura a versão anterior se foi atualizada
        if nova_versao and versao_anterior:
            restaurar_versao(versao_anterior)

if __name__ == "__main__":
    main()
