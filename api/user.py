from flask import Blueprint, request, jsonify

user_bp = Blueprint('user', __name__, url_prefix='/usuario')

usuarios = [
    {"email": "joao.santana@mail.com", "senha": "joao123@", "nome": "João Santana"},
    {"email": "yuri.ferreira@mail.com", "senha": "yuri123@", "nome": "Yuri Ferreira"},
    {"email": "jun.conheci@mail.com", "senha": "jun123@", "nome": "Jun Conheci"},
    {"email": "usermail@gmail.com", "senha": "userpassword01", "nome": "Usuário Teste"},
]

@user_bp.route('/', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    for user in usuarios:
        if user['email'] == email and user['senha'] == senha:
            return jsonify({
                "message": "Login realizado com sucesso!",
                "email": user['email'],
                "nome": user['nome']
            }), 200

    return jsonify({"error": "Credenciais inválidas"}), 401

@user_bp.route('/', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    nome = data.get('nome')

    if not email or not senha or not nome:
        return jsonify({"error": "Email, senha e nome são obrigatórios"}), 400

    for user in usuarios:
        if user['email'] == email:
            return jsonify({"error": "Usuário já cadastrado"}), 409

    novo_usuario = {"email": email, "senha": senha, "nome": nome}
    usuarios.append(novo_usuario)

    return jsonify({"message": "Usuário cadastrado com sucesso!", "nome": nome}), 201


