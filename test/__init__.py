from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
CAMINHO = f"{os.path.dirname(__file__)}\\Base\\pedidos.json"
def ler_pedidos():
    try:
        with open(CAMINHO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_pedidos(pedidos):
    with open(CAMINHO, 'w') as f:
        json.dump(pedidos, f)

@app.route('/pedido', methods=['POST'])
def criar_pedido():
    pedido = request.get_json()
    pedidos = ler_pedidos()
    pedidos.append(pedido)
    salvar_pedidos(pedidos)
    return jsonify({'id': len(pedidos) - 1, 'status': 'Pedido criado'}), 201

@app.route('/pedido/<int:id>', methods=['PUT'])
def editar_pedido(id):
    pedido = request.get_json()
    pedidos = ler_pedidos()
    if 0 <= id < len(pedidos):
        pedidos[id] = pedido
        salvar_pedidos(pedidos)
        return jsonify({'status': 'Pedido atualizado'}), 200
    else:
        return jsonify({'error': 'Pedido não encontrado'}), 404

@app.route('/pedido/<int:id>', methods=['GET'])
def consultar_pedido_id(id):
    pedidos = ler_pedidos()
    if 0 <= id < len(pedidos):
        return jsonify(pedidos[id]), 200
    else:
        return jsonify({'error': 'Pedido não encontrado'}), 404
    
@app.route('/pedido', methods=['GET'])
def consultar_pedido():
    return jsonify(ler_pedidos()), 200


if __name__ == '__main__':
    app.run(debug=True)
