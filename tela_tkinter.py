import customtkinter as ctk

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração inicial
        self.title("Tela de Login")
        self.geometry("300x200")
        self.resizable(False, False)

        # Frame para o conteúdo do login
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(padx=20, pady=20, fill="both", expand=True)

        # Widgets do frame de login
        self.label_usuario = ctk.CTkLabel(self.frame_login, text="Usuário")
        self.label_usuario.pack(pady=(10, 5))

        self.entry_usuario = ctk.CTkEntry(self.frame_login)
        self.entry_usuario.pack(pady=(0, 10), fill="x")

        self.label_senha = ctk.CTkLabel(self.frame_login, text="Senha")
        self.label_senha.pack(pady=(10, 5))

        self.entry_senha = ctk.CTkEntry(self.frame_login, show="*")
        self.entry_senha.pack(pady=(0, 10), fill="x")

        self.button_login = ctk.CTkButton(self.frame_login, text="Entrar", command=self.verificar_login)
        self.button_login.pack(pady=(10, 0))

        self.label_resultado = ctk.CTkLabel(self.frame_login, text="")
        self.label_resultado.pack(pady=(10, 0))

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        # Lógica de autenticação pode ser adicionada aqui
        if usuario == "admin" and senha == "senha":
            self.label_resultado.config(text="Login bem-sucedido!", text_color="green")
        else:
            self.label_resultado.config(text="Usuário ou senha incorretos.", text_color="red")
