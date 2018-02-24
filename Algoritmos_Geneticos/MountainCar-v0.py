from gene import *

EG = []
recompensaCromossomo = -6
aux = 0 
cont = 0
OB = False
Lista_Objetivo = []
    
for i in range(3):
   EG.append(i)
EG = tuple(EG)
    
MG = MaquinaGenetica(Gene(EG),2000,[],5)
for _ in range(MG.getSize()):
    MG.add(Cromossomo.preencher_C(Cromossomo(MG.getGene(),MG.getMX())))
        
env = gym.make('MountainCar-v0')
env.reset()
    
    
print("\n")
print(MG)
print("\n")
    
    
#for _ in range(50):
for _ in range(1):
    for Cro in MG.getPop():
        cont += 1
        for gene in Cro.getCorda():
            env.render()
            visao, r, done, z = env.step(gene)
            altura,k = visao
            if(altura > recompensaCromossomo):
                recompensaCromossomo = altura  
            if(altura == 0.6):
                aux += 1
                OB = True
                break
           
        Cro.setPont(recompensaCromossomo)
        print("\nCromossomo"+str(cont))
        if(OB):
            print(Cro)
            print(MG)
            print("OB"+ " // " +"Q_OBj: " + str(aux))
                
        else:
            print(Cro)
            print(MG)
            print("NOB"+ " // " +"Q_OBj: " + str(aux))
                
        recompensaCromossomo = -6
        OB = False
        env.reset()
        
    Lista_Objetivo.append(aux)
    print("\n\nNumero de Objetivos Atingidos: " + str(aux) + "\n\n")
    aux = 0
    cont = 0
    MG.selecao()
    env.reset()
    print("\n")
    print(MG)
    print("\n")

#print("\n\n" + str(Lista_Objetivo)+ "\n\n")
#x = input("Digite Enter para encerrar: ")
#if(x == '\n'):
#exit(0)
#if __name__ == "__main__":
    #main()

#Utilizar matploit para gerar gráficos das média das frequências do conjunto de ações


