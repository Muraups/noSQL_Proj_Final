# route.py
from flask import Blueprint, request, jsonify
from CONTROLLER.PessoaController import PessoaController

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
    data = request.json  # Ex.: {"id": int, "nome": str, ...}
    controller.criar_pessoa(data)
    return jsonify({"mensagem": "Pessoa inserida com sucesso!"}), 201

# PUT /pessoas/<pid>
@pessoa_bp.route("/pessoas/<int:pid>", methods=["PUT"])
def atualizar_pessoa(pid):
    data = request.json
    mod_count = controller.atualizar_pessoa(pid, data)
    if mod_count == 0:
        return jsonify({"erro": "Pessoa não encontrada!"}), 404
    return jsonify({"mensagem": "Pessoa atualizada com sucesso!"}), 200

# DELETE /pessoas/<pid>
@pessoa_bp.route("/pessoas/<int:pid>", methods=["DELETE"])
def deletar_pessoa(pid):
    del_count = controller.deletar_pessoa(pid)
    if del_count == 0:
        return jsonify({"erro": "Pessoa não encontrada!"}), 404
    return jsonify({"mensagem": "Pessoa deletada com sucesso!"}), 200
