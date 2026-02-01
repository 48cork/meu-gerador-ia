#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificação pré-deploy
Verifica se o projeto está pronto para GitHub e Streamlit Cloud
"""
import os
import sys
import io
from pathlib import Path

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def check_file_exists(filepath, required=True):
    """Verifica se um arquivo existe"""
    exists = Path(filepath).exists()
    status = "✅" if exists else ("❌" if required else "⚠️")
    print(f"{status} {filepath}")
    return exists

def check_not_in_gitignore(filepath):
    """Verifica se um arquivo NÃO está no .gitignore (deveria estar)"""
    if not Path(".gitignore").exists():
        return False
    
    with open(".gitignore", "r", encoding="utf-8") as f:
        gitignore_content = f.read()
    
    return filepath in gitignore_content or f"/{filepath}" in gitignore_content

def main():
    print("🔍 Verificando projeto para deploy...\n")
    
    errors = []
    warnings = []
    
    # Arquivos essenciais
    print("📁 Arquivos Essenciais:")
    essential_files = [
        "app.py",
        "requirements.txt",
        "README.md",
        ".gitignore",
    ]
    
    for file in essential_files:
        if not check_file_exists(file):
            errors.append(f"Arquivo essencial faltando: {file}")
    
    # Arquivos de configuração
    print("\n⚙️ Arquivos de Configuração:")
    config_files = [
        ".streamlit/config.toml",
        "env.template",
    ]
    
    for file in config_files:
        check_file_exists(file, required=False)
    
    # Verificar segurança
    print("\n🔒 Verificação de Segurança:")
    sensitive_files = [".env", ".streamlit/secrets.toml"]
    
    for file in sensitive_files:
        if check_file_exists(file, required=False):
            if not check_not_in_gitignore(file):
                errors.append(f"⚠️ {file} existe mas NÃO está no .gitignore!")
            else:
                print(f"✅ {file} está no .gitignore (correto)")
    
    # Verificar estrutura de diretórios
    print("\n📂 Estrutura de Diretórios:")
    dirs = ["agents", ".streamlit"]
    for dir_name in dirs:
        check_file_exists(dir_name, required=False)
    
    # Verificar requirements.txt
    print("\n📦 Verificando requirements.txt:")
    if Path("requirements.txt").exists():
        with open("requirements.txt", "r") as f:
            content = f.read()
            required_packages = ["streamlit", "pandas", "google-generativeai", "python-dotenv"]
            for pkg in required_packages:
                if pkg in content:
                    print(f"✅ {pkg} encontrado")
                else:
                    warnings.append(f"⚠️ {pkg} não encontrado em requirements.txt")
    
    # Resumo
    print("\n" + "="*60)
    print("📊 RESUMO")
    print("="*60)
    
    if errors:
        print(f"\n❌ ERROS ENCONTRADOS ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")
        print("\n⚠️ Corrija os erros antes de fazer deploy!")
        return False
    
    if warnings:
        print(f"\n⚠️ AVISOS ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")
    
    print("\n✅ Projeto está pronto para deploy!")
    print("\n📝 Próximos passos:")
    print("  1. git add .")
    print("  2. git commit -m 'Preparado para deploy'")
    print("  3. git push origin main")
    print("  4. Acesse https://share.streamlit.io")
    print("  5. Configure as Secrets (GOOGLE_API_KEY)")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
