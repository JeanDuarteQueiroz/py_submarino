from new_interface import maquina_escreve, iniciar_novo_jogo, gerar_submersivel_jogador, iniciar_missao, limpa_tela
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
def menu_navegacao(jogador, dificuldade_missao):
    
    jogador_ativo = jogador
    atributos_max = jogador_ativo.submersivel
    turnos = 0
    progresso = 0
    progressao_final = 0
    if dificuldade_missao == "inicial":
        progressao_final = 5000
    elif dificuldade_missao == "FACIL":
        progressao_final = 12000
    elif dificuldade_missao == "MEDIA":
        progressao_final = 22000
    elif dificuldade_missao == "DIFICIL":
        progressao_final = 50000
    else:
        progressao_final = 8000
    
    while True:
        limpa_tela()
        print("Informações Atuais:")
        print("-"*25)
        print(f"Progresso atual: {progresso}/{progressao_final} - Dificuldade: {dificuldade_missao}")
        print("-"*25)
        print("Recursos:")
        print(f"Oxigênio: {jogador_ativo.submersivel["oxigenio"]}% || Bateria: {jogador_ativo.submersivel["bateria"]}% || Casco: {jogador_ativo.submersivel["integridade_casco"]}%")
        print("-"*25)
        print("Tripulantes:")
        for nome, dados in jogador_ativo.tripulantes.items():
            print(f"[{dados["nome"]}] | +{dados["bonus"]} em {dados["tipo"]}")
        print(
            '''
            OPÇÕES DO MENU:
            
            [1] Descer submersível (Explorar)
            [2] Desligar os Motores (Consertar Casco)
            [3] Fazer Reparos (Recarrega Bateria)
            [4] Usar Itens
            [5] Salvar e Sair
            '''
        )
        op_jogador = input("Digite sua opção:  ").strip()
        if op_jogador == "1":
            oxigenio, bateria, progressao = jogador_ativo.descer_mais_fundo()
            progresso += progressao
            maquina_escreve(f"Você desceu {progressao}m! Gastos: {oxigenio}% de oxigênio e {bateria}% de bateria!")
            time.sleep(1.2)
            turnos += 1
            #gera_evento()
        elif op_jogador == "2":
            if jogador_ativo.submersivel["bateria"] >= atributos_max["bateria"]:
                print()
                print("A bateria está totalmente carregada!")
                time.sleep(1.2)
            else:
                oxigenio, carga = jogador_ativo.desligar_motores()
                jogador_ativo.submersivel["bateria"] = min(atributos_max["bateria", jogador_ativo.submersivel["bateria"]+ carga])
                print()
                maquina_escreve(f"Você recuperou {carga}% da Bateria! Gastos: {oxigenio}% de oxigênio!")
                time.sleep(1.2)
                turnos += 1
        elif op_jogador == "3":
            if jogador_ativo.submersibel["integridade_casco"] >= atributos_max["integridade_casco"]:
                print()
                print("A integridade do casco está perfeita!")
                time.sleep(1.2)
            else:
                oxigenio, bateria, reparo = jogador_ativo.desligar_motores()
                maquina_escreve(f"Você recuperou {reparo}% da Bateria! Gastos: {oxigenio}% de oxigênio e {bateria}% de bateria!")
                time.sleep(1.2)
                turnos += 1
        elif op_jogador == "4":
            pass

        elif op_jogador == "5":
            maquina_escreve("Salvando o jogo . . .")
            time.sleep(1.2)
            maquina_escreve("Finalizando o jogo . . .")
            time.sleep(1.2)
            break
        
        if jogador_ativo.submersivel["oxigenio"] or jogador_ativo.submersivel["bateria"] or jogador_ativo.submersivel["integridade_casco"] <= 0:
            limpa_tela()
            maquina_escreve("Os níveis da embarcação chegaram a níveis críticos . . .")
            time.sleep(1.2)
            for nome, dados in jogador_ativo.tripulantes.items():
                maquina_escreve(f"[{dados["nome"]}]: {dados["frase_fracasso"]}")
                time.sleep(1.5)
            
            print()   
            maquina_escreve("O submersível não aguentou a exploração.")
            time.sleep(1.2)
            break
        
        if progressao_final >= progresso:
            limpa_tela()
            maquina_escreve("Você conseguiu Comandante! A Exploração foi um sucesso!")
            time.sleep(1.2)
            print()
            maquina_escreve("Armazenando informações da exploração . . .")
            
            #Salvar informações da missão (tipo, comandante, nome da embarcação, tripulação, turnos).
            
            print()
            print("Deseja continuar explorando? ")
            op_jogador_venceu = input("Digite 'S' ou 'N':  ")

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
            comandante, submersivel = iniciar_novo_jogo()
            jogador = gerar_submersivel_jogador(comandante, submersivel)
            dificuldade_missao = iniciar_missao(True)
            menu_navegacao(jogador, dificuldade_missao)
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