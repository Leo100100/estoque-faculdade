from services.estoque_service import EstoqueService

class ProdutoController:

    @staticmethod
    def salvar_produto(usuario_id, nome, quantidade, preco):

        return EstoqueService.cadastrar_produto(usuario_id, nome, quantidade, preco)

    @staticmethod
    def listar_produtos(usuario_id):

        return EstoqueService.listar_produtos(usuario_id)

    @staticmethod
    def remover_produto(produto_id, usuario_id):

        return EstoqueService.remover_produto(produto_id, usuario_id)

    @staticmethod
    def buscar_por_id(produto_id, usuario_id):

        return EstoqueService.buscar_por_id(produto_id, usuario_id)

    @staticmethod
    def atualizar_produto(produto_id, usuario_id, nome, quantidade, preco):
        
        try:
            quantidade = int(quantidade)
            preco = float(preco)
            return EstoqueService.atualizar_produto(
                produto_id, usuario_id, nome, quantidade, preco
            )
        except Exception as e:
            return False, f"Erro ao atualizar produto: {e}"
