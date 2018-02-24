from numpy import *
from math import *
from random import *

#Rede Sigmoidal => No Futuro Substituir por Linear(tangete hiperbólica)
#Normalizar os dados antes de mandar pra rede

class RN_FFW(object):
    
    def __init__(self,LM_Pesos,Ident_Cam):
        self.Ident_Cam = Ident_Cam
        self.n_in = Ident_Cam[0]
        self.n_out = Ident_Cam[len(Ident_Cam)-1]
        self.LM_Pesos = LM_Pesos
        

    def Ativar_Rede(self):
        LM_Pesos = []
        for i in range(len(self.Ident_Cam)-1):
            M = zeros((self.Ident_Cam[i+1],self.Ident_Cam[i]))
            LM_Pesos.append(M)
        self.LM_Pesos = LM_Pesos


    def Func_Atv(self,IN,MP):
        return array([dot(IN,linha) for linha in MP])
        
    def Func_Trans(self,IN):
        L = []
        #return array([1/(1+exp(-A))  for A in list(IN)])
        return array([tanh(A) for A in list(IN)])

    def FeedForward(self,IN):#Botar o Valor Esperado como argumento
        Result = array(IN)
        for i in range(len(self.LM_Pesos)):
            In = self.Func_Atv(Result,self.LM_Pesos[i])
            Result = self.Func_Trans(In)
        return Result
        

    def set_LMP(self,modificacao,i):
        if(i<0):
            self.LM_Pesos = modificacao

        else:
            self.LM_Pesos[i] = modificacao

