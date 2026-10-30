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