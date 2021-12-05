import requests

data = {"username": "Lomba", "secret": "@admin477",
        "info": "cargo", "value": "desenvolvedor"}
response = requests.post(
    "http://127.0.0.1:5000/empregados/informations", data=data)

#response = requests.get('http://127.0.0.1:5000/empregados/salario/5000')

if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)
