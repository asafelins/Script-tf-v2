import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timezone

# Importando as classes dos outros arquivos
from licenca import Licenca
from automacao import Automacao
from interface import AutomacaoGUI

if __name__ == "__main__":
    hwid_esperado = "737c252ca6be6bb9c8eef707f2e769d0899d1486fedbbf7ab7f350a3e4501cb6"
    data_criacao_licenca = datetime(2024, 5, 11, tzinfo=timezone.utc)
    
    # Instanciando as classes
    licenca = Licenca(hwid_esperado, data_criacao_licenca)
    
    if licenca.verificar_licenca():
        print("Licença válida.")
        root = tk.Tk()
        app = AutomacaoGUI(root, licenca, None) 
        automacao = Automacao(app)
        app.automacao = automacao
        root.mainloop()
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Licença Inválida", "Sua licença está inválida ou expirada.")
        root.quit()