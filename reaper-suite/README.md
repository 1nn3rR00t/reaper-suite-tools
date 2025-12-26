# 💀 Reaper Suite - Advanced Web Fuzzer 💀

## Table of Contents
1. [Overview](#1-overview)
2. [Features](#2-features)
3. [Installation](#3-installation)
4. [Usage](#4-usage)
5. [Examples](#5-examples)
6. [Screenshots](#6-screenshots)
7. [License](#7-license)

---

## 1. Overview

The **Reaper Suite** is a highly customizable and intelligent web fuzzer designed for advanced reconnaissance and vulnerability discovery in web applications. Built with Python, it incorporates stealth techniques and intelligent target fingerprinting to evade detection and optimize attack strategies.

It's suitable for penetration testers, red team operators, and security researchers aiming for a deeper understanding of target infrastructure and bypassing common security mechanisms (WAFs, IDS/IPS).

---

## 2. Features

* **Customizable Fuzzing:** Supports GET and POST requests, custom headers, and dynamic payload injection (`FUZZ` keyword).
* **Stealth Capabilities:**
    * **Randomized Delays:** `--delay <min-max>` (e.g., `0.5-2.0s`) to mimic human browsing patterns.
    * **User-Agent Rotation:** Automatically rotates through a list of common User-Agents to prevent blacklisting.
    * **Proxy Support:** `--proxies <file.txt>` for rotating through a list of HTTP/SOCKS proxies.
* **Intelligent Filtering & Validation:**
    * **Hide by Status Code/Size:** `--hc 404,500` and `--hs 0,1234` to filter out irrelevant responses.
    * **Content-based Filtering:** `--fail "Wrong password"` or `--success "Welcome admin"` to identify valid hits based on response body.
* **Cyber-Intelligence & Auto-Advice:**
    * **Tech Fingerprinting:** Automatically identifies server technologies (PHP, ASP.NET, Apache, Nginx) from HTTP headers.
    * **Extension Suggestions:** Provides tactical advice on relevant file extensions (`.php`, `.aspx`) based on identified technologies.
* **Professional Reporting:** Generate detailed HTML reports (`-o report.html`) summarizing findings in a clean, executive-friendly format.
* **Kali/WSL2 Optimized:** Includes a `setup.sh` script for easy installation and path configuration on Debian-based systems.

---

## 3. Installation

### Prerequisites

* Python 3.x
* Kali Linux or WSL2 (Ubuntu/Debian-based)

### Steps

1.  **Clone the `reaper-suite-tools` repository:**
    ```bash
    git clone [https://github.com/YourGitHubUsername/reaper-suite-tools.git](https://github.com/YourGitHubUsername/reaper-suite-tools.git)
    cd reaper-suite-tools/reaper-suite
    ```
2.  **Make the installation script executable:**
    ```bash
    chmod +x setup.sh
    ```
3.  **Run the setup script:**
    ```bash
    ./setup.sh
    ```
    *(This script will install Python dependencies (`python3-requests`) and create a symbolic link, allowing you to run `reaper` from any directory.)*

### Manual Installation (if `setup.sh` fails)

```bash
# Install Python requests
sudo apt update
sudo apt install -y python3-requests # For Debian/Ubuntu/Kali
# OR for Arch: sudo pacman -S python-requests

# Make the script executable
chmod +x reaper_suite.py

# (Optional) Add to PATH manually
sudo ln -s "$(pwd)/reaper_suite.py" /usr/local/bin/reaper
