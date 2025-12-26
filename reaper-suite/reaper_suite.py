#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REAPER SUITE - v11.0 Intelligence
Dev: 1nn3rR00t
Kali Linux / WSL2 Optimized
"""

import requests
import sys
import argparse
import time
import threading
import socket
import datetime
import random
from concurrent.futures import ThreadPoolExecutor
from functools import partial

# --- Terminal Aesthetics ---
R, G, C, M, Y, B, X = "\033[91m", "\033[92m", "\033[96m", "\033[95m", "\033[93m", "\033[1m", "\033[0m"
DIM = "\033[2m"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
]

print_lock = threading.Lock()
findings = []

def get_ip(url):
    try:
        host = url.split("://")[-1].split("/")[0].split(":")[0]
        return socket.gethostbyname(host)
    except: return "Unknown"

def tech_fingerprint(url, headers_base):
    """
    Tries to identify the server stack to provide tactical advice.
    """
    try:
        # Grab a quick response to check headers
        res = requests.head(url, headers=headers_base, timeout=5, allow_redirects=True)
        server = res.headers.get("Server", "").lower()
        powered = res.headers.get("X-Powered-By", "").lower()
        
        techs = []
        advice = []

        if "php" in server or "php" in powered:
            techs.append("PHP")
            advice.append(".php, .phtml, .php3")
        if "asp.net" in powered or "microsoft-iis" in server:
            techs.append("ASP.NET / IIS")
            advice.append(".asp, .aspx, .config")
        if "apache" in server: techs.append("Apache")
        if "nginx" in server: techs.append("Nginx")

        if techs:
            print(f"{Y}[TECH-IDENTIFIED]{X} Stack: {B}{', '.join(techs)}{X}")
            if advice:
                print(f"{C}[STRATEGY]{X} Sugestão de extensões: {G}{', '.join(advice)}{X}")
        return techs
    except:
        return []

def worker_engine(payload, target_url, method, data_tmp, base_headers, h_codes, h_sizes, fail_str, success_str, delay, verbose):
    # Stealth delay jitter
    if delay:
        d_min, d_max = map(float, delay.split('-')) if '-' in delay else (float(delay), float(delay))
        time.sleep(random.uniform(d_min, d_max))

    # UA Rotation per request
    headers = base_headers.copy()
    headers["User-Agent"] = random.choice(USER_AGENTS)

    url = target_url.replace("FUZZ", payload)
    data = data_tmp.replace("FUZZ", payload) if data_tmp else None

    # Determine context for the report
    ctx = "FILE/DIR"
    if data_tmp:
        dt = data_tmp.lower()
        if any(x in dt for x in ["pass", "pwd", "secret"]): ctx = "PASSWORD"
        elif any(x in dt for x in ["user", "login"]): ctx = "USER"

    if verbose:
        with print_lock:
            sys.stdout.write(f"\r{DIM}[*] Checking: {payload[:30]}{X}\033[K")
            sys.stdout.flush()

    try:
        res = requests.request(method, url, data=data, headers=headers, timeout=7, allow_redirects=True)
        body = res.content.decode('utf-8', errors='ignore')

        # Logic for a valid hit
        is_hit = True
        if res.status_code in h_codes or len(res.content) in h_sizes: is_hit = False
        if fail_str and fail_str in body: is_hit = False
        if success_str and success_str not in body: is_hit = False

        if is_hit:
            with print_lock:
                sys.stdout.write("\r\033[K")
                color = G if ctx in ["PASSWORD", "USER"] else C
                print(f"{color}[{ctx}]{X} {payload:<20} | Status: {res.status_code} | Size: {len(res.content)}")
                findings.append({"type": ctx, "payload": payload, "code": res.status_code, "size": len(res.content)})
    except: pass

def main():
    parser = argparse.ArgumentParser(description="Reaper v11.0 - 1nn3rR00t")
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-w", "--wordlist", required=True)
    parser.add_argument("-m", "--mode", choices=['vhost', 'dir', 'custom'], default='custom')
    parser.add_argument("-d", "--data")
    parser.add_argument("-x", "--extensions")
    parser.add_argument("-t", "--threads", type=int, default=30)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("--delay")
    parser.add_argument("--hc", default="404")
    parser.add_argument("--hs", default="0")
    parser.add_argument("--fail")
    parser.add_argument("--success")
    
    args = parser.parse_args()

    # Load wordlist early
    try:
        with open(args.wordlist, 'r', errors='ignore') as f:
            payloads_raw = f.read().splitlines()
    except:
        print(f"{R}[-]{X} Wordlist não encontrada."); sys.exit(1)

    # Initial UI
    print("\033c", end="")
    print(f"{M}{B}REAPER v11.0{X} | {C}Cyber-Intelligence Mode{X}")
    print(f"{DIM}Target: {args.url} | Wordlist: {args.wordlist.split('/')[-1]}{X}\n")

    # Run Fingerprinting
    base_headers = {"User-Agent": random.choice(USER_AGENTS)}
    target_clean = args.url if "://" in args.url else f"http://{args.url}"
    techs = tech_fingerprint(target_clean, base_headers)

    # Auto-extension logic (optional, but professional)
    final_payloads = []
    ext_list = args.extensions.split(",") if args.extensions else []
    
    for p in payloads_raw:
        final_payloads.append(p)
        for ext in ext_list:
            final_payloads.append(f"{p}.{ext.strip('.')}")

    # Execution
    h_codes = [int(x) for x in args.hc.split(",")]
    h_sizes = [int(x) for x in args.hs.split(",")]
    
    target_url = target_clean
    if args.mode == "dir" and "FUZZ" not in target_url:
        target_url = f"{target_url.rstrip('/')}/FUZZ"

    print(f"{R}>>> INICIANDO ATAQUE EM {len(final_payloads)} ENDPOINTS...{X}\n")

    worker = partial(worker_engine, target_url=target_url, method="POST" if args.data else "GET",
                     data_tmp=args.data, base_headers=base_headers, h_codes=h_codes, h_sizes=h_sizes,
                     fail_str=args.fail, success_str=args.success, delay=args.delay, verbose=args.verbose)

    try:
        with ThreadPoolExecutor(max_workers=args.threads) as pool:
            pool.map(worker, final_payloads)
    except KeyboardInterrupt:
        print(f"\n{R}[!] Abortando por comando do usuário.{X}")

    print(f"\n{G}[+]{X} Fim da operação. Total de achados: {len(findings)}")

if __name__ == "__main__":
    main()
