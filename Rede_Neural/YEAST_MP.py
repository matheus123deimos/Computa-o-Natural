from Neural_Network_Implematation import M_Perceptron
from random import shuffle

#Declarações
AUXILIAR = []
INsB = []
INsC = []
INsD = []
INsE = []
EPOCA_L = []
TESTE_L = []
TB = {}
TBT = {}
NUMERO_DE_EPOCAS = 200
#35 EPOCAS
#1/0.985/0.0/1/3/3/6
#35 EPOCAS
#1/0.995/0.0/1/4/3/7
#Hiper_Parametros
CAMADAS_OCULTAS= 1
TAXA_DE_APRENDIZADO= 0.985
CONSTANTE_DE_MOMENTO= 0.08
VARIANTE_DE_TRANSFERENCIA=1
INTERVALO_DOS_PESOS=5
APROX_CASAS = 3
QNCO = 8

#Dicionarios de Tratamento de Dados(Locais de Presenca de Proteinas)
LPS = { 'CYT':[0.0,0.0,0.0,0.0],'MIT':[0.0,0.0,0.0,1.0],
        'ME3':[0.0,0.0,1.0,0.0],'ME2':[0.0,0.0,1.0,1.0],
        'ME1':[0.0,1.0,0.0,0.0],'EXC':[0.0,1.0,0.0,1.0],
        'VAC':[0.0,1.0,1.0,0.0],'POX':[0.0,1.0,1.0,1.0],
        'ERL':[1.0,0.0,0.0,0.0],'NUC':[1.0,0.0,0.0,1.0]}



#Codigo de preenchimento
file = open('yeast.txt','r')
for linha in file:
    if linha != '\n':
        LINHA = linha.replace('\n','').split('  ')
        while(len(LINHA)>9):
            del(LINHA[0])
        for i in range(len(LINHA)-1):
            LINHA[i] = float(LINHA[i])
        AUXILIAR.append(LINHA)
        
        

for linha in AUXILIAR[0:742]:
    INsB.append(linha[0:8])
    INsC.append(LPS[linha[8]])

for linha in AUXILIAR[742:1484]:
    INsD.append(linha[0:8])
    INsE.append(LPS[linha[8]])


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

YEAST = M_Perceptron(8,4,PARAMETROS,TB)
YEAST.learning_teste(EPOCA_L,TESTE_L,TBT)


