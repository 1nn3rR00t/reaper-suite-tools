#!/usr/bin/env python3
import requests, sys, argparse, socket, threading, json, os, signal
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from urllib.parse import urlparse

# --- PALETA DE CORES NEON (TRUECOLOR RGB 24-BIT) ---
C_PINK   = "\033[38;2;255;45;170m"   # Neon Pink
C_CYAN   = "\033[38;2;0;255;255m"    # Electric Cyan
C_PURP   = "\033[38;2;145;70;255m"   # Deep Purple
C_WHITE  = "\033[38;2;255;255;255m"
C_DIM    = "\033[38;2;80;80;80m"     # Stealth Grey
BOLD     = "\033[1m"
X        = "\033[0m"

print_lock = threading.Lock()
findings = []
shutdown_flag = False

def signal_handler(sig, frame):
    """Força o encerramento imediato ao pressionar Ctrl+C"""
    global shutdown_flag
    shutdown_flag = True
    print(f"\n\n{C_PINK}[!] ABORTING OPERATIONS (USER INTERRUPT)...{X}")
    os._exit(0) # Mata o processo instantaneamente sem esperar threads

signal.signal(signal.SIGINT, signal_handler)

def print_banner():
    banner = rf"""
{C_PINK}    ____  __________ _____  __________ 
{C_PINK}   / __ \/ ____/ __ / __ \/ ____/ __  \
{C_PURP}  / /_/ / __/ / /_/ / /_/ / __/ / /_/ /
{C_PURP} / _, _/ /___/ __  / ____/ /___/ _, _/ 
{C_CYAN}/_/ |_/_____/_/ |_/_/   /_____/_/ |_|   
{C_CYAN}         [ 1NN3RR00T - CORE v11.0 ]{X}"""
    print(banner)

def print_hud(args, target_ip, total_payloads):
    now = datetime.now().strftime("%H:%M:%S")
    div = f"{C_PURP}━{'━' * 58}━{X}"
    print(div)
    print(f"{C_CYAN}{BOLD} ► INFRASTRUCTURE LOGIC{X}")
    print(f"   {C_PINK}target:{X}  {C_WHITE}{args.url}{X}")
    print(f"   {C_PINK}addr:{X}    {C_WHITE}{target_ip}{X} {C_PURP}│{X} {C_PINK}time:{X} {C_WHITE}{now}{X}")
    print(div)
    print(f"{C_CYAN}{BOLD} ► KERNEL CONFIGURATION{X}")
    print(f"   {C_PURP}[mode]{X}   {C_WHITE}{args.mode.upper()}{X}    {C_PURP}[threads]{X} {C_WHITE}{args.threads}{X}")
    print(f"   {C_PURP}[load]{X}   {C_WHITE}{total_payloads} payloads{X}")
    if args.extensions: print(f"   {C_PURP}[exts]{X}   {C_CYAN}{args.extensions}{X}")
    print(div)
    print(f"{C_CYAN}{BOLD} ► ACTIVE FILTERS{X}")
    print(f"   {C_PINK}drop_code:{X} {C_WHITE}{args.hc}{X}   {C_PINK}drop_size:{X} {C_WHITE}{args.hs}{X}")
    print(div + "\n")

def generate_reports(target, findings_list):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"reaper_report_{timestamp}"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>REAPER INTELLIGENCE REPORT</title>
        <style>
            body {{ background: #0a0a0c; color: #00ffff; font-family: 'Courier New', monospace; padding: 40px; line-height: 1.6; }}
            .container {{ border: 2px solid #ff2da2; box-shadow: 0 0 20px #ff2da2; padding: 30px; background: rgba(255, 45, 170, 0.05); border-radius: 8px; }}
            h1 {{ color: #ff2da2; text-transform: uppercase; border-bottom: 2px solid #00ffff; padding-bottom: 10px; }}
            .finding {{ background: #1a1a1d; margin: 10px 0; padding: 15px; border-left: 5px solid #00ffff; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>💀 Reaper Intelligence Report</h1>
            <h3>ALVO: {target} | HITS: {len(findings_list)}</h3>
            {''.join([f'<div class="finding">{f}</div>' for f in findings_list])}
        </div>
    </body>
    </html>
    """
    
    with open(f"{report_name}.html", "w", encoding="utf-8") as f: f.write(html_content)
    
    report_data = {"target": target, "results": findings_list}
    with open(f"{report_name}.json", "w", encoding="utf-8") as f: json.dump(report_data, f, indent=4)

    print(f"\n{C_CYAN}[REPORT]{X} Web Report: {C_WHITE}{report_name}.html{X}")

def worker(payload, target_url, h_codes, h_sizes, verbose, mode, base_domain):
    if shutdown_flag: return

    current_host = f"{payload}.{base_domain}" if mode == "vhost" else base_domain
    headers = {"User-Agent": "1NN3RR00T-Reaper/11.0", "Host": current_host}

    try:
        url = target_url if mode == "vhost" else target_url.replace("FUZZ", payload)
        
        # Timeout curto (3s) para evitar travamento em 100 threads
        res = requests.get(url, headers=headers, timeout=3, allow_redirects=False)
        
        size = len(res.content)
        is_hit = res.status_code not in h_codes and size not in h_sizes

        with print_lock:
            if is_hit:
                sys.stdout.write("\r\033[2K")
                display = current_host if mode == "vhost" else payload
                print(f"{C_CYAN}[FOUND]{X} {C_WHITE}{display:<30}{X} {C_PINK}➔{X} Status: {C_CYAN}{res.status_code:<3}{X} {C_PURP}│{X} Size: {C_CYAN}{size}B{X}")
                findings.append(display)
            
            elif verbose and not shutdown_flag:
                # Throttle ajustado para 100 threads: imprime menos frequentemente para não travar o console
                if hash(payload) % 100 == 0: 
                    display_payload = (payload[:35] + '..') if len(payload) > 35 else payload
                    sys.stdout.write(f"\r\033[2K{C_DIM}[*] Scanning kernel: {display_payload:<40}{X}")
                    sys.stdout.flush()

    except Exception: pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-w", "--wordlist", required=True)
    parser.add_argument("-m", "--mode", choices=['dir', 'vhost'], default='dir')
    parser.add_argument("-t", "--threads", type=int, default=30)
    parser.add_argument("-x", "--extensions")
    parser.add_argument("--hc", default="404")
    parser.add_argument("--hs", default="0")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    print("\033c", end="")
    print_banner()

    parsed = urlparse(args.url)
    base_domain = parsed.hostname
    try: ip = socket.gethostbyname(base_domain)
    except: ip = "127.0.0.1"

    # [CORREÇÃO] Leitura de arquivo otimizada
    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            raw_payloads = f.read().splitlines()
    except FileNotFoundError:
        print(f"{C_PINK}[!] Wordlist not found!{X}")
        sys.exit(1)
    
    # Limpeza de payload ANTES de entrar nas threads
    payloads = [p.strip() for p in raw_payloads if p.strip() and not p.strip().startswith('#')]

    if args.extensions and args.mode == 'dir':
        extended_payloads = [f"{p}.{e.strip()}" for p in payloads for e in args.extensions.split(",")]
        payloads += extended_payloads

    print_hud(args, ip, len(payloads))
    target_path = args.url if "FUZZ" in args.url or args.mode == 'vhost' else args.url.rstrip('/') + "/FUZZ"

    print(f"{C_PURP}{BOLD}>>> INITIALIZING INFILTRATION PROTOCOL...{X}\n")

    engine = partial(worker, target_url=target_path, h_codes=[int(x) for x in args.hc.split(",")],
                     h_sizes=[int(x) for x in args.hs.split(",")], verbose=args.verbose,
                     mode=args.mode, base_domain=base_domain)

    # Execução protegida para garantir que Ctrl+C funcione
    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            # map() pode bloquear Ctrl+C, então iteramos para manter o controle
            for _ in executor.map(engine, payloads):
                pass
    except KeyboardInterrupt:
        signal_handler(None, None)

    sys.stdout.write("\r\033[2K")
    print(f"\n{C_CYAN}[+]{X} Operation Complete. {BOLD}{len(findings)}{X} access points verified.")
    
    if findings:
        generate_reports(args.url, findings)

if __name__ == "__main__":
    main()