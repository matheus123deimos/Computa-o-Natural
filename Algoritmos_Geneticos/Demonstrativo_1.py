from gene import *
from Rede_Neural_FFW import *

def Decodec(Cromossomo):
    LMP = []
    LVB = []
    for i in range(len(Cromossomo.getG().getIR())-1):
        M = zeros((Cromossomo.getG().getIR()[i+1],Cromossomo.getG().getIR()[i]))
        B = array([0.0 for j in range(Cromossomo.getG().getIR()[i+1])])
        LMP.append(M)
        LVB.append(B)
        
    for Conec in Cromossomo.corda:
        if(len(Conec)==4):
            Camada = Conec["Mtz"]
            ND = Conec["ND"]
            NE = Conec["NE"]
            LMP[Camada][ND][NE] += Conec["Peso"]
        else:
            Camada = Conec["Vt"]
            NR = Conec["NR"]
            LVB[Camada][NR] += Conec["Peso"]
    
    return LMP,LVB

BIAS = 1
POPULACAO = 10
IDENT_CAM = (2,3,1)
MUTACAO = 10
PROB = 100
ELITISMO  = 10

#Instanciação da Rede_Neural_FeedForWard e da Máquina_Genética // Ativação da Rede
RN = RN_FFW(BIAS,[],[],IDENT_CAM)

MG = MaquinaGenetica(Gene.Neuro_Gene(RN.Ident_Cam),-1,[],POPULACAO,PROB,ELITISMO)

RN.Ativar_Rede()

#Preenchimento da Maquina_Genetica
for _ in range(MG.getSize()):
    MG.add(Cromossomo.preencherC_NG(Cromossomo.Neuro_Crom(MUTACAO,[],RN.Ident_Cam)))

for i in range(len(MG.getPop())):
    MG.getPop()[i].pont = (randint(0,100000)/100000)

for i in MG.getPop():
    print(i)

MG.selecao()

print("\n\n")

for i in MG.getPop():
    print(i)


'''print(MG.getPop()[1].getCorda())
LMP, LVB = Decodec(MG.getPop()[1])
print("\n\n")
print(LMP)
    
#Estou pegando cada cromossomo e fazendo ele classificar os valores
#E obter os erros
#Será que o problema não está na forma que eu apresento o data_set para os
#cromossomos,deveria ter repetições, ordem aleatória do data_set
#será que o problema não estaá na seleção, deveria ser outra, ou na codi-
#ficação, deveria ser uma população de neurônios e somente uma pontuação
    
print(LVB)'''
