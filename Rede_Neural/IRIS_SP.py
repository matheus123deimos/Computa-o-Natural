from Neural_Network_Implematation import S_Perceptron
from random import *
import matplotlib.pyplot as plt

file = open('iris.txt','r')
INsB = []
INsC = []
EPOCA_1 = []
EPOCA_2 = []
EPOCA_3 = []
EPOCA_4 = []
EPOCA_5 = []
EPOCA_6 = []
EPOCA_7 = []
EPOCA_8 = []
EPOCA_9 = []
EPOCA_10 = []
LIS_AUX = []
TB = {}

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


for i in range(len(INsB)):
    TB[str(INsB[i])] = INsC[i]
    
    


LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_1.append(Aux)


LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_2.append(Aux)

LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_3.append(Aux)

LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_4.append(Aux)
    
LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_5.append(Aux)
    
LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_6.append(Aux)
    
LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_7.append(Aux)
    
LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_8.append(Aux)
    
LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_9.append(Aux)
    
LIS_AUX = list(INsB)

while(len(LIS_AUX)>0):
    Aux = []
    E1 = choice(LIS_AUX)
    Aux.append(E1)
    LIS_AUX.remove(E1)
    E2 = choice(LIS_AUX)
    Aux.append(E2)
    LIS_AUX.remove(E2)
    E3 = choice(LIS_AUX)
    Aux.append(E3)
    LIS_AUX.remove(E3)
    E4 = choice(LIS_AUX)
    Aux.append(E4)
    LIS_AUX.remove(E4)
    E5 = choice(LIS_AUX)
    Aux.append(E5)
    LIS_AUX.remove(E5)
    E6 = choice(LIS_AUX)
    Aux.append(E6)
    LIS_AUX.remove(E6)
    E7 = choice(LIS_AUX)
    Aux.append(E7)
    LIS_AUX.remove(E7)
    EPOCA_10.append(Aux)


IRIS = S_Perceptron(4,2,1.0)

IRIS.learning([EPOCA_1,EPOCA_2,EPOCA_3,EPOCA_4,EPOCA_5,EPOCA_6,EPOCA_7,EPOCA_8,EPOCA_9,EPOCA_10],TB)


file = open('bezdekIris.txt','r')

INsB = []
INsC = []
for linha in file:
    if linha != '\n':
        
        Aux = linha.split(',')
        
        for i in range(len(Aux)-1):
                Aux[i] = float(Aux[i])
                
        if(not(Aux[0:4] in INsB)):
            if(Aux[4][5] == 's'):Aux[4] = [0.0,0.0]
            elif(Aux[4][6] == 'e'): Aux[4] = [0.0,1.0]
            else: Aux[4] = [1.0,1.0]
            INsB.append(Aux[0:4])
            INsC.append(Aux[4])
            


for i in range(len(INsB)):
    TB[str(INsB[i])] = INsC[i]

P_Setosa = 0
#P_Versi_Virgi = 0
P_Versi = 0
P_Virgi = 0
x = 0
y = 0
z = 0

for inp in INsB:
    
    if(IRIS.usar(inp) == [0.0,0.0] and TB[str(inp)] == [0.0,0.0]):
        x += 1
        
    if(IRIS.usar(inp) == [0.0,1.0] and TB[str(inp)] == [0.0,1.0]):
        y+=1
        
    if(IRIS.usar(inp) == [1.0,1.0] and TB[str(inp)] == [1.0,1.0]):
        z+=1

P_Setosa = (x/INsC.count([0.0,0.0]))*100
P_Versi = (y/INsC.count([0.0,1.0]))*100
P_Virgi = (z/INsC.count([1.0,1.0]))*100
print(str(P_Setosa))
print(str(P_Versi))
print(str(P_Virgi))    


#Fazer Tabela de pontuações para duas e três classificações
#Tentar achar uma forma de aumentar a precisão dos floats
#achar um dataset mais robusto

