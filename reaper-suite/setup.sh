#!/bin/bash

# --- REAPER SUITE INSTALLER FOR ARCH LINUX ---
# Autor: 1nn3rR00t

# Cores para o terminal
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # Sem cor

echo -e "${GREEN}[*] A iniciar instalação da Reaper Suite...${NC}"

# 1. Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[!] Python3 não encontrado. Instala-o com: sudo pacman -S python${NC}"
    exit 1
fi

# 2. Instalar dependências (requests) via pacman (preferível no Arch) ou pip
echo -e "${GREEN}[*] A instalar dependências...${NC}"
sudo pacman -S --noconfirm python-requests &> /dev/null

# 3. Dar permissão de execução ao script principal
chmod +x reaper_suite.py

# 4. Criar um link simbólico para o /usr/local/bin
# Isso permite que corras 'reaper' em qualquer lugar do terminal
echo -e "${GREEN}[*] A configurar comando global...${NC}"
sudo ln -sf "$(pwd)/reaper_suite.py" /usr/local/bin/reaper

# 5. Finalização
echo -e "${GREEN}[+] Instalação concluída com sucesso!${NC}"
echo -e "${GREEN}[+] Agora podes usar o comando: ${NC}${RED}reaper -u http://alvo.com -w wordlist.txt ...${NC}"
