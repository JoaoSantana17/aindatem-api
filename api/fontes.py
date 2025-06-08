from flask import Blueprint, jsonify



fontes_bp = Blueprint('fontes', __name__, url_prefix='/fontes')

fontes = ["Comunitária", "Oficial"]

@fontes_bp.route('/', methods=['GET'])
def listar_fontes():
    return jsonify(fontes)
