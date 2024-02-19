import requests

def get_champions_name(_id):
    # Obter a versão mais recente da API
    url = "http://ddragon.leagueoflegends.com/api/versions.json"
    r = requests.get(url)
    version = r.json()[0]
    
    # Obter os dados dos campeões usando a versão obtida
    url2 = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
    request2 = requests.get(url2)
    data = request2.json()
    
    # Procurar pelo campeão com o ID fornecido
    for champion, info in data["data"].items():
        if int(info["key"]) == _id:  # Comparando o ID como inteiro
            return champion
