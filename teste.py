import random
import time
import new_interface

class Entidade():
    def __init__(self, id: int, nome: str):
        pass

class Submersivel(Entidade):
    def __init__(self, id, nome , comandante: str, submersivel: dict, tripulantes: dict):
        super().__init__(id, nome)
        
        self.id = id
        self.nome = nome
        
        self.comandante = comandante
        
        atributos_submersivel = ['nome','oxigenio', 'bateria', 'integridade_casco']
        self.submersivel = {x: submersivel[x] for x in atributos_submersivel if x in atributos_submersivel}

        
        self.tripulantes = tripulantes
        
        self.itens = {
            
        }
    
    def __str__(self):
        return super().__str__()
    
    def descer_mais_fundo(self):
        
        gasto_oxigenio_padrao = random.randint(1, 10)
        gasto_bateria_padrao = random.randint(1, 10)
        
        self.submersivel["oxigenio"] = max(0, self.submersivel["oxigenio"] - (gasto_oxigenio_padrao)) # ADICIONAR HABILIDADES DE TRIPULANTES QUE REDUZEM O GASTO
        self.submersivel["bateria"] = max(0, self.submersivel["bateria"] - (gasto_bateria_padrao)) # ADICIONAR HABILIDADES DE TRIPULANTES QUE REDUZEM O GASTO
                
        progresso_padrao = random.randint(500, 1200) 
        # ADICIONAR HABILIDADES DE TRIPULANTES OU SUBMERSIVEL QUE AUMENTAM O PROGRESSO
        
        return gasto_oxigenio_padrao, gasto_bateria_padrao, progresso_padrao

    def fazer_reparos(self):
                
        reparo_padrao = random.randint(15, 30)
        
        self.submersivel["integridade_casco"] = min(100, self.submersivel["integridade_casco"] + (reparo_padrao)) # ADICIONAR HABILIDADE DE TRIPULANTE QUE AUMENTA O REPARO
        
        gasto_oxigenio_padrao = random.randint(1, 4)
        gasto_bateria_padrao = random.randint(1, 15)
        
        self.submersivel["oxigenio"] = max(0, self.submersivel["oxigenio"] - (gasto_oxigenio_padrao)) # ADICIONAR HABILIDADES DE TRIPULANTES QUE REDUZEM O GASTO
        self.submersivel["bateria"] = max(0, self.submersivel["bateria"] - (gasto_bateria_padrao)) # ADICIONAR HABILIDADES DE TRIPULANTES QUE REDUZEM O GASTO
        
        return gasto_oxigenio_padrao, gasto_bateria_padrao, reparo_padrao
    
    def desligar_motores(self):
        
        carga_padrao = random.randint(15, 30)
        
        self.submersivel["bateria"]  = min(100, self.submersivel["bateria"] + (carga_padrao)) # ADICIONAR HABILIDADE DE TRIPULANTE QUE AUMENTA A CARGA PADRÃO
        
        gasto_oxigenio_padrao = random.randint(1, 4)
        
        self.submersivel["oxigenio"] = max(0, self.submersivel["oxigenio"] - (gasto_oxigenio_padrao)) # ADICIONAR HABILIDADES DE TRIPULANTES QUE REDUZEM O GASTO
        
        return gasto_oxigenio_padrao, carga_padrao
    
submersivel_teste = {
    "nome": "Abominável",
    "oxigenio": 100,
    "bateria": 100,
    "integridade_casco": 50
}

tripulantes_teste = {
    "presidente": {
        "nacao": "Brasil",
        "nome": "Presidente",
        "bonus": 20,
        "tipo": "integridade_casco"
    },
    "tuso": {
        "nacao": "Brasil",
        "nome": "Tuso",
        "bonus": 20,
        "tipo": "oxigenio"
    },
    "charlie": {
        "nacao": "Brasil",
        "nome": "Charlie",
        "bonus": 20,
        "tipo": "bateria"    
    }
}

jogador = Submersivel(1, "submersivel", "Jean Duarte Queiroz", submersivel_teste, tripulantes_teste)

jogador.itens["cilindro_de_oxigenio"] = {
    "id": 1,
    "nome": "Cilindro de Oxigênio",
    "quantidade": 3,
    "descricao": "Um cilindro que contém uma boa quantidade de oxigenio armazenada.",
    "bonus": 30,
    "tipo": "oxigenio"
}

progressao = 0
turno = 0

while True:
    new_interface.limpa_tela()
    print(f"SEU PROGRESSO: {progressao}")
    print(f"TURNOS: {turno}")
    print(f"Oxi: {jogador.submersivel["oxigenio"]}, Bat {jogador.submersivel["bateria"]}, Casco {jogador.submersivel["integridade_casco"]}")
    print(
        '''
        ESCOLHAS:
        
        
        [1] DESCER
        [2] FAZER REPARO
        [3] DESLIGAR MOTORES
        [4] USAR ITENS
        [5] SAIR
        '''
    )
    op = input("Digite a opção:  ")
    if op == "1":
        oxigenio, bateria, progresso = jogador.descer_mais_fundo()
        progressao += progresso
        print(f"\nVocê desceu {progresso}m e usando {oxigenio}% de oxigenio e {bateria}% de bateria")
        turno += 1
        time.sleep(1.5)
        new_interface.limpa_tela()
        
    elif op == "2":
        if jogador.submersivel["integridade_casco"] >= 100:
            print("\nIntegridade do casco está perfeita!")
            time.sleep(2)
        else:
            oxigenio, bateria, reparo = jogador.fazer_reparos()
            print(f"\nVocê reparou {reparo}% do casco! Você consumiu {oxigenio}% de oxigenio e {bateria}% de bateria.")
            turno += 1
            time.sleep(1.5)
            new_interface.limpa_tela()
            
    elif op == "3":
        if jogador.submersivel["bateria"] >= 100:
            print("A bateria está totalmente carregada!")
            time.sleep(2)
        else:
            oxigenio, carga = jogador.desligar_motores()
            print(f"\nVocê desligou os motores e recarregou {carga}% de bateria, e gastou {oxigenio}% de oxigenio.")
            turno += 1
            time.sleep(1.5)
            new_interface.limpa_tela()
    
    elif op == "4":
        id_item = new_interface.exibir_inventario(jogador)
        if id_item != "0":      
            turno+=1
            id_item = int(id_item)
            new_interface.usar_item(jogador, id_item)
        
    elif op == "5":
        print("\nSaindo.")
        time.sleep(1)
        break