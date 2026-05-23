from services.auth_service import AuthService

class AuthController:

    @staticmethod
    def fazer_login(usuario, senha):

        return AuthService.login(usuario, senha)

    @staticmethod
    def fazer_cadastro(usuario, senha, confirmar_senha):
       
        return AuthService.cadastrar(usuario, senha, confirmar_senha)
