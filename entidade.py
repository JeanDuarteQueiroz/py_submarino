from random import randint
import json
import os

ARQUIVO_RECORDES = "dados/recordes.json"

class Submarino():
    def __init__( self, id, nome: str, comandante: str):
        # INFOS #
        self.id = id
        self.nome = nome
        self.comandante = comandante
        
        # RECURSOS #
        self.oxigenio = 100
        self.integridade_casco = 100
        self.bateria = 100
        
        
        # TRIPULANTES #
        self.tripulantes = {
            
        }
        
        # CONSUMIVEIS #
        self.itens = {
            
        }
    
    def __str__(self):
        return f"Comandante: {self.comandante} - Embarcação: {self.nome} || Niveis: Oxigênio: {self.oxigenio}%, Bateria: {self.bateria}%, Integridade Casco: {self.integridade_casco}"  
  
    def exibe_ficha(self):
        print("-"*20)
        print(f"COMANDANTE DA MISSÃO: {self.comandante}")
        print("-"*20)
        print(f"EMBARCAÇÃO: {self.nome}")
        print("-"*20)
        print("NÍVEIS DE RECURSO:")
        print()
        print(f"Oxigênio: {self.oxigenio}%")
        print(f"Bateria: {self.bateria}%")
        print(f"Integridade do Casco: {self.integridade_casco}%")
        print("-"*20)
        print("TRIPULANTES:")
        print()
        print(f"Controlador: {self.tripulantes.get('controlador', 'Desocupado')}")
        print(f"Analista: {self.tripulantes.get('analista', 'Desocupado')}")
        print(f"Mecânico: {self.tripulantes.get('mecanico', 'Desocupado')}")
        print("-"*20)
        print()
        
    def descer_mais_fundo(self, progresso):

        progresso = randint(500, 1200) 
        
        gasto_oxigenio = randint(2,7)    
        gasto_bateria = randint(1,5)
        
        self.oxigenio = max(0, self.oxigenio - gasto_oxigenio)
        self.bateria = max(0, self.bateria - gasto_bateria)
        
        return progresso, gasto_oxigenio, gasto_bateria
    
    def fazer_reparos(self):
        if self.integridade_casco >= 100:
            return 
        
        reparo = randint(10,30)
        gasto_bateria = randint (3, 10)
        
        self.integridade_casco = min(100, self.integridade_casco + reparo)
        self.bateria = max(0, self.bateria - gasto_bateria)

        return reparo, gasto_bateria
    
    def desligar_motores(self):
        if self.bateria >= 100:
            return
        
        recarga = randint(10,30)
        gasto_oxigenio = randint (3, 10)
        
        self.bateria = min(100, self.bateria + recarga)
        self.oxigenio = max(0, self.oxigenio - gasto_oxigenio)
        
        return recarga, gasto_oxigenio