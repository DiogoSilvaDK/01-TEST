from flask import Flask,jsonify,request
import os
import json

app = Flask(__name__)

LIVROS = json.load(open(f"{os.path.dirname(__file__)}\\Base\\Livros.json","r",encoding='utf-8'))

# Consutar(Todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(LIVROS)

# Consutar(ID)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in LIVROS:
        if livro.get('id') == id:
            return jsonify(livro)
        
#Editar(ID) 
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterados = request.get_json()
    for indice,livro in enumerate(LIVROS):
        if livro.get('id') == id:
            LIVROS[indice].update(livro_alterados)
            return jsonify(LIVROS[indice])

app.run(port=5000,host='localhost',debug=True)