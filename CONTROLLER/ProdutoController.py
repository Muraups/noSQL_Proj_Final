from MODEL.ProdutoModel import Produto, ProdutoModel

class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()

    def listar_produtos(self):
        return self.model.listar_todos()

    def criar_produto(self, data):
        produto = Produto(
            pid=data["id"],
            nome=data["nome"],
            preco=data["preco"],
            estoque=data["estoque"]
        )
        self.model.criar_produto(produto)

    def atualizar_produto(self, pid, data):
        produto = Produto(
            pid=pid,
            nome=data["nome"],
            preco=data["preco"],
            estoque=data["estoque"]
        )
        return self.model.atualizar_produto(produto)

    def deletar_produto(self, pid):
        return self.model.deletar_produto(pid)
