from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Função para obter todas as cidades do Brasil ordenadas alfabeticamente por nome
def lista_cidades():
    try:
        url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
        resposta = requests.get(url)
        if resposta.status_code == 200: #response.status_code retorna um número que indica o status (200 é OK, 404 é Not Found)
            cidades = resposta.json()
            nomes_cidades = sorted([cidade['nome'] for cidade in cidades])
            return jsonify(nomes_cidades)
        else:
            return jsonify({"erro": "Falha ao buscar as cidades"})
    except Exception as e:
        return jsonify({"erro": str(e)})

# Função para obter as cidades de um estado específico ordenadas alfabeticamente por nome
def lista_por_estado(estado):
    try:
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            cidades = resposta.json()
            nomes_cidades = sorted([cidade['nome'] for cidade in cidades])
            return jsonify(nomes_cidades)
        else:
            return jsonify({"erro": f"Falha ao buscar as cidades para o estado {estado}"})
    except Exception as e:
        return jsonify({"erro": str(e)})

# Rota para obter todas as cidades do Brasil ordenadas alfabeticamente por nome
@app.route('/cidades')
def lista_cidades_rota():
    return lista_cidades()

# Rota para obter as cidades de um estado específico ordenadas alfabeticamente por nome
@app.route('/cidades/<estado>')
def lista_por_estado_rota(estado):
    return lista_por_estado(estado.upper())

if __name__ == '__main__':
    app.run(debug=True)
