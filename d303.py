
class CuboMagico():

    def __init__(self, cores,  lados): #metodo construtor de atributos
        self.colors = cores 
        self.sides = lados

    def get_cores(self):
        return  self.colors

    def  get_lados(self):
        return self.sides

    def set_cores(self, cores):
        self.colors = cores

    def set_lados(self, lados):
        self.sides = lados


lista_de_cores= [ 'vermelho', 'azul', 'verde', 'amarelo', 'laranja', 'branco']

porcos = CuboMagico(lista_de_cores, 6)

cores_do_porco = porcos.get_cores()
porcos.set_cores(['','','','','',''])
print(cores_do_porco)

class Animal():

    def __init__(self, pelo, patas ):
        self.pelo = pelo
        self.patas = patas
