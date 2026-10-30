from interface import cria_jogador, aguarda_jogador, limpa_tela, gera_evento, salvar_recorde, exibir_top_3
from entidade import Submarino
import time

def main():
    
    submarino = cria_jogador()
    limpa_tela()
    submarino.exibe_ficha()
    aguarda_jogador()
    
    turnos = 0
    progressao = 0
    progressao_fim = 11000
    
    while True:
        turnos += 1
        limpa_tela()
        print(f"Progresso atual: {progressao}")
        print(f"Recursos: \nOxigênio: {submarino.oxigenio}%\nBateria: {submarino.bateria}%\nIntegridade do Casco: {submarino.integridade_casco}%")
        print('''
        Menu de Opções
        
        [1] Descer mais fundo. (- oxigenio, - bateria)
        
        [2] Fazer reparos. (+ casco, - bateria)
        
        [3] Desligar motores. (+ bateria, - oxigenio)
        '''
        )
        op = int(input("Digite sua a opção: "))
        
        if op == 1:
            progresso, gasto_oxigenio, gasto_bateria = submarino.descer_mais_fundo(progressao)
            progressao += progresso
            print(f"Você desceu... - {gasto_oxigenio}% de oxigênio e - {gasto_bateria}% de bateria.")
            time.sleep(1)
            tem_evento, descricao, tipo, dano = gera_evento()
            if tem_evento == True:
                if tipo == "oxigenio":
                    submarino.oxigenio = max(0, submarino.oxigenio - dano)
                    print(descricao)
                    print(f"Seu oxigênio teve {dano}% de redução")
                    time.sleep(2)
                elif tipo == "bateria":
                    submarino.bateria = max(0, submarino.bateria - dano)
                    print(descricao)
                    print(f"Sua bateria teve {dano}% de redução!")
                    time.sleep(2)
                elif tipo == "integridade_casco":
                    submarino.integridade_casco = max(0, submarino.integridade_casco - dano)
                    print(f"Seu casco sofreu {dano}% de avaria!")
                    time.sleep(2)
                else:
                    print("Tipo desconhecido!")
                    time.sleep(2)
            else:
                print(descricao)
                time.sleep(2)
                
        elif op == 2:
            if submarino.integridade_casco >= 100:
                print("A integridade do está perfeita!")
            else:
                reparo, gasto = submarino.fazer_reparos()
                print(f"Você reparou {reparo}% do casco! Mas gastou {gasto}% da bateria nesse processo.")
            time.sleep(1)
        elif op == 3:
            if submarino.bateria >= 100:
                print("A bateria totalmente carregada!")
            else:
                recarga, gasto = submarino.desligar_motores()
                print(f"Você recarregou {recarga}% de bateria! Mas gastou {gasto}% de oxigênio aguardando o processo.")
            time.sleep(1)
        else:
            limpa_tela()
            print("Escolha a opção válida!")
            time.sleep(1)
            limpa_tela()
        
        if submarino.oxigenio <= 0 or submarino.bateria <= 0 or submarino.integridade_casco <=0:
            limpa_tela()
            print("Game Over")
            time.sleep(1)
            break
        
        if progressao >= progressao_fim:
            limpa_tela()
            print("Parabéns Comandante! Você conseguiu explorar a fossa oceânica!")
            
            # Salva o recorde e exibe o placar
            salvar_recorde(submarino.comandante, turnos)
            exibir_top_3()
            
            time.sleep(1)
            break
    
        
        
if __name__ == "__main__":
    main()