from config.database import db

class Produto:
    def __init__(self, pid, nome, preco, estoque):
        self.id = pid
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class ProdutoModel:
    def __init__(self):
        self.collection = db.produtos

    def listar_todos(self):
        return list(self.collection.find({}, {"_id": 0}))

    def criar_produto(self, produto):
        self.collection.insert_one(produto.__dict__)

    def atualizar_produto(self, produto):
        result = self.collection.update_one(
            {"id": produto.id},
            {"$set": produto.__dict__}
        )
        return result.modified_count

    def deletar_produto(self, pid):
        result = self.collection.delete_one({"id": pid})
        return result.deleted_count
