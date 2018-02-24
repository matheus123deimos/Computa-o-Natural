from gene import *
from Rede_Neural_FFW_SB import *
from random import *
import matplotlib.pyplot as plt

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


#Instâncias para Teste

INsB = []
INsC = []
INsD = []
INsE = []
INsF = []
INsG = []

TB1  = {}
TB2  = {}
TB3  = {}


INsA1 = []
INsA2 = []


INsH = []
INsI = []
TBT = {}

POPULACAO = 60
IDENT_CAM = (4,5,2)
GENE = Gene((0,1),'F',4)
MUT =  5
PROB = 10
MAX = 0
QT = 1

for i in range(len(IDENT_CAM)-1):
    MAX += IDENT_CAM[i]*IDENT_CAM[i+1]

#tratamento do data_set ex2data1
file = open('iris.txt','r')
for linha in file: 
    if linha != '\n':
        Aux = linha.split(',')
        for i in range(len(Aux)-1):
                Aux[i] = float(Aux[i])
        if(not(Aux[0:4] in INsB or Aux[0:4] in INsD or Aux[0:4] in INsF)):
            if(Aux[4][5] == 's'):
                Aux[4] = [1.0,1.0]
                INsB.append(Aux[0:4])
                INsC.append(Aux[4])
            elif(Aux[4][6] == 'i'):
                Aux[4] = [0.0,0.0]
                INsD.append(Aux[0:4])
                INsE.append(Aux[4])
            else:
                #continue
                Aux[4] = [1.0,0.0]
                INsF.append(Aux[0:4])
                INsG.append(Aux[4])
            #else: Aux[4] = [1.0,1.0]

#tratamento do teste         
file = open('bezdekIris.txt','r')
for linha in file: 
    if linha != '\n':
        Aux = linha.split(',')
        for i in range(len(Aux)-1):
                Aux[i] = float(Aux[i])
        if(not(Aux[0:4] in INsH)):
            if(Aux[4][5] == 's'):
                Aux[4] = [1.0,1.0]
                INsH.append(Aux[0:4])
                INsI.append(Aux[4])
            elif(Aux[4][6] == 'i'):
                Aux[4] = [0.0,0.0]
                INsH.append(Aux[0:4])
                INsI.append(Aux[4])
            else:
                #continue
                Aux[4] = [1.0,0.0]
                INsH.append(Aux[0:4])
                INsI.append(Aux[4])
            
#criacao da Tabela_de_Aprendizado
for i in range(len(INsB)):
    TB1[str(INsB[i])] = INsC[i]
for i in range(len(INsD)):
    TB2[str(INsD[i])] = INsE[i]
for i in range(len(INsF)):
    TB3[str(INsF[i])] = INsG[i]

#Criação das Tabela_de_Teste
for i in range(len(INsH)):
    TBT[str(INsH[i])] = INsI[i]

#Instanciação da Rede_Neural_FeedForWard e da Máquina_Genética // Ativação da Rede
RN = RN_FFW([],IDENT_CAM)

MG = MaquinaGenetica(GENE,-1,[],POPULACAO,PROB)

RN.Ativar_Rede()

#Preenchimento da Maquina_Genetica
for _ in range(MG.getSize()):
    MG.add(Cromossomo.preencherC_EG(Cromossomo(GENE,MAX,[],0,MUT)))

#Aprendizado Neuro_Evolutivo

MEDIAS = []
MAIORES = []
MENORES = []
Quant = []
REP = 1

for _ in range(REP):
    shuffle(INsB)
    shuffle(INsD)
    shuffle(INsF)
    shuffle(INsH)
    for i in range(len(INsB)+len(INsD)+len(INsF)):
        PONT = []
        Inst1 = choice(INsB)
        Inst2 = choice(INsD)
        Inst3 = choice(INsF)
        for Cro in MG.getPop():
            LMP = Decodec(Cro,RN)
            RN.set_LMP(LMP,-1)
            OUTPUT1 = RN.FeedForward(Inst1)
            OUTPUT2 = RN.FeedForward(Inst2)
            OUTPUT3 = RN.FeedForward(Inst3)
            ERRO1 = sum(0.5*((array(TB1[str(Inst1)])-OUTPUT1)**2))
            ERRO2 = sum(0.5*((array(TB2[str(Inst2)])-OUTPUT2)**2))
            ERRO3 = sum(0.5*((array(TB3[str(Inst3)])-OUTPUT3)**2))
            ERRO = (ERRO1*ERRO2*ERRO3)**(1/3)
            PONT.append(-ERRO)
            Cro.setPont(-ERRO)
            
        MEDIAS.append(median(PONT))
        MAIORES.append(max(MG.getPop()).getPont())
        MENORES.append(min(MG.getPop()).getPont())
        MG.selecao()

        QUANT = 0
        Inst = choice(INsH)
        for Cro in MG.getPop():
            LMP = Decodec(Cro,RN)
            RN.set_LMP(LMP,-1)
            OUT = RN.FeedForward(Inst)
            out = (OUT[0]+OUT[1])/2
            CLASS = []
            SORT1 = randint(0,100)/100
            SORT2 = randint(0,100)/100
            Val1 = 1.0 if SORT1<=out else 0.0
            Val2 = 1.0 if SORT2<=out else 0.0
            CLASS = array([Val1,Val2])
            TRUE = array(TBT[str(Inst)])
            if(CLASS[0] == TRUE[0] and CLASS[1] == TRUE[1]):QUANT+=1
        
        Quant.append(QUANT)
#plotagem do grafico da Média das Pontuações
plt.plot(list(range(1,(len(INsB)+len(INsD)+len(INsF))*REP+1)),MEDIAS,linewidth=2)
plt.title("Grafico da Pontuacao Media",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Pontuacao_Media/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.show()

#plotagem dos gráficos de Melhor da Geracao e Pior da Geracao
plt.plot(list(range(1,(len(INsB)+len(INsD)+len(INsF))*REP+1)),MAIORES,linewidth=2)
plt.plot(list(range(1,(len(INsB)+len(INsD)+len(INsF))*REP+1)),MENORES,linewidth=2,color='red')
#plt.legend(['maior','menor'],lab=2)
plt.title("Maiores e Menores por Geracao",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Pontuacao/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.show()


#plotagem do grafico de Acertos 
plt.plot(list(range(1,(len(INsB)+len(INsD)+len(INsF))*REP+1)),Quant,linewidth=2)
plt.title("Grafico dos Acertos",fontsize=24)
plt.xlabel("GERACAO",fontsize=14)
plt.ylabel("Acertos/Geracao",fontsize=14)
plt.tick_params(axis='both',which = 'major',labelsize=5)
plt.show()

'''
for Cro in MG.getPop():    
    LM = Decodec(Cro,RN)
    RN.set_LMP(LM,-1)

    OUT1 = RN.FeedForward([5.1,3.5,1.4,0.2])
    CLASS = []
    SORT1 = randint(0,100)/100
    SORT2 = randint(0,100)/100
    Val1 = 1.0 if SORT1<=OUT1[0]*OUT1[1] else 0.0
    Val2 = 1.0 if SORT2<=OUT1[1]*OUT1[0] else 0.0
    CLASS = [Val1,Val2]
    print(OUT1)
    seed(20)
    OUT2 = RN.FeedForward([6.1,2.8,4.0,1.3])
    CLASS = []
    SORT3 = randint(0,100)/100
    SORT4 = randint(0,100)/100
    Val1 = 1.0 if SORT3<=OUT2[0]*OUT2[1] else 0.0
    Val2 = 1.0 if SORT4<=OUT2[1]*OUT2[0] else 0.0
    CLASS = [Val1,Val2]
    print(OUT2)
    seed(30)
    OUT3 = RN.FeedForward([6.3,3.4,5.6,2.4])
    CLASS = []
    SORT5 = randint(0,100)/100
    SORT6 = randint(0,100)/100
    Val1 = 1.0 if SORT5<=OUT3[0]*OUT3[1] else 0.0
    Val2 = 1.0 if SORT6<=OUT3[1]*OUT3[0] else 0.0
    CLASS = [Val1,Val2]
    print(OUT3)
    print("\n\n")'''
     
#5.1,3.5,1.4,0.2 Setosa
#6.1,2.8,4.0,1.3 Versicolor
#6.3,3.4,5.6,2.4 Virginica
