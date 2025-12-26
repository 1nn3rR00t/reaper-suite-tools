![Banner](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/hud.png)

# 💀 Reaper Suite - Advanced Web Fuzzer 💀

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

![usage](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/usage.png)

```
usage: reaper [-h] -u URL -w WORDLIST [-m {dir,vhost}] [-t THREADS] [-x EXTENSIONS] [--hc HC] [--hs HS] [-v]

options:
  -h, --help            show this help message and exit
  -u, --url URL
  -w, --wordlist WORDLIST
  -m, --mode {dir,vhost}
  -t, --threads THREADS
  -x, --extensions EXTENSIONS
  --hc HC
  --hs HS
  -v, --verbose
```


### 5. Practical Examples
Bypassing 719-byte Static Errors: reaper -u http://target.local/FUZZ -w common.txt --hs 719


### 6. 📸 Evidence & Screenshots (PoC)


🖥️ A. Terminal HUD & Target Intell

![hud](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/hud.png)

⚡ B. Infiltration Operation (Active Bypass)

![vhost](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/vhost.png)

📊 C. Professional Report

![report_created](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_created.png)

![report_generated](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_generated.png)


```
Example execution command: wkhtmltopdf reaper_report_2025-12-26_14-04-14.html Relatorio_Final_Megacorp.pdf

Loading pages (1/6)
Counting pages (2/6)
Resolving links (4/6)
Loading headers and footers (5/6)
Printing pages (6/6)
Done
```

Report WEB Example:

![report_web](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_web.png)

Report PDF Example:

![report_pdf](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_pdf.png)

### 7. ⚖️ License & Disclaimer
License: MIT License. Disclaimer: Esta ferramenta foi desenvolvida estritamente para fins educacionais e testes de penetração autorizados. O uso indevido é de total responsabilidade do usuário.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<a name="português"></a>
## BR Versão em Português

### 1. Visão Geral
Fuzzer web inteligente e customizável desenvolvido para reconhecimento avançado. Incorpora técnicas de furtividade (stealth) e identificação de tecnologias do alvo para otimizar auditorias de segurança.

### 2. Funcionalidades Principais
Inteligência Cibernética: Identifica automaticamente tecnologias (PHP, Nginx, etc.) e sugere extensões de arquivos.

Protocolo Stealth: Delays aleatórios e rotação de User-Agent para evitar bloqueios.

Filtragem Inteligente: Filtre por código de status, tamanho ou strings específicas no corpo da resposta (ex: erro de 719 bytes).

### 3. Instalação e Uso
```
chmod +x setup.sh && ./setup.sh
reaper -u [http://target.com/FUZZ](http://target.com/FUZZ) -w wordlist.txt -v
```

### 4. Comandos Avançados
![usage](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/usage.png)

```
usage: reaper [-h] -u URL -w WORDLIST [-m {dir,vhost}] [-t THREADS] [-x EXTENSIONS] [--hc HC] [--hs HS] [-v]

options:
  -h, --help            show this help message and exit
  -u, --url URL
  -w, --wordlist WORDLIST
  -m, --mode {dir,vhost}
  -t, --threads THREADS
  -x, --extensions EXTENSIONS
  --hc HC
  --hs HS
  -v, --verbose
```

### 5. Exemplos Práticos
Bypass de Erros Estáticos de 719 bytes: reaper -u http://target.local/FUZZ -w common.txt --hs 719


### 6. 📸 Evidências & Capturas de Tela (PoC)

🖥️ A. HUD do Terminal & Inteligência de Alvo

![hud](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/hud.png)

⚡ B. Operação de Infiltração (Bypass Ativo)

![vhost](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/vhost.png)

📊 C. Relatórios Profissionais

![report_created](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_created.png)

![report_generated](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_generated.png)

Exemplo de execução: wkhtmltopdf reaper_report_2025-12-26_14-04-14.html Relatorio_Final_Megacorp.pdf

Loading pages (1/6)
Counting pages (2/6)
Resolving links (4/6)
Loading headers and footers (5/6)
Printing pages (6/6)
Done

Exemplo de relatorio WEB:

![report_web](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_web.png)

Exemplo de relatorio PDF:

![report_pdf](https://github.com/1nn3rR00t/reaper-suite-tools/blob/main/reaper-suite/assets/report_pdf.png)

### 7. ⚖️ Licença & Aviso Legal
Licença: Licença MIT. Aviso Legal: Esta ferramenta foi desenvolvida estritamente para fins educacionais e testes de penetração autorizados. O uso indevido é de total responsabilidade do usuário.

----------------------------------------------------------------------------------------------------------------------------------------------------------->

Desenvolvido por 1nn3rR00t | Shadow Walker Operations
