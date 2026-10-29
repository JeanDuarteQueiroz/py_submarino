from entidade import Submarino 
import os
import sys
import time
import random
import json

with open("dados/nomes_submarino.json", "r", encoding="utf-8") as arquivo:
    dados_submarino = json.load(arquivo)
    
with open("dados/nomes_tripulantes.json", "r", encoding="utf-8") as arquivo:
    dados_tripulantes = json.load(arquivo)

with open("dados/eventos.json", "r", encoding="utf-8") as arquivo:
    dados_eventos = json.load(arquivo)

def aguarda_jogador():
    input("Digite [ENTER] para continuar...")
    return

def limpa_tela():
    os.system('cls' if os.name == "nt" else "clear")

def maquina_escrever(texto: str, atraso: float = 0.05, quebrar_linha: bool = True):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(atraso)
    
    if quebrar_linha:
        print()

def cria_jogador():
    maquina_escrever("Gerando novo protocólo Abys...")
    time.sleep(1)
    maquina_escrever("Iniciando protocólo...")
    time.sleep(1)
    print()
    nome_comandante = input("Digite o nome do Comandante: ")
    maquina_escrever(". . . . .", 0.09)
    print()
    limpa_tela()
    print(
        '''
                Embarcação:
     |                                  |
     |  [1] Usar embarcação própria.    |
     |                                  |
     |  [2] Usar embarcação aleatória.  |
     |                                  |
        '''
    )
    while True:
        
        op = int(input("Digite a opção:  "))

        if op == 2:
            nome_submarino = random.choice(dados_submarino)
            maquina_escrever(". . . . .", 0.09)
            print()
            limpa_tela()
            maquina_escrever(f"Nome da Embarcação disponibilizada: {nome_submarino}")
            time.sleep(2)
            break
        elif op == 1:
            nome_submarino = input("Digite o nome da Embarcação:  ")
            maquina_escrever(". . . . .")
            print()
            limpa_tela()
            break
        else:
            print("Opção Inválida!")
            
    limpa_tela()
    maquina_escrever("Informações registradas e anexadas ao protocólo.")
    print()
    
    jogador = Submarino(1, nome_submarino, nome_comandante)
    
    jogador.tripulantes["controlador"] = random.choice(dados_tripulantes)
    jogador.tripulantes["analista"] = random.choice(dados_tripulantes)
    jogador.tripulantes["mecanico"] = random.choice(dados_tripulantes)
    
    aguarda_jogador()
    return jogador

def gera_evento():
    chance_evento = random.randint(1,100)
    chaves = list(dados_eventos.keys())
    
    if chance_evento <= 25:
        evento = random.choice(chaves)
        
        descricao = dados_eventos[evento]["descricao"]
        tipo = dados_eventos[evento]["tipo"]
        dano_min = dados_eventos[evento]["dano_min"]
        dano_max = dados_eventos[evento]["dano_max"]
        
        if tipo == "nenhum":
            gasto = 0
            return True, descricao, tipo, gasto
        else:
            gasto = random.randint(dano_min, dano_max)
            return True, descricao, tipo, gasto