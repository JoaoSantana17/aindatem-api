from flask import Blueprint, request, jsonify
import random
import re

recursos_bp = Blueprint('recursos', __name__, url_prefix='/recursos')

def gerar_coordenadas():
    lat = round(-23.5 + random.uniform(-0.05, 0.05), 6)
    lon = round(-46.6 + random.uniform(-0.05, 0.05), 6)
    return lat, lon

locais = [
    {
        "nome": "Hospital Central",
        "recurso": "Medicamento",
        "fonte": "Oficial",
        "distancia": "Até 5Km",
        "latitude": -23.5505,
        "longitude": -46.6333,
        "endereco": "Av. Central, 100",
        "contato": "(11) 3333-4444",
        "horario": "24h"
    },
    {
        "nome": "Centro Comunitário",
        "recurso": "Abrigo",
        "fonte": "Comunitária",
        "distancia": "Até 5Km",
        "latitude": -23.5567,
        "longitude": -46.6251,
        "endereco": "Rua da União, 45",
        "contato": "(11) 2222-1111",
        "horario": "08h às 20h"
    },
    {
        "nome": "Mercado Solidário",
        "recurso": "Alimento",
        "fonte": "Comunitária",
        "distancia": "Até 1Km",
        "latitude": -23.5523,
        "longitude": -46.6288,
        "endereco": "Av. das Nações, 789",
        "contato": "(11) 9999-1234",
        "horario": "07h às 22h"
    },
    {
        "nome": "Farmácia Popular",
        "recurso": "Medicamento",
        "fonte": "Comunitária",
        "distancia": "Até 5Km",
        "latitude": -23.5472,
        "longitude": -46.6395,
        "endereco": "Rua Popular, 123",
        "contato": "(11) 4002-8922",
        "horario": "08h às 18h"
    },
    {
        "nome": "Escola Municipal",
        "recurso": "Higiene",
        "fonte": "Oficial",
        "distancia": "Até 10Km",
        "latitude": -23.5411,
        "longitude": -46.6453,
        "endereco": "Rua das Flores, 456",
        "contato": "(11) 3232-5678",
        "horario": "07h às 17h"
    },
    {
        "nome": "Associação de Bairro",
        "recurso": "Água",
        "fonte": "Comunitária",
        "distancia": "Até 1Km",
        "latitude": -23.5378,
        "longitude": -46.6369,
        "endereco": "Praça da Paz, 12",
        "contato": "(11) 8765-4321",
        "horario": "09h às 19h"
    }
]

@recursos_bp.route('/', methods=['GET'])
def listar_locais():
    recurso_param = request.args.get('recurso')
    fonte_param = request.args.get('fonte')
    distancia_param = request.args.get('distancia')

    resultado = locais


    if recurso_param:
        resultado = [r for r in resultado if r['recurso'].lower() == recurso_param.lower()]
    if fonte_param:
        resultado = [r for r in resultado if r['fonte'].lower() == fonte_param.lower()]
    if distancia_param:
        resultado = [r for r in resultado if r['distancia'].lower() == distancia_param.lower()]

    def extrair_km(dist: str):
        match = re.search(r'\d+', dist)
        return int(match.group()) if match else 999

    resultado.sort(key=lambda r: extrair_km(r['distancia']))

    return jsonify(resultado), 200

@recursos_bp.route('/', methods=['POST'])
def cadastrar_local():
    data = request.get_json()

    required_fields = ['nome', 'recurso', 'fonte', 'distancia']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Dados incompletos"}), 400

    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude is None or longitude is None:
        latitude, longitude = gerar_coordenadas()

    novo_local = {
        "nome": data['nome'],
        "recurso": data['recurso'],
        "fonte": data['fonte'],
        "distancia": data['distancia'],
        "latitude": latitude,
        "longitude": longitude
    }

    if 'endereco' in data:
        novo_local['endereco'] = data['endereco']
    if 'contato' in data:
        novo_local['contato'] = data['contato']
    if 'horario' in data:
        novo_local['horario'] = data['horario']

    locais.append(novo_local)
    return jsonify({"message": "Local cadastrado com sucesso!", "local": novo_local}), 201
