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
    else:
        return False, "Nada de mais ocorreu", "nenhum", 0
    
def salvar_recorde(nome_comandante, turnos):
        recordes = []
        
        # 1. Lê os dados existentes, se o arquivo já existir
        if os.path.exists(ARQUIVO_RECORDES):
            with open(ARQUIVO_RECORDES, "r", encoding="utf-8") as arquivo:
                try:
                    recordes = json.load(arquivo)
                except json.JSONDecodeError:
                    recordes = [] # Previne erro se o arquivo existir mas estiver vazio
                    
        # 2. Adiciona a nova pontuação
        recordes.append({
            "comandante": nome_comandante, 
            "turnos": turnos
        })
        
        # 3. Ordena a lista do menor para o maior número de turnos
        # A função lambda diz ao Python para usar o valor da chave "turnos" como critério de ordenação
        recordes.sort(key=lambda x: x["turnos"])
        
        # (Opcional) Mantém apenas o Top 5 para o arquivo não crescer infinitamente
        recordes = recordes[:5]
        
        # 4. Salva os dados ordenados de volta no arquivo
        with open(ARQUIVO_RECORDES, "w", encoding="utf-8") as arquivo:
            json.dump(recordes, arquivo, indent=4, ensure_ascii=False)

def exibir_top_3():
        if not os.path.exists(ARQUIVO_RECORDES):
            return
            
        with open(ARQUIVO_RECORDES, "r", encoding="utf-8") as arquivo:
            recordes = json.load(arquivo)
            
        print("\n" + "="*30)
        print("🏆 TOP 3 COMANDANTES 🏆")
        print("="*30)
        
        # Pega apenas os 3 primeiros da lista
        for i, recorde in enumerate(recordes[:3]):
            print(f"{i+1}º Lugar: Cmdt. {recorde['comandante']} - {recorde['turnos']} turnos")
        print("="*30 + "\n")