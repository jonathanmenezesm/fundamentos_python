# Crie um codigo em python que teste "pudim" está acessivel pelo computador usado.

import requests

try:
    r = requests.get("http://www.pudim.com.br")
    if r.ok:  # equivalente a status_code == 200
        print("O site Pudim está acessível!")
    else:
        print("Não consegui acessar o site Pudim!")
except requests.exceptions.RequestException:
    print("Erro ao tentar acessar o site Pudim!")


