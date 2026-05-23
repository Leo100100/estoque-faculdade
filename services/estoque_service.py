"""
Camada de serviço: regras de negócio do estoque.
O Controller chama o Service, que chama o Model.
Aqui ficam validações e lógicas mais complexas.
"""

from models.produto_model import ProdutoModel

class EstoqueService:

    @staticmethod
    def validar_produto(nome, quantidade, preco):
        if not nome or not nome.strip():
            return False, "O nome do produto não pode ser vazio."
        if not quantidade or not str(quantidade).strip():
            return False, "A quantidade não pode ser vazia."
        if not preco or not str(preco).strip():
            return False, "O preço não pode ser vazio."
        try:
            qtd = int(quantidade)
            if qtd < 0:
                return False, "A quantidade não pode ser negativa."
        except ValueError:
            return False, "A quantidade deve ser um número inteiro."
        try:
            p = float(str(preco).replace(",", "."))
            if p < 0:
                return False, "O preço não pode ser negativo."
        except ValueError:
            return False, "O preço deve ser um número válido."
        return True, ""

    @staticmethod
    def cadastrar_produto(usuario_id, nome, quantidade, preco):

        preco = str(preco).replace(",", ".")
        ok, erro = EstoqueService.validar_produto(nome, quantidade, preco)
        if not ok:
            return False, erro
        sucesso = ProdutoModel.salvar(usuario_id, nome, quantidade, preco)
        if sucesso:
            return True, "Produto cadastrado com sucesso!"
        return False, "Erro ao salvar no banco de dados."

    @staticmethod
    def listar_produtos(usuario_id):

        return ProdutoModel.listar(usuario_id)

    @staticmethod
    def remover_produto(produto_id, usuario_id):

        sucesso = ProdutoModel.deletar(produto_id, usuario_id)
        if sucesso:
            return True, "Produto removido com sucesso!"
        return False, "Erro ao remover o produto."

    @staticmethod
    def buscar_por_id(produto_id, usuario_id):

        return ProdutoModel.buscar_por_id(produto_id, usuario_id)

    @staticmethod
    def atualizar_produto(produto_id, usuario_id, nome, quantidade, preco):

        ok, erro = EstoqueService.validar_produto(nome, quantidade, preco)
        if not ok:
            return False, erro
        sucesso = ProdutoModel.atualizar(produto_id, usuario_id, nome, quantidade, preco)
        if sucesso:
            return True, "Produto atualizado com sucesso!"
        return False, "Erro ao atualizar o produto."
