from MODEL.ServicoModel import Servico, ServicoModel

class ServicoController:
    def __init__(self):
        self.model = ServicoModel()

    def listar_servicos(self):
        return self.model.listar_todos()

    def criar_servico(self, data):
        servico = Servico(
            sid=data["id"],
            nome=data["nome"],
            descricao=data["descricao"],
            valor=data["valor"]
        )
        self.model.criar_servico(servico)

    def atualizar_servico(self, sid, data):
        servico = Servico(
            sid=sid,
            nome=data["nome"],
            descricao=data["descricao"],
            valor=data["valor"]
        )
        return self.model.atualizar_servico(servico)

    def deletar_servico(self, sid):
        return self.model.deletar_servico(sid)
