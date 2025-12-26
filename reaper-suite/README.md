# 💀 Reaper Suite - Advanced Web Fuzzer 💀

![Banner](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/screenshots/hud.png)

> **Languages:** [English](#english) | [Português](#português)

----------------------------------------------------------------------------------------------------------------------------------------------------------->

<a name="english"></a>
## 🇺🇸 English Version

### 1. Overview
Highly customizable and intelligent web fuzzer designed for advanced reconnaissance. It incorporates stealth techniques and intelligent target fingerprinting to optimize attack strategies.

### 2. Key Features
* **Cyber-Intelligence:** Automatically identifies technologies (PHP, Nginx, etc.) and suggests file extensions.
* **Stealth Protocol:** Randomized delays and User-Agent rotation to bypass WAFs.
* **Intelligent Filtering:** Filter by status code, size (bytes), or specific response strings.

### 3. Installation & Usage
```bash
chmod +x setup.sh && ./setup.sh
reaper -u [http://target.com/FUZZ](http://target.com/FUZZ) -w wordlist.txt -v
```

### 4. Advanced Commands

Flag	Description
-x	Append extensions (e.g., php,txt,bak).
--hs	Hide Size: Ignore responses by exact byte size (e.g., --hs 719).
--delay	Set request delay for stealth (e.g., 0.5-1.5).

### 5. Practical Examples
Bypassing 719-byte Static Errors: reaper -u http://target.local/FUZZ -w common.txt --hs 719


### 6. 📸 Evidence & Screenshots (PoC)


🖥️ A. Terminal HUD & Target Intell


⚡ B. Infiltration Operation (Active Bypass)


### 7. ⚖️ License & Disclaimer
License: MIT License. Disclaimer: Esta ferramenta foi desenvolvida estritamente para fins educacionais e testes de penetração autorizados. O uso indevido é de total responsabilidade do usuário.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 1. Visão Geral
Fuzzer web inteligente e customizável desenvolvido para reconhecimento avançado. Incorpora técnicas de furtividade (stealth) e identificação de tecnologias do alvo para otimizar auditorias de segurança.

### 2. Funcionalidades Principais
Inteligência Cibernética: Identifica automaticamente tecnologias (PHP, Nginx, etc.) e sugere extensões de arquivos.

Protocolo Stealth: Delays aleatórios e rotação de User-Agent para evitar bloqueios.

Filtragem Inteligente: Filtre por código de status, tamanho ou strings específicas no corpo da resposta (ex: erro de 719 bytes).

### 3. Instalação e Uso
chmod +x setup.sh && ./setup.sh
reaper -u [http://target.com/FUZZ](http://target.com/FUZZ) -w wordlist.txt -v


### 4. Comandos Avançados
-x	Adiciona extensões (ex: php,txt,bak).
--hs	Hide Size: Ignora respostas por tamanho exato de bytes (ex: --hs 719).
--delay	Define o atraso das requisições para furtividade (ex: 0.5-1.5).


### 5. Exemplos Práticos
Bypass de Erros Estáticos de 719 bytes: reaper -u http://target.local/FUZZ -w common.txt --hs 719


### 6. 📸 Evidências & Capturas de Tela (PoC)

🖥️ A. HUD do Terminal & Inteligência de Alvo


⚡ B. Operação de Infiltração (Bypass Ativo)


📊 C. Relatórios Profissionais


### 7. ⚖️ Licença & Aviso Legal
Licença: Licença MIT. Aviso Legal: Esta ferramenta foi desenvolvida estritamente para fins educacionais e testes de penetração autorizados. O uso indevido é de total responsabilidade do usuário.

----------------------------------------------------------------------------------------------------------------------------------------------------------->

Desenvolvido por 1nn3rR00t | Shadow Walker Operations
