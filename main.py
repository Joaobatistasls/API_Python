import requests
import json

cep = 57940000
cep = str(cep)

if len(cep) == 8:
    url_api = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    # print(f"Resposta sem o JSON: {url_api}")  
    resposta = url_api.json()
    # print(f"Resposta com JSON: {resposta}")
    cep, localidade, uf = resposta["cep"], resposta["localidade"], resposta["uf"]
    print(f"Seu endereço é: {cep}, {localidade}, {uf}")
else:
    raise ValueError("CEP Inválido!!")
