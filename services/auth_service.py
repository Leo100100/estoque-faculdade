from models.usuario_model import UsuarioModel

class AuthService:

    @staticmethod
    def login(usuario, senha):

        if not usuario or not usuario.strip():
            return False, None, "Informe o usuário."
        if not senha or not senha.strip():
            return False, None, "Informe a senha."

        registro = UsuarioModel.buscar_por_usuario(usuario.strip())
        if not registro:
            return False, None, "Usuário não encontrado."

        usuario_id, _, senha_salva = registro
        if senha != senha_salva:
            return False, None, "Senha incorreta."

        return True, usuario_id, "Login realizado com sucesso!"

    @staticmethod
    def cadastrar(usuario, senha, confirmar_senha):
        
        if not usuario or not usuario.strip():
            return False, "Informe o nome de usuário."
        if len(usuario.strip()) < 3:
            return False, "O usuário deve ter pelo menos 3 caracteres."
        if not senha or len(senha) < 4:
            return False, "A senha deve ter pelo menos 4 caracteres."
        if senha != confirmar_senha:
            return False, "As senhas não coincidem."

        existente = UsuarioModel.buscar_por_usuario(usuario.strip())
        if existente:
            return False, "Este nome de usuário já está em uso."

        sucesso = UsuarioModel.criar(usuario.strip(), senha)
        if sucesso:
            return True, "Cadastro realizado com sucesso!"
        return False, "Erro ao criar usuário no banco de dados."
