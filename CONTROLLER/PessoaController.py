from MODEL.PessoaModel import Pessoa, PessoaModel

class PessoaController:
    def __init__(self):
        self.model = PessoaModel()

    def listar_pessoas(self):
        return self.model.listar_todos()

    def criar_pessoa(self, data):
        pessoa = Pessoa(
            pid=data["id"],
            nome=data["nome"],
            fone=data["fone"],
            aniversario=data["aniversario"]
        )
        self.model.criar_pessoa(pessoa)

    def atualizar_pessoa(self, pid, data):
        pessoa = Pessoa(
            pid=pid,
            nome=data["nome"],
            fone=data["fone"],
            aniversario=data["aniversario"]
        )
        return self.model.atualizar_pessoa(pessoa)

    def deletar_pessoa(self, pid):
        return self.model.deletar_pessoa(pid)
