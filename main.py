import customtkinter as ctk
from tela_tkinter import JanelaPrincipal

# Configuração inicial do customtkinter
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

def main():
    app = JanelaPrincipal()
    app.mainloop()

if __name__ == "__main__":
    main()
