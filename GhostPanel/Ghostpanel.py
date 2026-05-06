import customtkinter as ctk
import psutil
import socket
import platform
import threading
import time
import random
import string
from ping3 import ping
from tkinter import messagebox

# =========================
# CONFIGURAÇÃO
# =========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("1100x700")
app.title("GhostPanel")

# =========================
# FUNÇÕES SISTEMA
# =========================
def atualizar_sistema():
    while True:
        try:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            disco = psutil.disk_usage('/').percent
            sistema = platform.system()
            release = platform.release()

            hostname = socket.gethostname()
            ip_local = socket.gethostbyname(hostname)

            cpu_label.configure(text=f"CPU: {cpu}%")
            ram_label.configure(text=f"RAM: {ram}%")
            disco_label.configure(text=f"DISCO: {disco}%")
            sistema_label.configure(text=f"SISTEMA: {sistema} {release}")
            ip_label.configure(text=f"IP LOCAL: {ip_local}")

            cpu_bar.set(cpu / 100)
            ram_bar.set(ram / 100)
            disco_bar.set(disco / 100)

            logs.insert("end", f"[INFO] Sistema atualizado | CPU {cpu}% | RAM {ram}%\n")
            logs.see("end")

        except Exception as e:
            logs.insert("end", f"ERRO: {e}\n")

        time.sleep(2)

# =========================
# GERADOR SENHA
# =========================
def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(16))

    senha_entry.delete(0, "end")
    senha_entry.insert(0, senha)

# =========================
# COPIAR SENHA
# =========================
def copiar_senha():
    senha = senha_entry.get()

    if senha:
        app.clipboard_clear()
        app.clipboard_append(senha)
        messagebox.showinfo("GhostPanel", "Senha copiada!")

# =========================
# EXECUTAR COMANDO
# =========================
def executar_comando():
    comando = comando_entry.get()

    try:
        import subprocess

        resultado = subprocess.check_output(comando, shell=True, text=True)

        terminal_box.delete("1.0", "end")
        terminal_box.insert("end", resultado)

        logs.insert("end", f"[CMD] {comando}\n")

    except Exception as e:
        terminal_box.delete("1.0", "end")
        terminal_box.insert("end", str(e))

# =========================
# PING
# =========================
def testar_ping():
    host = ping_entry.get()

    try:
        resposta = ping(host)

        if resposta:
            ping_result.configure(text=f"PING: {round(resposta * 1000)} ms")
            logs.insert("end", f"[PING] {host} online\n")
        else:
            ping_result.configure(text="HOST OFFLINE")
            logs.insert("end", f"[PING] {host} offline\n")

    except:
        ping_result.configure(text="ERRO")

# =========================
# TÍTULO
# =========================
titulo = ctk.CTkLabel(
    app,
    text="GHOSTPANEL",
    font=("Consolas", 35, "bold"),
    text_color="#00ff66"
)

titulo.pack(pady=10)

# =========================
# FRAME PRINCIPAL
# =========================
main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

# =========================
# LADO ESQUERDO
# =========================
left_frame = ctk.CTkFrame(main_frame, width=350)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# CPU
cpu_label = ctk.CTkLabel(left_frame, text="CPU: 0%", font=("Consolas", 18))
cpu_label.pack(pady=10)

cpu_bar = ctk.CTkProgressBar(left_frame, width=250)
cpu_bar.pack()

# RAM
ram_label = ctk.CTkLabel(left_frame, text="RAM: 0%", font=("Consolas", 18))
ram_label.pack(pady=10)

ram_bar = ctk.CTkProgressBar(left_frame, width=250)
ram_bar.pack()

# DISCO
disco_label = ctk.CTkLabel(left_frame, text="DISCO: 0%", font=("Consolas", 18))
disco_label.pack(pady=10)

disco_bar = ctk.CTkProgressBar(left_frame, width=250)
disco_bar.pack()

# SISTEMA
sistema_label = ctk.CTkLabel(left_frame, text="SISTEMA", font=("Consolas", 16))
sistema_label.pack(pady=15)

# IP
ip_label = ctk.CTkLabel(left_frame, text="IP", font=("Consolas", 16))
ip_label.pack(pady=5)

# =========================
# GERADOR SENHA
# =========================
senha_title = ctk.CTkLabel(left_frame, text="GERADOR DE SENHA", font=("Consolas", 18, "bold"))
senha_title.pack(pady=15)

senha_entry = ctk.CTkEntry(left_frame, width=250, height=40)
senha_entry.pack(pady=5)

btn_gerar = ctk.CTkButton(left_frame, text="GERAR", command=gerar_senha)
btn_gerar.pack(pady=5)

btn_copiar = ctk.CTkButton(left_frame, text="COPIAR", command=copiar_senha)
btn_copiar.pack(pady=5)

# =========================
# CENTRO
# =========================
center_frame = ctk.CTkFrame(main_frame)
center_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

terminal_title = ctk.CTkLabel(center_frame, text="TERMINAL", font=("Consolas", 22, "bold"))
terminal_title.pack(pady=10)

comando_entry = ctk.CTkEntry(center_frame, width=500, height=40)
comando_entry.pack(pady=10)

executar_btn = ctk.CTkButton(center_frame, text="EXECUTAR", command=executar_comando)
executar_btn.pack(pady=5)

terminal_box = ctk.CTkTextbox(center_frame, width=600, height=300, font=("Consolas", 14))
terminal_box.pack(pady=10)

# =========================
# PING
# =========================
ping_title = ctk.CTkLabel(center_frame, text="TESTE DE PING", font=("Consolas", 18, "bold"))
ping_title.pack(pady=10)

ping_entry = ctk.CTkEntry(center_frame, placeholder_text="8.8.8.8", width=250)
ping_entry.pack(pady=5)

ping_btn = ctk.CTkButton(center_frame, text="TESTAR", command=testar_ping)
ping_btn.pack(pady=5)

ping_result = ctk.CTkLabel(center_frame, text="---", font=("Consolas", 16))
ping_result.pack(pady=5)

# =========================
# LADO DIREITO
# =========================
right_frame = ctk.CTkFrame(main_frame, width=250)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

logs_title = ctk.CTkLabel(right_frame, text="LOGS", font=("Consolas", 22, "bold"))
logs_title.pack(pady=10)

logs = ctk.CTkTextbox(right_frame, width=250, height=500, font=("Consolas", 12))
logs.pack(pady=10)

logs.insert("end", "GhostPanel iniciado...\n")

# =========================
# THREAD SISTEMA
# =========================
thread = threading.Thread(target=atualizar_sistema)
thread.daemon = True
thread.start()

# =========================
# LOOP
# =========================
app.mainloop()
