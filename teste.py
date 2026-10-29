import json
import random

with open("dados/eventos.json", "r", encoding="utf-8") as arquivo:
    dados_eventos = json.load(arquivo)
    
chaves = list(dados_eventos.keys())
evento = random.choice(chaves)    
print(dados_eventos[evento]["descricao"])