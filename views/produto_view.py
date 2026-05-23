import customtkinter as ctk
from tkinter import messagebox, ttk, simpledialog
from controllers.produto_controller import ProdutoController


class ProdutoView(ctk.CTk):

    def __init__(self, usuario_id, usuario_nome):
        super().__init__()

        self.usuario_id = usuario_id
        self.usuario_nome = usuario_nome

        self.title(f"Sistema de Estoque — {usuario_nome}")
        self.geometry("800x580")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self._produto_id_selecionado = None

        # ── Cabeçalho ────────────────────────────────────────────
        frame_header = ctk.CTkFrame(self, fg_color="transparent")
        frame_header.pack(padx=20, pady=(10, 0), fill="x")

        ctk.CTkLabel(
            frame_header,
            text="Sistema de Estoque",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(side="left")

        ctk.CTkLabel(
            frame_header,
            text=f"Olá, {usuario_nome}",
            font=ctk.CTkFont(size=13),
            text_color="gray50"
        ).pack(side="left", padx=15)

        ctk.CTkButton(
            frame_header,
            text="Sair",
            command=self._sair,
            fg_color="gray40",
            hover_color="gray30",
            width=70,
            height=28
        ).pack(side="right")

        # ── Frame do formulário ──────────────────────────────────
        frame_form = ctk.CTkFrame(self)
        frame_form.pack(padx=20, pady=8, fill="x")

        ctk.CTkLabel(frame_form, text="Nome:").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.entry_nome = ctk.CTkEntry(frame_form, width=200)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Quantidade:").grid(
            row=0, column=2, padx=10, pady=5, sticky="w"
        )
        self.entry_quantidade = ctk.CTkEntry(frame_form, width=100)
        self.entry_quantidade.grid(row=0, column=3, padx=10, pady=5)

        ctk.CTkLabel(frame_form, text="Preço (R$):").grid(
            row=0, column=4, padx=10, pady=5, sticky="w"
        )
        self.entry_preco = ctk.CTkEntry(frame_form, width=100)
        self.entry_preco.grid(row=0, column=5, padx=10, pady=5)

        # ── Botões ───────────────────────────────────────────────
        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(pady=8)

        ctk.CTkButton(
            frame_botoes, text="Salvar",
            command=self.salvar_produto,
            fg_color="#27ae60", hover_color="#1e8449", width=130
        ).grid(row=0, column=0, padx=8)

        ctk.CTkButton(
            frame_botoes, text="Atualizar Lista",
            command=self.carregar_produtos,
            fg_color="#2980b9", hover_color="#1f618d", width=140
        ).grid(row=0, column=1, padx=8)

        ctk.CTkButton(
            frame_botoes, text="Remover",
            command=self.remover_produto,
            fg_color="#c0392b", hover_color="#922b21", width=120
        ).grid(row=0, column=2, padx=8)

        ctk.CTkButton(
            frame_botoes, text="Limpar",
            command=self.limpar_campos,
            fg_color="gray40", hover_color="gray30", width=100
        ).grid(row=0, column=3, padx=8)

        ctk.CTkButton(
            frame_botoes, text="Modificar",
            command=self.abrir_tela_modificacao,
            width=120
        ).grid(row=0, column=4, padx=8)

        # ── Tabela ───────────────────────────────────────────────
        frame_tabela = ctk.CTkFrame(self)
        frame_tabela.pack(padx=20, pady=10, fill="both", expand=True)

        colunas = ("ID", "Nome", "Quantidade", "Preço")
        self.tabela = ttk.Treeview(
            frame_tabela, columns=colunas, show="headings", height=12
        )

        for col in colunas:
            self.tabela.heading(col, text=col)

        self.tabela.column("ID", width=50, anchor="center")
        self.tabela.column("Nome", width=280)
        self.tabela.column("Quantidade", width=100, anchor="center")
        self.tabela.column("Preço", width=120, anchor="e")

        scroll = ttk.Scrollbar(frame_tabela, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scroll.set)
        self.tabela.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.tabela.bind("<<TreeviewSelect>>", self.ao_selecionar_linha)

        self.carregar_produtos()

    # ── Métodos ─────────────────────────────────────────────────

    def salvar_produto(self):
        nome = self.entry_nome.get().strip()
        quantidade = self.entry_quantidade.get().strip()
        preco = self.entry_preco.get().strip()

        ok, mensagem = ProdutoController.salvar_produto(
            self.usuario_id, nome, quantidade, preco
        )
        if ok:
            messagebox.showinfo("Sucesso", mensagem)
            self.limpar_campos()
            self.carregar_produtos()
        else:
            messagebox.showerror("Erro", mensagem)

    def carregar_produtos(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        produtos = ProdutoController.listar_produtos(self.usuario_id)
        for p in produtos:
            self.tabela.insert("", "end", values=(
                p[0], p[1], p[2], f"R$ {p[3]:.2f}"
            ))

    def remover_produto(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um produto para remover.")
            return

        valores = self.tabela.item(selecionado[0])["values"]
        produto_id = valores[0]
        nome = valores[1]

        if messagebox.askyesno("Confirmar", f"Deseja remover '{nome}'?"):
            ok, mensagem = ProdutoController.remover_produto(produto_id, self.usuario_id)
            if ok:
                messagebox.showinfo("Sucesso", mensagem)
                self.carregar_produtos()
                self.limpar_campos()
            else:
                messagebox.showerror("Erro", mensagem)

    def ao_selecionar_linha(self, event):
        selecionado = self.tabela.selection()
        if selecionado:
            valores = self.tabela.item(selecionado[0])["values"]
            self._produto_id_selecionado = valores[0]
            self.limpar_campos()
            self.entry_nome.insert(0, valores[1])
            self.entry_quantidade.insert(0, valores[2])
            preco_str = str(valores[3]).replace("R$ ", "")
            self.entry_preco.insert(0, preco_str)

    def limpar_campos(self):
        self.entry_nome.delete(0, "end")
        self.entry_quantidade.delete(0, "end")
        self.entry_preco.delete(0, "end")
        self._produto_id_selecionado = None

    def abrir_tela_modificacao(self):
        produto_id = simpledialog.askinteger(
            "Modificar Produto", "Digite o ID do produto:"
        )
        if not produto_id:
            return

        produto = ProdutoController.buscar_por_id(produto_id, self.usuario_id)
        if not produto:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        self.abrir_janela_edicao(produto)

    def abrir_janela_edicao(self, produto):
        janela = ctk.CTkToplevel(self)
        janela.title("Editar Produto")
        janela.geometry("400x300")

        produto_id = produto[0]

        ctk.CTkLabel(janela, text="Nome:").pack(pady=5)
        entry_nome = ctk.CTkEntry(janela, width=250)
        entry_nome.pack(pady=5)
        entry_nome.insert(0, produto[1])

        ctk.CTkLabel(janela, text="Quantidade:").pack(pady=5)
        entry_quantidade = ctk.CTkEntry(janela, width=250)
        entry_quantidade.pack(pady=5)
        entry_quantidade.insert(0, produto[2])

        ctk.CTkLabel(janela, text="Preço:").pack(pady=5)
        entry_preco = ctk.CTkEntry(janela, width=250)
        entry_preco.pack(pady=5)
        entry_preco.insert(0, produto[3])

        def salvar_alteracoes():
            nome = entry_nome.get().strip()
            quantidade = entry_quantidade.get().strip()
            preco = entry_preco.get().strip()
            ok, mensagem = ProdutoController.atualizar_produto(
                produto_id, self.usuario_id, nome, quantidade, preco
            )
            if ok:
                messagebox.showinfo("Sucesso", mensagem)
                janela.destroy()
                self.carregar_produtos()
            else:
                messagebox.showerror("Erro", mensagem)

        ctk.CTkButton(janela, text="Salvar", command=salvar_alteracoes).pack(pady=20)

    def _sair(self):
        """Fecha a janela principal e volta para o login."""
        self.destroy()
