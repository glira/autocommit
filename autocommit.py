#!/usr/bin/env python3
import os
import sys
import subprocess
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura as variáveis de ambiente
API_KEY = os.getenv('API_KEY')
GIT_USER_NAME = os.getenv('GIT_USER_NAME')
GIT_USER_EMAIL = os.getenv('GIT_USER_EMAIL')

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
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": (
                        "Faça em portugues, gere uma mensagem de commit detalhada "
                        "com base nas seguintes diferenças entre os arquivos. "
                        "Sua primeira linha na resposta deve ser o título:\n"
                        f"{diff_text}"
                    )
                }]
            }]
        }
        
        response = requests.post(
            url, 
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=15
        )
        response.raise_for_status()
        
        # Processa a resposta
        data = response.json()
        mensagem = (data.get("candidates", [{}])[0]
                   .get("content", {})
                   .get("parts", [{}])[0]
                   .get("text", "").strip())
        
        if mensagem:
            print("\n--- Descritivo Gerado ---")
            print(mensagem)
            print("-------------------------\n")
            return mensagem
                
    except Exception as e:
        print(f"❌ Erro ao gerar mensagem com Gemini: {e}")
    
    return "Commit automático"

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

def main():
    """Função principal do programa"""
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

        # Gera mensagem de commit
        mensagem = gerar_mensagem_commit(alteracoes)

        # Confirma com o usuário
        confirmar = input("❓ Deseja usar este descritivo para o commit? (s/n): ").strip().lower()
        if confirmar != 's':
            print("❌ Commit cancelado.")
            return

        # Cria o commit
        criar_commit(mensagem)

    except KeyboardInterrupt:
        print("\n❌ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
