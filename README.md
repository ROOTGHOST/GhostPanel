# GHOSTPANEL — Projeto Python para Kali Linux

## Ideia do Projeto

O GhostPanel é um painel cyberpunk feito em Python para Kali Linux.

Ele funciona como um painel de monitoramento real do sistema, com visual hacker.

---

# Funções do GhostPanel

## Sistema

* Uso de CPU em tempo real
* Uso de RAM
* Uso de disco
* Temperatura do sistema
* Tempo ligado do PC
* Informações do Linux

## Rede

* Mostrar IP local
* Mostrar IP público
* Ping em hosts
* Monitor de internet
* Verificar portas abertas localmente
* Scanner simples da rede local

## Interface

* Tema cyberpunk
* Terminal fake animado
* Logs em tempo real
* Visual vermelho/preto/verde
* Efeitos estilo Matrix

## Ferramentas úteis

* Gerador de senha
* Bloco de notas
* Executor de comandos Linux
* Histórico de comandos
* Informações do hardware

## Extras

* Login inicial
* Sons cyberpunk
* Splash screen
* Sistema de plugins
* Modo tela cheia
* Dashboard moderno

---

# Estrutura do Projeto

```bash
GhostPanel/
│
├── main.py
├── requirements.txt
├── assets/
│   ├── logo.png
│   ├── sounds/
│   └── wallpapers/
│
├── modules/
│   ├── system_info.py
│   ├── network_tools.py
│   ├── password_generator.py
│   ├── terminal.py
│   └── scanner.py
│
├── themes/
│   └── cyber.theme
│
└── README.md
```

---

# Bibliotecas

## Instalar no Kali

```bash
sudo apt update
sudo apt install python3-pip python3-tk -y

pip3 install customtkinter
pip3 install psutil
pip3 install requests
pip3 install pillow
pip3 install netifaces
pip3 install ping3
```

---

# Como Rodar

```bash
python3 main.py
```

---

# Interface Recomendada

## Visual:

* Fundo preto
* Bordas vermelhas
* Texto verde neon
* Fonte Consolas
* Animações suaves

---

# Funções reais em Python

## CPU e RAM

```python
import psutil

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

print(cpu)
print(ram)
```

---

## IP Local

```python
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(ip)
```

---

## Ping

```python
from ping3 import ping

resposta = ping('8.8.8.8')
print(resposta)
```

---

## Scanner simples da rede local

```python
import socket

alvo = '192.168.0.1'

for porta in [21,22,80,443]:
    s = socket.socket()
    s.settimeout(0.5)

    if s.connect_ex((alvo, porta)) == 0:
        print(f'Porta aberta: {porta}')
```

---

# Ideias Futuras

## GhostPanel PRO

* Chat integrado
* Sistema de contas
* Dashboard web
* Painel remoto
* Atualizador automático
* Temas personalizados
* Overlay estilo hacker

---

# README GitHub

## Nome

GHOSTPANEL

## Descrição

Cyberpunk Linux Monitoring Dashboard built with Python.

## Tags

```txt
python
kali-linux
linux
cyberpunk
system-monitor
network
security
customtkinter
```

---

# Dica Importante

Use:

* customtkinter para interface moderna
* threading para atualizar sem travar
* subprocess para comandos Linux
* psutil para monitoramento

---

# Melhor parte

Esse projeto realmente funciona no Kali Linux.

Você só instala as bibliotecas e executa.

Não precisa compilar nem configurar servidor.
