from config.database import conectar

class UsuarioModel:

    @staticmethod
    def buscar_por_usuario(usuario):

        conn = conectar()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, usuario, senha FROM usuarios WHERE usuario = %s",
                (usuario,)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def criar(usuario, senha):
        
        conn = conectar()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)",
                (usuario, senha)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
