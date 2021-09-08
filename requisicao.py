import requests
import json


# Realiza requisição na URL configurada
URL = open("url.txt").readline()
requisicao = requests.get(URL, verify=False)
response = requisicao.json()

# Printa na tela o resultado JSON
print(response)

# Salva a resposta em um arquivo JSON
with open("arquivo.json", "w") as outfile:
    json.dump(response, outfile)

