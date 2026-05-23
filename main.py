from views.login_view import LoginView
from views.produto_view import ProdutoView


if __name__ == "__main__":
    while True:
     
        login = LoginView()
        login.mainloop()


        if login.usuario_logado_id is None:
            break

        app = ProdutoView(login.usuario_logado_id, login.usuario_logado_nome)
        app.mainloop()


