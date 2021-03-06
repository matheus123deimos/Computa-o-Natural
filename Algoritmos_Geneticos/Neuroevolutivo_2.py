from gene import *
from Rede_Neural_FFW_SB import *
from random import *
import matplotlib.pyplot as plt

#Não há o uso de pesos negativos, isso poderia ser um problema?

#FUNÇÃO DE DECODIFICAÇÃO

def Decodec(C,R):
    LMP = []
    Cr = list(C.getCorda())
    for i in range(len(R.Ident_Cam)-1):
        M = zeros((R.Ident_Cam[i+1],R.Ident_Cam[i]))
        LMP.append(M)
        
    for i in range(len(LMP)):
        for j in range(len(LMP[i])):
            for k in range(len(LMP[i][j])):
                LMP[i][j][k] = Cr[0]
                del(Cr[0])
    
    return LMP


#VARIÁVEIS e PARÂMETROS

INsB = []
INsC = []
T = []
TB = {}

D1 = []
D2 = []

AM = []
BM = []
CM = []

AD = []
BD = []
CD = []

am = 0
bm = 0
cm = 0

ad = 0
bd = 0
cd = 0


POPULACAO =100
IDENT_CAM = (3,4,1)
GENE = Gene((0,1),'F',4)
MUT =  2.25
TRUNC = 85
MAX = 0
QT = 1

MEDIAS = []
MA = []
MI = []
a1 = []
a2 = []
REP = 1
TESTE = 40

for i in range(len(IDENT_CAM)-1):
    MAX += IDENT_CAM[i]*IDENT_CAM[i+1]

#TRATAMENTO DATA_SET
    
file = open('Data_Set_Alt.txt','r')
for linha in file:
        if(linha!='\n'):
            Aux = linha[0:len(linha)-1].split(',')
            for i in range(len(Aux)):
                    Aux[i] = float(Aux[i])
            if(Aux[3] == 1):
                INsB.append(Aux[0:3])
                INsC.append([-1.0])
            else:
                INsB.append(Aux[0:3])
                INsC.append([1.0])

    
#NORMALIZAÇÃO DOS DADOS
    
for In in INsB:
    AM.append(In[0])
    BM.append(In[1])
    CM.append(In[2])
    
am = median(AM)
bm = median(BM)
cm = median(CM)
ad = std(AM)
bd = std(BM)
cd = std(CM)

for i in range(len(INsB)):
    Za=Zb=Zc=0
    Za = (INsB[i][0]-am)/ad
    Zb = (INsB[i][1]-bm)/bd
    Zc = (INsB[i][2]-cm)/cd
    INsB[i] = [Za,Zb,Zc]


#TABELA DE APRENDIZADO
                
for i in range(len(INsB)):
    TB[str(INsB[i])] = INsC[i]

#Instanciação da Rede_Neural_FeedForWard e da Máquina_Genética // Ativação da Rede
                
RN = RN_FFW([],IDENT_CAM)

MG = MaquinaGenetica(GENE,-1,[],POPULACAO,TRUNC)

RN.Ativar_Rede()

#PREENCHIMENTO DA MÁQUINA_GENÈTICA

for _ in range(MG.getSize()):
    MG.add(Cromossomo.preencherC_EG(Cromossomo(GENE,MAX,[],0,MUT)))
     

#SEPARAÇÂO DO DATA_SET

for D in INsB:
    if(TB[str(D)]==[-1.0]):
        D1.append(D)
    else:
        D2.append(D)
        
#T1 = [D1[i] for i in range(int(len(D1)/2))] 
#T2 = [D2[i] for i in range(int(len(D2)/2))]
#D1 = [D1[i] for i in range(int(len(D1)/2),len(D1))]
#D2 = [D2[i] for i in range(int(len(D2)/2),len(D2))]

#APRENDIZADO NEURO_EVOLUTIVO

for _ in range(REP):
    for i in range(len(INsB)):
    
        PONT1 = []
        PONT2 = []
        P1 = []
        P2 = []
        
        OUT1 = [choice(D1) for _ in range(int(TESTE/2))]
        OUT2 = [choice(D2) for _ in range(int(TESTE/2))]
        #t1 =   [choice(T1) for _ in range(int(TESTE/2))]
        #t2 =   [choice(T2) for _ in range(int(TESTE/2))]
        
        #Aprendizado
        
        for Cro in MG.getPop():
            A1 = 0
            A2 = 0
            for i in range(int(TESTE/2)):
                LMP = Decodec(Cro,RN)
                RN.set_LMP(LMP,-1)
                out1 = RN.FeedForward(OUT1[i])
                out2 = RN.FeedForward(OUT2[i])
                if(out1[0]<=0.0):
                    A1+=1
                if(out2[0]>=0.0):
                    A2+=1
            
            PONT1.append((A1+A2)/TESTE)
            P1.append(2*A1/TESTE)
            P2.append(2*A2/TESTE)
            Cro.setPont((A1+A2)/TESTE)
        
        #Teste
        '''
        for Cro in MG.getPop():
            A1 = 0
            A2 = 0
            for i in range(int(TESTE/2)):
                LMP = Decodec(Cro,RN)
                RN.set_LMP(LMP,-1)
                out1 = RN.FeedForward(t1[i])
                out2 = RN.FeedForward(t2[i])
                if(out1[0]<=0.0):
                    A1+=1

                if(out2[0]>=0.0):
                    A2+=1
            
            PONT2.append((A1+A2)/TESTE)
        '''  
        MEDIAS.append(median(PONT1))
        a1.append(median(P1))
        a2.append(median(P2))
        #T.append(median(PONT2))
        MA.append(max(MG.getPop()).getPont())
        MI.append(min(MG.getPop()).getPont())
        
        MG.selecao()

    
#plotagem do grafico da Média das Pontuações
plt.plot(list(range(1,(len(INsB))*REP+1)),MEDIAS,linewidth=2)
plt.title("Grafico da Pontuacao Media",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Pontuacao_Media/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.axis([1,(len(INsB)*REP+1),0,1],fontsize=25)
plt.show()

#plotagem do grafico da Média das Pontuações A1
plt.plot(list(range(1,(len(INsB))*REP+1)),a1,linewidth=2)
plt.title("Grafico da Pontuacao Media A1",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Pontuacao_Media/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.axis([1,(len(INsB)*REP+1),0,1],fontsize=25)
plt.show()

#plotagem do grafico da Média das Pontuações A2
plt.plot(list(range(1,(len(INsB))*REP+1)),a2,linewidth=2)
plt.title("Grafico da Pontuacao Media A2",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Pontuacao_Media/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.axis([1,(len(INsB)*REP+1),0,1],fontsize=25)
plt.show()

#plotagem dos gráficos de Melhor da Geracao e Pior da Geracao
plt.plot(list(range(1,(len(INsB))*REP+1)),MA,linewidth=2)
plt.plot(list(range(1,(len(INsB))*REP+1)),MI,linewidth=2,color='red')
#plt.legend(['maior','menor'],lab=2)
plt.title("Maiores e Menores por Geracao",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Pontuacao/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.axis([1,(len(INsB)*REP+1),0,1],fontsize=25)
plt.show()
'''
#plotagem do grafico de Teste
plt.plot(list(range(1,(len(INsB))*REP+1)),T,linewidth=2)
#plt.legend(['maior','menor'],lab=2)
plt.title("Grafico de Teste",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Pontuacao_Media/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.axis([1,(len(INsB)*REP+1),0,1],fontsize=25)
plt.show()
'''

