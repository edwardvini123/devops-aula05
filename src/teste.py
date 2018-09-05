class tv:
    def __init__(self,polegadas, marca):
        self.polegadas = polegadas
        self.marca = marca
        self.canais = 50
        self.volumemaximo = 100
        self.estadotv = False
        self.volumeatual = 11
        self.canalatual = 5
        self.canalmaximo = 1000
    def metodoligar(self):
        #codigo ligar
        self.estadotv = not self.estadotv
    def metododesligar(self):
        #codigo desligar
        self.estadotv = not self.estadotv
    def metodovolumemais(self):
        #codigo volume mais
        if (self.volumeatual < self.volumemaximo):
            self.volumeatual += 1
        else:
                print("nao é possivel")
    def metodovolumemenos(self):
        #codigo volume menos
        if (self.volumeatual > 0):
            self.volumeatual -= 1
        else:
                print("nao é possivel")
    def metodoescolhecanal(self):
        #codigo escolhe canal
        self.canalatual = ""
    def metodoavancacanal(self):
        #codigo avanca canal
        if (self.canalatual < self.canalmaximo):
            self.canalatual += 1
        else:
                print("nao é possivel")
    def metodovoltacanal(self):
        #codigo volta canal
        if (self.canalatual > 0):
            self.canalatual -= 1
        else:
                print("nao é possivel")  

v = tv(40,"sony")
"""print(v.estadotv)
v.metodoligar()
print(v.estadotv)
v.metododesligar()
print(v.estadotv)
print(v.volumeatual)
v.metodovolumemais()
print(v.volumeatual)
v.metodovolumemenos()
print(v.volumeatual)
v.metodoescolhecanal()
print(v.canalatual)
v.metodoavancacanal()
print(v.canalatual)
v.metodovoltacanal()
print(v.canalatual)"""


def loop(tv):
    onibus = True
    while 1==1 :
        teste = int(input("Digite a opcao: 1 liga  2 desliga 3 volumemais 4 volumemenos"))
        if teste == 1:
            v.metodoligar()
            print(v.estadotv)
        elif teste == 2:
            v.metododesligar()
            print(v.estadotv)
        elif teste == 3:
            if v.volumeatual < v.volumemaximo:
                v.metodovolumemais()
                print(v.volumeatual)
            else:
                print("Naopode")
        elif teste == 4:
            if v.volumeatual > 0:
                v.metodovolumemenos()
                print(v.volumeatual)
            else:
                print("Naopode")
        elif teste == 5:
            if v.estadotv = True:
                if v.canalmaximo < 1000: 
                    quantos = int(input("quantos"))
                    v.canalatual += quantos


            v.metodoescolhecanal()
            print(v.canalatual)
        
        else:
            print("teste")

loop(tv)


#variavel de instancia sem parametro, pois nao estou solicitando parametor acima 
'''v = veiculo("fusca","1996","asd-1231","preto")
print (v.estadomotor)
v.metodoligar()
print (v.estadomotor)
print(v.nome,v.modelo,v.placa,v.cor,v.estadomotor)'''
'''
class onibus(veiculo):
    def __init__(self,nome,modelo,placa,cor,capacidademaxima,situacaoporta,passageiros):
        veiculo.__init__(self,nome,modelo,placa,cor)
        self.capacidademaxima = capacidademaxima
        self.situacaoporta = 0
        self.passageiros = 0
    def definircapacidade(self,cap):
        self.capacidademaxima = 10
    def abrirporta(self):
        self.situacaoporta = 1
    def fecharporta(self):
        self.situacaoporta = 0
    def entrarpassageiro(self):
        if (self.situacaoporta == 1 and self.passageiros < self.capacidademaxima ):
            self.passageiros += 1
        else:
                print("nao é possivel")
    def sairpassageiro(self):
        if (self.situacaoporta == 1 and self.passageiros > 0 ):
            self.passageiros -= 1
        else:
            print("nao é possivel: sair")

def loop(onibus):
    onibus = True
    while 1==1 :
        teste = int(input("Digite a opcao: 1 abre  2 fecha  3 entra 4 Sai  5 passageiros "))
        if teste == 1:
            o.abrirporta()
            print(o.situacaoporta)
        elif teste == 2:
            o.fecharporta()
            print(o.situacaoporta)
        elif teste == 3:
            if o.situacaoporta == 1:
                if o.capacidademaxima < 10: 
                    quantos = int(input("quantos"))
                    o.passageiros += quantos
        elif teste == 4:
            if o.situacaoporta == 1:
                quantos = int(input("quantos"))
                o.passageiros -= quantos
            elif o.situacaoporta == 0:
                print("impossivel sair")
        elif teste == 5:
            print (o.passageiros)
        
        else:
            print("teste")
            
o = onibus("fusca","1996","asd-1231","preto",3,"situacaoporta",1)

loop(onibus)
'''
'''
o.abrirporta()
print("Abre porta")
print("Entra Passageiro")
o.entrarpassageiro()
print("Quantidade de passageiros no onibus",o.passageiros)
o.fecharporta()
print("Fecha Porta")
print("Abre porta")
o.abrirporta()
print("Entra Passageiro")
o.entrarpassageiro()
print("Quantidade de passageiros no onibus",o.passageiros)
print("Sai Passageiro")
o.sairpassageiro()
print("Quantidade de passageiros no onibus",o.passageiros)'''
