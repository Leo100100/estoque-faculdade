from config.database import conectar

class ProdutoModel:

    @staticmethod
    def salvar(usuario_id, nome, quantidade, preco):

        conn = conectar()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            sql = """INSERT INTO produtos (usuario_id, nome, quantidade, preco)
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql, (usuario_id, nome, int(quantidade), float(preco)))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar produto: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar(usuario_id):

        conn = conectar()
        if not conn:
            return []
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nome, quantidade, preco FROM produtos WHERE usuario_id = %s",
                (usuario_id,)
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def deletar(produto_id, usuario_id):

        conn = conectar()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s AND usuario_id = %s",
                (produto_id, usuario_id)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def atualizar(produto_id, usuario_id, nome, quantidade, preco):

        conn = conectar()
        if not conn:
            return False
        try:
            cursor = conn.cursor()
            sql = """UPDATE produtos SET nome=%s, quantidade=%s, preco=%s
                     WHERE id=%s AND usuario_id=%s"""
            cursor.execute(sql, (nome, int(quantidade), float(preco), produto_id, usuario_id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def buscar_por_id(produto_id, usuario_id):
        
        conn = conectar()
        if not conn:
            return None
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nome, quantidade, preco FROM produtos WHERE id = %s AND usuario_id = %s",
                (produto_id, usuario_id)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar produto: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
