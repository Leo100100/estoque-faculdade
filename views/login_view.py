import customtkinter as ctk
from tkinter import messagebox
from controllers.auth_controller import AuthController


class LoginView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Estoque — Login")
        self.geometry("400x480")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.usuario_logado_id = None
        self.usuario_logado_nome = None

        self._modo = "login"   # alterna entre "login" e "cadastro"

        self._construir_tela()

    # ── Construção da interface ──────────────────────────────────

    def _construir_tela(self):

        # Título
        ctk.CTkLabel(
            self,
            text="Sistema de Estoque",
            font=ctk.CTkFont(size=22, weight="bold")
        ).pack(pady=(30, 5))

        ctk.CTkLabel(
            self,
            text="Faça login para continuar",
            font=ctk.CTkFont(size=13),
            text_color="gray50"
        ).pack(pady=(0, 20))

        # Frame do formulário
        self._frame = ctk.CTkFrame(self, corner_radius=12)
        self._frame.pack(padx=40, fill="x")

        # Campo usuário
        ctk.CTkLabel(self._frame, text="Usuário:", anchor="w").pack(
            padx=20, pady=(20, 2), fill="x"
        )
        self.entry_usuario = ctk.CTkEntry(self._frame, placeholder_text="Digite seu usuário")
        self.entry_usuario.pack(padx=20, fill="x")

        # Campo senha
        ctk.CTkLabel(self._frame, text="Senha:", anchor="w").pack(
            padx=20, pady=(10, 2), fill="x"
        )
        self.entry_senha = ctk.CTkEntry(
            self._frame, placeholder_text="Digite sua senha", show="*"
        )
        self.entry_senha.pack(padx=20, fill="x")

        # Campo confirmar senha (somente no cadastro)
        self.label_confirmar = ctk.CTkLabel(
            self._frame, text="Confirmar senha:", anchor="w"
        )
        self.entry_confirmar = ctk.CTkEntry(
            self._frame, placeholder_text="Repita a senha", show="*"
        )

        # Botão principal
        self.btn_principal = ctk.CTkButton(
            self._frame,
            text="Entrar",
            command=self._acao_principal,
            height=40
        )
        self.btn_principal.pack(padx=20, pady=(20, 20), fill="x")

        # Rodapé — link para alternar modo
        self.label_alternar = ctk.CTkLabel(
            self,
            text="Não tem conta? Cadastre-se",
            cursor="hand2",
            text_color="#2980b9",
            font=ctk.CTkFont(size=12)
        )
        self.label_alternar.pack(pady=10)
        self.label_alternar.bind("<Button-1>", lambda e: self._alternar_modo())

        # Bind Enter
        self.bind("<Return>", lambda e: self._acao_principal())

    # ── Alternância login / cadastro ─────────────────────────────

    def _alternar_modo(self):
        if self._modo == "login":
            self._modo = "cadastro"
            self.title("Sistema de Estoque — Cadastro")
            self.geometry("400x540")
            self.btn_principal.configure(text="Cadastrar")
            self.label_alternar.configure(text="Já tem conta? Faça login")
            # Exibir campo confirmar senha
            self.label_confirmar.pack(
                in_=self._frame, padx=20, pady=(10, 2), fill="x",
                before=self.btn_principal
            )
            self.entry_confirmar.pack(
                in_=self._frame, padx=20, fill="x",
                before=self.btn_principal
            )
        else:
            self._modo = "login"
            self.title("Sistema de Estoque — Login")
            self.geometry("400x480")
            self.btn_principal.configure(text="Entrar")
            self.label_alternar.configure(text="Não tem conta? Cadastre-se")
            self.label_confirmar.pack_forget()
            self.entry_confirmar.pack_forget()

    # ── Ação principal (login ou cadastro) ───────────────────────

    def _acao_principal(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get()

        if self._modo == "login":
            ok, usuario_id, mensagem = AuthController.fazer_login(usuario, senha)
            if ok:
                self.usuario_logado_id = usuario_id
                self.usuario_logado_nome = usuario
                self.destroy()
            else:
                messagebox.showerror("Erro no login", mensagem)

        else:  # cadastro
            confirmar = self.entry_confirmar.get()
            ok, mensagem = AuthController.fazer_cadastro(usuario, senha, confirmar)
            if ok:
                messagebox.showinfo("Sucesso", mensagem + "\nAgora faça login.")
                self._alternar_modo()
                self.entry_usuario.delete(0, "end")
                self.entry_senha.delete(0, "end")
            else:
                messagebox.showerror("Erro no cadastro", mensagem)
