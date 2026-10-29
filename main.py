from interface import cria_jogador, aguarda_jogador, limpa_tela
from entidade import Submarino
import time

def main():
    
    submarino = cria_jogador()
    limpa_tela()
    submarino.exibe_ficha()
    aguarda_jogador()
    
    progressao = 0
    progressao_fim = 11000
    
    while True:
        
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
            time.sleep(1)
            break
        
if __name__ == "__main__":
    main()