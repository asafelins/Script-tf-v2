import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import automacao

class AutomacaoGUI:
    def __init__(self, root, licenca, automacao):
        self.root = root
        self.licenca = licenca
        self.automacao = automacao
        self.root.title("Script TF")
        self.root.iconbitmap("fotos/icon.ico")
        self.root.attributes("-topmost", True)
        self.root.minsize(300, 340)
        self.root.maxsize(300, 340)
        self.root.geometry("300x340")
        self.root.resizable(False, False)
        
        self.btn_iniciar = tk.Button(self.root, text="Iniciar", command=self.iniciar_automacao, width=8)
        self.btn_iniciar.pack(pady=3)
        
        self.btn_parar = tk.Button(self.root, text="Parar", command=self.parar_simples, state=tk.DISABLED, width=8)
        self.btn_parar.pack(pady=3)
        
        self.texto_info = tk.Label(self.root, text="Mantenha pressionada a tecla ctrl para parar.", fg="red")
        self.texto_info.pack(pady=5)
        
        self.txt_output = scrolledtext.ScrolledText(self.root, width=100, height=15)
        self.txt_output.pack(pady=5)
        
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)

    def iniciar_automacao(self):
        self.txt_output.delete(1.0, tk.END)
        self.automacao.iniciar_automacao()
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_parar.config(state=tk.NORMAL)

    def parar_automacao(self):
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_parar.config(state=tk.DISABLED)
    
    def parar_simples(self):
        self.automacao.parar_automacao()


    def fechar_janela(self):
        self.parar_automacao()
        self.root.destroy()

    def write(self, text):
        if not text.endswith('\n'):
            text += '\n'

        current_time = datetime.now().strftime("%H:%M:%S")
        formatted_text = f"[{current_time}] {text}"
        self.txt_output.insert(tk.END, formatted_text)
        self.txt_output.see(tk.END)
