#!/bin/bash

# --- CORES NEON PARA O SETUP ---
C_PINK="\033[38;2;255;45;170m"
C_CYAN="\033[38;2;0;255;255m"
C_PURP="\033[38;2;145;70;255m"
X="\033[0m"

echo -e "${C_PINK}    ____  __________ _____  __________ "
echo -e "   / __ \/ ____/ __ / __ \/ ____/ __  \\"
echo -e "${C_PURP}  / /_/ / __/ / /_/ / /_/ / __/ / /_/ /"
echo -e " / _, _/ /___/ __  / ____/ /___/ _, _/ "
echo -e "${C_CYAN}/_/ |_/_____/_/ |_/_/   /_____/_/ |_|   "
echo -e "         [ SETUP PROTOCOL - v11.0 ]${X}\n"

# 1. Atualizar e instalar dependências do sistema
echo -e "${C_CYAN}[*]${X} A instalar dependências do sistema (wkhtmltopdf)..."
sudo apt update -y && sudo apt install -y wkhtmltopdf python3-pip

# 2. Instalar bibliotecas Python necessárias
echo -e "${C_CYAN}[*]${X} A configurar ambiente Python (requests)..."
pip3 install requests

# 3. Criar Wordlists de teste
echo -e "${C_CYAN}[*]${X} A gerar wordlists de laboratório..."
echo -e "admin\nconfig\nbackup\napi\nindex\nlogin\nphpmyadmin\n.env" > common.txt
echo -e "www\ndev\napi\nstaging\nmail\nadmin\ntest\ninternal" > vhosts.txt

# 4. Configurar permissões
echo -e "${C_CYAN}[*]${X} A ajustar permissões de execução..."
chmod +x reaper_suite.py
chmod +x victim.py

# 5. Instrução para o ficheiro HOSTS
echo -e "\n${C_PINK}[!] ATENÇÃO - CONFIGURAÇÃO MANUAL NECESSÁRIA:${X}"
echo -e "Para o modo VHOST realista, como exemplo adicione esta linha ao teu ${C_CYAN}/etc/hosts${X}:"
echo -e "${C_PURP}127.0.0.1   megacorp-internal.local dev.megacorp-internal.local api.megacorp-internal.local staging.megacorp-internal.local mail.megacorp-internal.local admin.megacorp-internal.local${X}"

echo -e "\n${C_CYAN}[+]${X} Setup concluído com sucesso. O laboratório está pronto."
