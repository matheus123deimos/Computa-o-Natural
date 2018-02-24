#python Neural_Network_Implematation_1.py
from numpy import *
from math import *
import matplotlib.pyplot as plt
from decimal import Decimal
from random import *


class S_Perceptron(object):

    def __init__(self,inputs,outputs,T_learn):#por emquanto o usuario nÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£o ira iniciar os pesos
        self.inputs = inputs
        self.outputs = outputs
        self.Vect_Hv = zeros((self.outputs,self.inputs +1))# O 1 ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© do bias
        self.T_learn = T_learn


    def activ_funct(self,Pesos,Entradas):#tentar ver se ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© possÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­vel implementar um produto com a transposta
        return dot(Pesos,Entradas)


    def transf_funct(self,AF):
        if(AF<=0.0):return 0.0
        return 1.0


    #IrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ ser usado o aprendizado em sequÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia; baies = 1; vetorr de pesos ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© inicializado com  0; MÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©todo de CorreÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£o de Erros
    def learning(self,EPOCA_L,TB):
        EM =[]

        for EPOCA in EPOCA_L:
            for CICLO in EPOCA:#Tentar ver se Existe forma mais simples
                In_Ln = []
                em = Decimal('0.0')
                for In in CICLO:
                    In_Ln.append(array([1]+In))
                i = 0
                for VIN in In_Ln:
                    Fator_Correct = zeros((self.outputs,self.inputs +1))
                    OUT = array([0 for i in range(self.outputs)])

                    for j in range(self.outputs): #Processo de IN/OUT
                        AF = self.activ_funct(self.Vect_Hv[j],VIN)
                        OUT[j] = self.transf_funct(AF)

                    REFERENCIA = array(TB[str(CICLO[i])])
                    Erro = REFERENCIA - OUT#Vetor de Erro

                    for j in range(self.outputs):
                        Fator_Correct[j] += (VIN*self.T_learn*Erro[j])

                    self.Vect_Hv += Fator_Correct #CorreÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â£o dos Pesos
                    em +=(Decimal(str(sum(abs(Erro))))/Decimal(str(self.outputs)))
                    i += 1
                EM_D = em/Decimal(str(self.outputs))
                EM.append(float(EM_D))#fazer o erro por ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©poca



        #plotagem dos graficos
        plt.plot(list(range(1,len(EM)+1)),EM,linewidth=2)
        plt.title("Grafico de Aprendizado",fontsize=24)
        plt.xlabel("Iteracoes",fontsize=14)
        plt.ylabel("Erro_Medio/CICLO",fontsize=14)

        plt.tick_params(axis='both',which = 'major',labelsize=5)
        plt.show()


    def usar(self,IN):
        In = array([1]+IN)
        OUT = []
        for out in range(self.outputs):
            AF = self.activ_funct(self.Vect_Hv[out],In)
            OUT.append(self.transf_funct(AF))

        return OUT

#Criar no Futuro um MÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©todo de Teste
#MELHORAR O SINGULAIER PERCEPTRON UTILIZANDO O QUE FOI FEITO NO MULTILAIER
#MELHORAR O SINGULAIER PERCEPTRON UTILIZANDO O QUE FOI FEITO NO MULTILAIER
#MELHORAR O SINGULAIER PERCEPTRON UTILIZANDO O QUE FOI FEITO NO MULTILAIER
#MELHORAR O SINGULAIER PERCEPTRON UTILIZANDO O QUE FOI FEITO NO MULTILAIER
#MELHORAR O SINGULAIER PERCEPTRON UTILIZANDO O QUE FOI FEITO NO MULTILAIER
#def __str__(self):
#Modificar o s_perceptron com as ideias que eu tive para o m_perceptron, inclusive fazer erro por epoca
#e tirar esse negÃƒÆ’Ã‚Â³cio de ciclo
#Lembrar se ÃƒÆ’Ã‚Â© possÃƒÆ’Ã‚Â­vel fazer utilizando a transposta

class M_Perceptron(object):

    def __init__(self,inp,outp,PR,TB):
        L_cam = []
        for i in range(PR[0]+2):
            if(i==0):
                V_In = array([0.0 for i in range(inp)])
                L_cam.append(V_In)
                
            elif(i<=PR[0] and i>0):
                if(i==1):
                    Peso = zeros((PR[6],inp+1))
                    CORRECAO = zeros((PR[6],inp+1))
                    V_at = array([0.0 for i in range(PR[6])])
                    V_tr = array([0.0 for i in range(PR[6])])
                    V_grad_L = array([0.0 for i in range(PR[6])])
                    for j in range(PR[6]):
                        Peso[j] += array([choice([float(i) for i in range(-PR[4],PR[4])]) for _ in range(inp+1)])

                    L_cam.append([Peso,V_at,V_tr,V_grad_L,CORRECAO])

                else:
                    Peso = zeros((PR[6],PR[6]+1))
                    CORRECAO = zeros((PR[6],PR[6]+1))
                    V_at = array([0.0 for i in range(PR[6])])
                    V_tr = array([0.0 for i in range(PR[6])])
                    V_grad_L = array([0.0 for i in range(PR[6])])
                    for j in range(PR[6]):
                        Peso[j] += array([choice([float(i) for i in range(-PR[4],PR[4])]) for _ in range(PR[6]+1)])

                    L_cam.append([Peso,V_at,V_tr,V_grad_L,CORRECAO])

            else:
                Peso = zeros((outp,PR[6]+1))
                CORRECAO = zeros((outp,PR[6]+1))
                V_at = array([0.0 for i in range(outp)])
                V_tr = array([0.0 for i in range(outp)])
                V_grad_L = array([0.0 for i in range(outp)])
                for j in range(outp):
                    Peso[j] += array([choice([float(i) for i in range(-PR[4],PR[4])]) for _ in range(PR[6]+1)])

                L_cam.append([Peso,V_at,V_tr,V_grad_L,CORRECAO])

        
        self.L_Cam = L_cam
        self.PR= PR
        self.inp = inp
        self.outp = outp
        self.TB = TB

    def activ_funct(self,Pesos,Entrada):
        return array([dot(Pesos[i],Entrada) for i in range(len(Pesos))])

    def transf_funct(self,OP,AF):
        #return array([(1/1+exp(-i)) for i in AF])
        if(OP):
            if(self.PR[3] == 1):
                aux = []
                for i in AF:
                    if(i<0):
                        aux.append(1 - (1/1+exp(i)))
                    else:
                        aux.append(1/1+exp(-i))
                return array(aux)
     
        else:
            return self.PR[3]
                

    def Derivada_TF(self,vr,AF):
        if(vr == 1):
            aux = []
            for i in AF:
                if(i<0):
                    aux.append(exp(i)/pow((1+exp(i)),2))
                else:
                    aux.append(exp(-i)/pow((1+exp(-i)),2))
            return array(aux)
        
    def GRAD_LOC(self,CM,ERRO):
        if(CM!=0):
            if(CM == self.PR[0]+1):
                self.L_Cam[CM][3] = -ERRO*self.Derivada_TF(self.transf_funct(False,0.0),self.L_Cam[CM][1])
            else:
                 Fator_GA = array([dot(self.L_Cam[CM+1][3],array(list(self.L_Cam[CM+1][0][0:len(self.L_Cam[CM+1][2]),i:i+1].T[0]))) for i in range(1,self.PR[6]+1)])
                 self.L_Cam[CM][3] = self.Derivada_TF(self.transf_funct(False,0.0),self.L_Cam[CM][1])*Fator_GA


    def PRO(self,In):
        
        self.L_Cam[0] = array(In)
        self.L_Cam[1][1] = self.activ_funct(self.L_Cam[1][0],array([1.0]+list(self.L_Cam[0])))
        self.L_Cam[1][2] = self.transf_funct(True,self.L_Cam[1][1])
        for i in range(2,self.PR[0]+1):
            self.L_Cam[i][1] = self.activ_funct(self.L_Cam[i][0],array([1.0]+list(self.L_Cam[i-1][2])))
            self.L_Cam[i][2] = self.transf_funct(True,self.L_Cam[i][1])

        self.L_Cam[self.PR[0] +1][1] = self.activ_funct(self.L_Cam[self.PR[0] +1][0],array([1.0]+list(self.L_Cam[self.PR[0]][2])))
        self.L_Cam[self.PR[0] +1][2] = [i for i in self.transf_funct(True,self.L_Cam[self.PR[0] +1][1])]
        REFERENCIA = array(self.TB[str(In)])
        ERRO = REFERENCIA - self.L_Cam[self.PR[0] +1][2]

        return ERRO

    def usar(self,USO):
            OUT = []
            for IN in USO:
                self.L_Cam[0] = array(IN)
                self.L_Cam[1][1] = self.activ_funct(self.L_Cam[1][0],array([1.0]+list(self.L_Cam[0])))
                self.L_Cam[1][2] = self.transf_funct(True,self.L_Cam[1][1])
                for i in range(2,self.PR[0]+1):
                    self.L_Cam[i][1] = self.activ_funct(self.L_Cam[i][0],array([1.0]+list(self.L_Cam[i-1][2])))
                    self.L_Cam[i][2] = self.transf_funct(True,self.L_Cam[i][1])
    
                self.L_Cam[self.PR[0] +1][1] = self.activ_funct(self.L_Cam[self.PR[0] +1][0],array([1.0]+list(self.L_Cam[self.PR[0]][2])))
                self.L_Cam[self.PR[0] +1][2] = [round(i,self.PR[5]) for i in self.transf_funct(True,self.L_Cam[self.PR[0] +1][1])]
                OUT.append(self.L_Cam[self.PR[0]+1][2])
    
            return OUT

    def B_PRO(self,ERRO):
        for i in range(self.PR[0]+1):
            x = self.PR[0] + (1-i)
            self.GRAD_LOC(x,ERRO)
            if(x==1):
                for i in range(len(self.L_Cam[x][1])):
                    self.L_Cam[x][4][i] = [self.L_Cam[x][3][i]*self.PR[1]]+[self.L_Cam[x][3][i]*y*self.PR[1] for y in self.L_Cam[x-1]]+  self.L_Cam[x][4][i]*self.PR[2]
            else:
                for i in range(len(self.L_Cam[x][1])):
                  self.L_Cam[x][4][i] = [self.L_Cam[x][3][i]*self.PR[1]]+[self.L_Cam[x][3][i]*y*self.PR[1] for y in self.L_Cam[x-1][2]] + self.L_Cam[x][4][i]*self.PR[2]
            
            for j in range(len(self.L_Cam[x][0])):
                self.L_Cam[x][0][j] += self.L_Cam[x][4][j]
                                       
        return ERRO


    def learning_teste(self,EPOCA_L,L_TESTE,TBT):
        ERRO_M = []
        PORCENTAGENS = []
        i=0
        for EPOCA in EPOCA_L:
            ERRO = 0.0
            for inp in EPOCA:
                ERRO += sum(0.5*((self.B_PRO(self.PRO(inp)))**2))/len(EPOCA)
            ERRO_M.append(ERRO)
            
            if(i<=len(L_TESTE)-1):
                cont_aux = 0.0
                OUT = self.usar(L_TESTE[i])
                for j in range(len(OUT)):
                    if(all(OUT[j][0] == TBT[str(L_TESTE[i][j])])):
                        cont_aux+=1.0
                PORCENTAGENS.append((cont_aux/len(L_TESTE[i]))*100)
            i+=1
            
        #plotagem do grafico de Aprendizado
        plt.plot(list(range(1,len(EPOCA_L)+1)),ERRO_M,linewidth=2)
        plt.title("Grafico de Aprendizado",fontsize=24)
        plt.xlabel("EPOCA",fontsize=14)
        plt.ylabel("Erro_Medio/EPOCA",fontsize=14)
        plt.tick_params(axis='both',which = 'major',labelsize=5)
        plt.show()
        
        #plotagem do grafico de Teste
        plt.plot(list(range(1,len(PORCENTAGENS)+1)),PORCENTAGENS,linewidth=2)
        plt.title("Grafico de Teste",fontsize=24)
        plt.xlabel("Grupo de Teste",fontsize=14)
        plt.ylabel("Porcentagem de Acertos(%)",fontsize=14)
        plt.tick_params(axis='both',which = 'major',labelsize=5)
        plt.show()




