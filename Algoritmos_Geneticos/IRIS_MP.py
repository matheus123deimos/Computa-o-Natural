from Neural_Network_Implematation import M_Perceptron
from random import shuffle

INsB = []
INsC = []
INsD = []
INsE = []
EPOCA_L = []
TESTE_L = []
TB = {}
TBT = {}
NUMERO_DE_EPOCAS = 200

CAMADAS_OCULTAS= 1
TAXA_DE_APRENDIZADO= 0.8
CONSTANTE_DE_MOMENTO= 0.0
VARIANTE_DE_TRANSFERENCIA=1
INTERVALO_DOS_PESOS= 3
APROX_CASAS = 3
QNCO = 6

#tratamento do data_set iris.txt
file = open('iris.txt','r')
for linha in file:
    if linha != '\n':
        Aux = linha.split(',')
        for i in range(len(Aux)-1):
                Aux[i] = float(Aux[i])
        if(not(Aux[0:4] in INsB)):
            if(Aux[4][5] == 's'):Aux[4] = [0.0,0.0]
            elif(Aux[4][6] == 'i'): Aux[4] = [0.0,1.0]
            else: Aux[4] = [1.0,1.0]
            INsB.append(Aux[0:4])
            INsC.append(Aux[4])

#tratamento do data_set bezdekIris.txt
file = open('bezdekIris.txt','r')
for linha in file:
    if linha != '\n':
        Aux = linha.split(',')
        for i in range(len(Aux)-1):
                Aux[i] = float(Aux[i])
        if(not(Aux[0:4] in INsD)):
            if(Aux[4][5] == 's'):Aux[4] = [1.0,1.0]
            elif(Aux[4][6] == 'i'): Aux[4] = [0.0,1.0]
            else: Aux[4] = [0.0,0.0]
            INsD.append(Aux[0:4])
            INsE.append(Aux[4])

LIS_AUX1 = list(INsB)
LIS_AUX2 = list(INsD)

#Criação da Lista_de_Epocas
for _ in range(NUMERO_DE_EPOCAS):
    shuffle(LIS_AUX1)
    #if(not(LIS_AUX in EPOCA_L)):
    EPOCA_L.append(LIS_AUX1)

#Criação da Lista_de_Teste
for _ in range(NUMERO_DE_EPOCAS):
    shuffle(LIS_AUX2)
    #if(not(LIS_AUX in EPOCA_L)):
    TESTE_L.append(LIS_AUX2)

#Criação das Tabela_de_Época
for i in range(len(INsB)):
    TB[str(INsB[i])] = INsC[i]

#Criação das Tabela_de_Teste
for i in range(len(INsD)):
    TBT[str(INsD[i])] = INsE[i]



PARAMETROS = (CAMADAS_OCULTAS,TAXA_DE_APRENDIZADO,CONSTANTE_DE_MOMENTO,VARIANTE_DE_TRANSFERENCIA,INTERVALO_DOS_PESOS,APROX_CASAS,QNCO)

# 1 - SIGMOIDE
# 2 - TANGENTE_HIPERBOLICA
# 3 - GAUSSIANA

IRIS = M_Perceptron(4,2,PARAMETROS,TB)
IRIS.learning_teste(EPOCA_L,TESTE_L,TBT)

