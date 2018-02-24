from Neural_Network_Implematation import M_Perceptron
from random import shuffle

INsB = []
INsC = []
EPOCA_L = []
TESTE_L = []
TB = {}
TBT = {}
NUMERO_DE_EPOCAS = 200

CAMADAS_OCULTAS= 1
TAXA_DE_APRENDIZADO= 0.935
CONSTANTE_DE_MOMENTO= 0.0
VARIANTE_DE_TRANSFERENCIA=3
INTERVALO_DOS_PESOS= 5

file = open('ex2data1.txt','r')
for linha in file:
        if(linha!='\n'):
            Aux = linha[0:len(linha)-1].split(',')
            for i in range(len(Aux)):
                    Aux[i] = float(Aux[i])
            INsB.append(Aux[0:2])
            if(Aux[2] == 0):
                    INsC.append(1.0)
            else:
                    INsC.append(-1.0)


LIS_AUX = list(INsB)

for _ in range(NUMERO_DE_EPOCAS):
    APR = LIS_AUX[0:70]
    shuffle(APR)
    #if(not(LIS_AUX in EPOCA_L)):
    EPOCA_L.append(APR)
    
for _ in range(NUMERO_DE_EPOCAS):
    TEST = LIS_AUX[70:100]
    shuffle(TEST)
    #if(not(LIS_AUX in EPOCA_L)):
    TESTE_L.append(TEST)

for i in range(len(INsB[0:70])):
    TB[str(INsB[i])] = INsC[i]


for i in range(30):
    TBT[str(INsB[len(INsB)-(i+1)])] = INsC[len(INsB)-(i+1)]
    

PARAMETROS = (CAMADAS_OCULTAS,TAXA_DE_APRENDIZADO,CONSTANTE_DE_MOMENTO,VARIANTE_DE_TRANSFERENCIA,INTERVALO_DOS_PESOS)

# 1 - SIGMOIDE
# 2 - TANGENTE_HIPERBOLICA
# 3 - GAUSSIANA

IRIS = M_Perceptron(2,1,PARAMETROS,TB)
IRIS.learning_teste(EPOCA_L,TESTE_L,TBT,)

