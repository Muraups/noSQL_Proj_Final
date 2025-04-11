from flask import Blueprint, request, jsonify
from CONTROLLER.PessoaController import PessoaController
from CONTROLLER.ProdutoController import ProdutoController
from CONTROLLER.ServicoController import ServicoController


pessoa_bp = Blueprint("pessoa_bp", __name__)
controller = PessoaController()

# GET /pessoas
@pessoa_bp.route("/pessoas", methods=["GET"])
def listar_pessoas():
    pessoas = controller.listar_pessoas()
    return jsonify(pessoas), 200

# POST /pessoas
@pessoa_bp.route("/pessoas", methods=["POST"])
def criar_pessoa():
    data = request.get_json()  # Corrigido aqui
    controller.criar_pessoa(data)
    return jsonify({"mensagem": "Pessoa inserida com sucesso!"}), 201

# PUT /pessoas/<pid>
@pessoa_bp.route("/pessoas/<int:pid>", methods=["PUT"])
def atualizar_pessoa(pid):
    data = request.get_json()
    mod_count = controller.atualizar_pessoa(pid, data)
    if mod_count == 0:
        return jsonify({"erro": "Pessoa não encontrada!"}), 404
    return jsonify({"mensagem": "Pessoa atualizada com sucesso!"}), 200

# DELETE /pessoas/<int:pid>
@pessoa_bp.route("/pessoas/<int:pid>", methods=["DELETE"])
def deletar_pessoa(pid):
    del_count = controller.deletar_pessoa(pid)
    if del_count == 0:
        return jsonify({"erro": "Pessoa não encontrada!"}), 404
    return jsonify({"mensagem": "Pessoa deletada com sucesso!"}), 200

produto_controller = ProdutoController()
servico_controller = ServicoController()

# Rotas Produto
@pessoa_bp.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produto_controller.listar_produtos()), 200

@pessoa_bp.route("/produtos", methods=["POST"])
def criar_produto():
    data = request.json
    produto_controller.criar_produto(data)
    return jsonify({"mensagem": "Produto criado com sucesso!"}), 201

@pessoa_bp.route("/produtos/<int:pid>", methods=["PUT"])
def atualizar_produto(pid):
    data = request.json
    count = produto_controller.atualizar_produto(pid, data)
    if count == 0:
        return jsonify({"erro": "Produto não encontrado!"}), 404
    return jsonify({"mensagem": "Produto atualizado!"}), 200

@pessoa_bp.route("/produtos/<int:pid>", methods=["DELETE"])
def deletar_produto(pid):
    count = produto_controller.deletar_produto(pid)
    if count == 0:
        return jsonify({"erro": "Produto não encontrado!"}), 404
    return jsonify({"mensagem": "Produto deletado!"}), 200

# Rotas Serviço
@pessoa_bp.route("/servicos", methods=["GET"])
def listar_servicos():
    return jsonify(servico_controller.listar_servicos()), 200

@pessoa_bp.route("/servicos", methods=["POST"])
def criar_servico():
    data = request.json
    servico_controller.criar_servico(data)
    return jsonify({"mensagem": "Serviço criado com sucesso!"}), 201

@pessoa_bp.route("/servicos/<int:sid>", methods=["PUT"])
def atualizar_servico(sid):
    data = request.json
    count = servico_controller.atualizar_servico(sid, data)
    if count == 0:
        return jsonify({"erro": "Serviço não encontrado!"}), 404
    return jsonify({"mensagem": "Serviço atualizado!"}), 200

@pessoa_bp.route("/servicos/<int:sid>", methods=["DELETE"])
def deletar_servico(sid):
    count = servico_controller.deletar_servico(sid)
    if count == 0:
        return jsonify({"erro": "Serviço não encontrado!"}), 404
    return jsonify({"mensagem": "Serviço deletado!"}), 200
