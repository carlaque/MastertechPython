class Receita():

    def __init__(self, instrumentos, ingredientes, preparo):
        self.instrumentos = instrumentos
        self.ingredientes = ingredientes
        self.preparo = preparo

    ##GETTERS
    def get_instrumentos(self):
        return self.instrumentos
    def get_ingredientes(self):
        return self.ingredientes
    def get_preparo(self):
        return self.preparo
    
    ##SETTERS
    def set_instrumentos(self, ins):
        self.instrumentos = ins
    def set_ingredientes(self, ing):
        self.ingredientes = ing
    def set_preparo(self, pre):
        self.preparo = pre

    ##METODOS
    def lerInstrumentos(self, rec):
        inst=1
        instrumentos = []
        while(inst == 1):
            instrumento = input("Digite um instrumento: \n")
            instrumentos.append(instrumento)
            inst = int(input("\nDeseja inserir mais instrumento?\n1 - sim\n2 - não \n"))

        rec.set_instrumentos(instrumentos)
        # print(rec.get_instrumentos())
    
    def lerIngredientes(self,rec):
        ingr = 1
        ingredientes =[]
        while(ingr==1):
            ingrediente = input("Digite um ingrediente: \n")
            ingredientes.append(ingrediente)
            ingr = int(input("\nDeseja inserir mais ingrediente?\n1 - sim\n2 - não \n"))

        rec.set_ingredientes(ingredientes)
        # print(rec.get_ingredientes())

    def lerPreparos(self,rec):
        ppr = 1
        preparos = []
        while(ppr==1):
            preparo = input("Digite uma etapa do preparo: \n")
            preparos.append(preparo)
            ppr = int(input("\nDeseja inserir mais uma etapa do preparo?\n1 - sim\n2 - não \n"))

        rec.set_preparo(preparos)
        print(rec.get_preparo())

    def exibir(self,rec):
        print("-----INSTRUMENTOS------")
        print('\n'.join(map(str, rec.get_instrumentos()))) 

        print("\n-----INGREDIENTES-----")
        print('\n'.join(map(str, rec.get_ingredientes()))) 

        print("\n-----MODO DE PREPARO-----")
        print('\n'.join(map(str, rec.get_preparo()))) 


class Doce(Receita):

    def __init__(self, instrumentos, ingredientes, preparo, confeitos, quantidade):
        self.instrumentos = instrumentos
        self.ingredientes = ingredientes
        self.preparo = preparo
        self.confeitos  = confeitos
        self.quantidade = quantidade

    ##GETTERS
    def get_confeitos(self):
        return self.confeitos
    def get_quantiade(self):
        return self.quantidade

    ##SETTER
    def set_confeitos(self, conf):
        self.confeitos = conf
    def set_quantiade(self, qtd):
        self.quantidade = qtd
    
    ##METODOS
    def lerConfeitos(self, rec):
        confs = 1
        confeitos = []
        while(confs == 1):
            confeito = input("Digite o confeito necessario:\n")
            confeitos.append(confeito)
            confs = int(input("Deseja adicionar mais um confeito a receita?\n1 - sim\n2 - nao"))
        
        rec.set_confeitos(confeitos)

    def lerQuantidade(self, rec):
        quantidade = int(input("\nDigite o quantiade de doces que essa receita ia render:\n"))
        rec.set_quantiade(quantidade)

# class Salgado(Receita):



rec = Receita(['panela', 'garfo'], ['agua','macarrao instantaneo','tempero'], ['ferva a agua'])

Receita.lerInstrumentos(True, rec)
Receita.lerIngredientes(True, rec)
Receita.lerPreparos(True, rec)
Receita.exibir(True, rec)
