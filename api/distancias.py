from flask import Blueprint, jsonify



distancias_bp = Blueprint('distancias', __name__, url_prefix='/distancias')

distancias = ["Até 1Km", "Até 5Km", "Até 10Km"]

@distancias_bp.route('/', methods=['GET'])
def listar_distancias():
    return jsonify(distancias)
