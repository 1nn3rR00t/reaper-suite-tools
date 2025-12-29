from http.server import HTTPServer, BaseHTTPRequestHandler

class VictimHandler(BaseHTTPRequestHandler):
    def send_my_headers(self, status=200):
        self.send_response(status)
        self.send_header("Server", "Apache/2.4.41 (Ubuntu) PHP/7.4.3")
        self.send_header("X-Powered-By", "PHP/7.4.3")
        self.send_header("X-Victim-ID", "MegaCorp_Internal_Asset")
        self.end_headers()

    def do_GET(self):
        host = self.headers.get('Host', '')

        # --- Lógica de Virtual Hosts (Modo VHOST) ---
        vhosts = {
            "dev.megacorp-internal.local": "AMBIENTE DE DESENVOLVIMENTO: ACESSO PERMITIDO",
            "api.megacorp-internal.local": "API ENDPOINT: TOKEN REQUERIDO",
            "staging.megacorp-internal.local": "AMBIENTE DE HOMOLOGAÇÃO",
            "mail.megacorp-internal.local": "WEBMAIL SERVICE V1.2",
            "admin.megacorp-internal.local": "PAINEL DE CONTROLE DE INFRAESTRUTURA"
        }

        if host in vhosts:
            self.send_my_headers(200)
            self.wfile.write(vhosts[host].encode())
            return

        # --- Lógica de Diretórios (Modo DIR) ---
        if self.path == "/admin.php":
            self.send_my_headers(200)
            self.wfile.write(b"Welcome to Secret Admin Panel!")
        elif self.path == "/config" or self.path == "/backup":
            self.send_my_headers(403)
            # Resposta de 719 bytes para o seu filtro --hs
            padding = "A" * 700
            self.wfile.write(f"Forbidden Cluster {padding}".encode())
        else:
            self.send_my_headers(404)
            self.wfile.write(b"Not Found")

print("[*] Laboratório 1NN3RR00T Ativo")
print("[*] URLs: megacorp-internal.local | dev | api | staging | mail | admin")
HTTPServer(('0.0.0.0', 8080), VictimHandler).serve_forever()
