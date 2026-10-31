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
    
    def usar_consumivel(self, consumivel):
        tipo = consumivel["tipo"]
        bonus = consumivel["bonus"]
        if consumivel[tipo] in ["oxigenio", "integridade_casco", "bateria"]:
            self.submersivel[tipo] = min(100, self.submersivel[tipo] + bonus)
        
        return tipo, bonus


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

todos_itens = jogador.itens

for chave, valor in todos_itens.items():
    print(f"{valor["id"]} -> {valor["nome"]} x {valor["quantidade"]} -> {valor["descricao"]}")
    
id_item = input("Digite o ID do item: ").strip()

if id_item in todos_itens.values():
    print("Uhu")

