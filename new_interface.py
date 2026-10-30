import os
import sys
import time
import random
import json
from new_entidade import Submersivel

ARQUIVO_RECORDES = "dados/recordes.json"
QUALIDADE = "comum", "incomum", "raro"

with open("dados/dados_submersivel.json", "r", encoding="utf-8") as arquivo:
    dados_submersivel = json.load(arquivo)
    
with open("dados/dados_tripulantes.json", "r", encoding="utf-8") as arquivo:
    dados_tripulantes = json.load(arquivo)

with open("dados/eventos.json", "r", encoding="utf-8") as arquivo:
    dados_eventos = json.load(arquivo)
    
#--------------| UTILITARIOS |-------------#
def jogador_confirma():
    input("Digite [ENTER] para continuar...")
    return

def maquina_escreve(texto: str, atraso: float = 0.02, quebrar_linha: bool = True):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(atraso)
        
    if quebrar_linha:
        print()

def limpa_tela():
    os.system('cls' if os.name == "nt" else "clear")
#------------------------------------------#
#----------------| RANKING |---------------#
def exibir_ranking(x: int = 3):
    if not os.path.exists(ARQUIVO_RECORDES):
        return
    
    with open(ARQUIVO_RECORDES, "r", encoding="utf-8") as arquivo:
        recordes = json.load(arquivo)
    
    for i, recorde in enumerate(recordes[:x]):
        print(f"{i+1}º Lugar: Cmdt. {recorde['comandante']} - {recorde['turnos']} turnos")
    print("="*30 + "\n")
#------------------------------------------#    
#----------| GERADOR DE EVENTOS |----------#





#------------------------------------------#
#----------------| JOGADOR |---------------#  

def gerar_submersivel_jogador(comandante, nome_submersivel):
    
    qualidade_tripulante = random.choices(QUALIDADE, weights=[9.7, 0.2, 0.1], k=1)
    qualidade_submersivel = random.choices(QUALIDADE, weights=[9.7, 0.2, 0.1], k=1)    

    atributos_base = dados_submersivel.get(qualidade_submersivel[0])

    tripulantes = {}

    tripulantes_da_qualidade = dados_tripulantes.get(qualidade_tripulante[0], {})
    lista_sorteio = list(tripulantes_da_qualidade.items())
    quantidade = min(3, len(lista_sorteio))
    sorteados = random.sample(lista_sorteio, quantidade)

    for nome, atributos in sorteados:
        tripulantes[nome] = atributos
    
    atributos = atributos_base.copy()
    
    for nome, dados in tripulantes.items():
        if "bonus" in dados and "tipo" in dados:
            tipo_atributo = dados["tipo"]
            valor_bonus = dados["bonus"]
            
            if tipo_atributo in atributos:
                atributos[tipo_atributo] += valor_bonus
                
    atributos["nome"] = nome_submersivel
    
    jogador = Submersivel(1, "submersivel", comandante, atributos, tripulantes)

    return jogador
   
def inicia_novo_jogo():
    limpa_tela()
    maquina_escreve("Gerando um novo protocólo de missão. . .")
    time.sleep(1.5)
    print()
    maquina_escreve("Iniciando o protocólo. . .")
    time.sleep(1.5)
    print()
    limpa_tela()
    nome_comandante = input("Digite o nome do Comandante responsável: ")
    time.sleep(1.5)
    print()
    print(
        '''
        Escolha do Submersível:
        
        [1] Submersível próprio.
        [2] Submersível da Companhia.
        '''    
    )
    op = input("Digite a opção: ")
    while True:
        if op == "1":
            nome_submersivel = input("Digite o nome do Submersível:  ")
            time.sleep(1.5)
            print()
            break
        elif op == "2":
            maquina_escreve("Buscando submersiveis disponíveis. . .")
            nome_submersivel = random.choice(dados_submersivel)
            print()
            maquina_escreve(f"Submersível disbonibilizado para a missão: {nome_submersivel}")
            break
        else:
            print("Escolha uma opção válida! 1 ou 2\n")

    maquina_escreve("\nInformações anexadas ao protocólo. Iniciando missão.")
    return nome_comandante, nome_submersivel