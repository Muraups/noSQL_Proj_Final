from config.database import db

class Servico:
    def __init__(self, sid, nome, descricao, valor):
        self.id = sid
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class ServicoModel:
    def __init__(self):
        self.collection = db.servicos

    def listar_todos(self):
        return list(self.collection.find({}, {"_id": 0}))

    def criar_servico(self, servico):
        self.collection.insert_one(servico.__dict__)

    def atualizar_servico(self, servico):
        result = self.collection.update_one(
            {"id": servico.id},
            {"$set": servico.__dict__}
        )
        return result.modified_count

    def deletar_servico(self, sid):
        result = self.collection.delete_one({"id": sid})
        return result.deleted_count
