# exemplo_03_requisicoes.py

import requests


url_base = "https://api.franciscosensaulas.com"

# Consultar categorias 

def consultar_categorias():
    url = f"{url_base}/api/v1/biblioteca/categorias"

    resposta = requests.get(url)

    print("Status Code:", resposta.status_code)
    print("Response:", resposta.text)

def apagar_categoria():
    id = 191
    url = f"{url_base}/api/v1/biblioteca/categorias/{id}"

    resposta = requests.delete(url)
    print("Status Code:", resposta.status_code)


def cadastrar_categoria():
    url = f"{url_base}/api/v1/biblioteca/categorias"

    categoria = {
        "nome": "Drama"
    }

    resposta = requests.post(url, json=categoria)
    print("Status Code: ", resposta.status_code)


def editar_categoria():
    id = 192
    url = f"{url_base}/api/v1/biblioteca/categorias/{id}"
    
    categoria = {
        "nome": "Ação"
    }
    resposta = requests.put(url, json=categoria)
    print("Status Code: ", resposta.status_code)


# cadastrar_categoria()
# apagar_categoria()
# editar_categoria()
consultar_categorias()