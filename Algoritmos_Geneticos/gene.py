#import gym
from random import *

#IR - Identificador de Rede
class Gene(object):
    #O Espaço de genes é um intervalo, se for inteiro são somente aqueles numeros,
    #se for floats é um conjunto infinitesimal de numeros
    def __init__(self,EG,Var,CD):
        self.EG = EG
        self.Var = Var
        self.CD = CD
        
    def getEG(self):
        return self.EG

    def getVar(self):
        return self.Var
    
    def addEG(self,EG,Var):
        self.EG = EG
        self.Var = Var


class Cromossomo(object):
    
    def __init__(self,G,MAX = 2000,corda = [],pont = 0,P_Mut=5): 
        self.corda = corda
        self.pont = pont
        self.MAX = MAX
        self.G = G
        self.P_Mut = P_Mut
                   
    def getCorda(self):
        return self.corda

    def getMut(self):
        return self.P_Mut
    	
    def getPont(self):
        return self.pont
		
    def getMAX(self):
        return self.MAX
        
    def getG(self):
        return self.G

    def setPont(self,pont):
        self.pont = pont

    def preencherC_EG(C):
        if(len(C.getCorda())==0):
            cord = []
            x1 = C.getG().getEG()[0]
            x2 = C.getG().getEG()[1]
            Cas_Dec = C.getG().CD
            for _ in range(C.getMAX()):
            #u = randint(0,1), Peso Negativo
                if(C.getG().getVar()== 'F'):
                    cord.append((randint(x1,x2-1)+(randint(0,10**Cas_Dec)/10**Cas_Dec)))
                else:
                    cord.append(randint(x1,x2))
            C.corda = cord
        return C
                
    def cross(self,Cromossomo):
        corda1 = []
        corda2 = []
        for i in range(self.getMAX()):
            u = randint(0,1)
            if(u==1):
                corda1.append(self.getCorda()[i])
                corda2.append(Cromossomo.getCorda()[i])
            else:
                corda1.append(Cromossomo.getCorda()[i])
                corda2.append(self.getCorda()[i])
        
                
        fator_mutacao = choice(range(1,100000))/1000
        if(fator_mutacao <= self.getMut()):
            x1 = self.getG().getEG()[0]
            x2 = self.getG().getEG()[1]
            Cas_Dec = self.getG().CD
            if(self.getG().getVar()=='F'):
                corda1[choice(range(self.getMAX()))] = randint(x1,x2-1)+(randint(0,10**Cas_Dec)/10**Cas_Dec)
            else:
                corda1[choice(range(self.getMAX()))] = cord.append(randint(x1,x2))

        fator_mutacao = choice(range(1,100000))/1000
        if(fator_mutacao <= self.getMut()):
            x1 = self.getG().getEG()[0]
            x2 = self.getG().getEG()[1]
            Cas_Dec = self.getG().CD
            if(self.getG().getVar()=='F'):
                corda2[choice(range(self.getMAX()))] = randint(x1,x2-1)+(randint(0,10**Cas_Dec)/10**Cas_Dec)
            else:
                corda2[choice(range(self.getMAX()))] = cord.append(randint(x1,x2))
           
        return corda1, corda2

    def __str__(self):
        
            return ("\n"+"Pontuacao: "+str(self.getPont()))
        
    def __eq__(self,Cromossomo):
        return self.getCorda() == Cromossomo.getCorda()
    
    def __lt__(self,Cromossomo):
        return self.getPont() < Cromossomo.getPont()


class MaquinaGenetica(object):
        
        def __init__(self,G,MX = -1,populacao = [],size = 50,p_DeadCromossomo = 40,El = 10):
                self.populacao = populacao
                self.size = size
                self.geracao = 0
                self.G = G
                self.p_DeadCromossomo = p_DeadCromossomo
                self.MX = MX
                self.El = El
                
        def getPop(self):
                return self.populacao

        def getMX(self):
                return self.MX
        
        def getPDC(self):
            return self.p_DeadCromossomo

        def getSize(self):
                return self.size

        def getGer(self):
                return self.geracao

        def getGene(self):
            return self.G

        def setGer(self,geracao):
                self.geracao = geracao
        def adaptar(self):
            lista = list(self.getPop())
            lista.sort()
            fdc = int((self.getPDC()/100)*self.getSize())
            for i in lista[0:fdc]:
                self.populacao[self.populacao.index(i)] = choice(lista[fdc:len(lista)])
                
        def selecao(self):
            Mutation = self.getPop()[0].getMut()
            lista = []
            self.adaptar()
            for _ in range(int((self.getSize()/2))):
                x = choice(self.getPop())
                y = choice(self.getPop())
                cx,cy = x.cross(y)
                Cx = Cromossomo(self.getGene(),self.getMX(),cx)
                Cy = Cromossomo(self.getGene(),self.getMX(),cy)
                #Cx.setPont(max(x.getPont(),y.getPont()))
                #Cy.setPont(max(x.getPont(),y.getPont()))
                lista.append(Cx)
                lista.append(Cy)
                
            self.populacao = lista
            self.setGer(self.getGer()+1)
        
        def add(self,Cromossomo):#
            self.populacao.append(Cromossomo)
            if(len(self.getPop())==1):
                self.MX = self.getPop()[0].getMAX()

        def __str__(self):
           
            return ("Geracao: "+str(self.getGer()))
            
            


#modificar a parte da classe
#Estudar dicionarios para modificar ainda mais a classe
