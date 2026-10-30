from new_interface import maquina_escreve, limpa_tela
import time
import json
import os


#----------------------------------------------#
#----------------| SAVE $ LOAD |---------------#
ARQUIVO_SAVE = "saves.json"

def inicializar_saves():
    if not os.path.exists(ARQUIVO_SAVE):
        dados_iniciais = {
            "slot_1": {"status": "Vazio", "tripulacao": [], "turno": 0},
            "slot_2": {"status": "Vazio", "tripulacao": [], "turno": 0},
            "slot_3": {"status": "Vazio", "tripulacao": [], "turno": 0}
        }
        with open(ARQUIVO_SAVE, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_iniciais, arquivo, indent=4)

def carregar_dados_saves():
    with open(ARQUIVO_SAVE, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def exibir_slots(dados):
    print("\n=== SLOTS DE SAVE ===")
    for chave, info in dados.items():
        numero_slot = chave.replace("slot_", "") 
        status = info["status"]
        
        if status == "Vazio":
            print(f"[{numero_slot}] - Vazio")
        else:
            turno = info["turno"]
            print(f"[{numero_slot}] - Jogo Salvo (Turno: {turno} | Tripulação: {len(info['tripulacao'])} membros)")
            
    print("=====================")

#----------------------------------------------#

def menu_inicial():   
    while True:    
        maquina_escreve("Olá Jogador! Entre as opções abaixo...")
        print('''
        OPÇÕES DE JOGO    
            
        [1] Iniciar um Novo Jogo . . .
        [2] Carregar um Jogo Existente . . .
        [3] Mostrar TOP 5 . . .
        [4] Sair . . .
        ''')
        op1 = input("Digite sua opção: ").strip()
        
        if op1 == "1":
            print("\nIniciando novo jogo...")
            # iniciar_novo_jogo()
            pass
        elif op1 == '2':
            print("\nAbrindo tela de saves...")
            dados = carregar_dados_saves()
            exibir_slots(dados)
            input("\nPressione ENTER para voltar ao menu...")
        elif op1 == "3":
            print("\nExibindo ranking...")
            # exibir_ranking()
            pass
        elif op1 == "4":
            print("Finalizando . . .")
            time.sleep(0.05) # Corrigido de time.slep para time.sleep
            break
        else:
            print("Opção inválida! Escolha entre 1, 2, 3 ou 4!")
    
def main():
    inicializar_saves()
    menu_inicial()
    

if __name__ == "__main__":
    main()