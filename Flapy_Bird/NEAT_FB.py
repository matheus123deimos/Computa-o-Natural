from __future__ import print_function
import matplotlib.pyplot as plt
import os
import neat
import visualize
from numpy import *
from random import *
from flappybird import *

VET_MED =[]
VET_BEST = []
NC = 10

#CENARIO = Cena_Flp(7,0.12)
#CENARIO.preenche()

#Crio um Vetor de Cenários de tamanho 10 com 5 tubos e velocidade 0.12
CENARIO = [Cena_Flp(7,0.12)for _ in range(NC)]

#Preenche cada cenário com os tubos
for i in range(NC):
        CENARIO[i].preenche()
        
def eval_genomes(genomes, config):
    
    VT_NET = []
    SCORE = []# vetor de Scores da população
        
    for genome_id,genome in genomes:#Decoifica os Genomas em Redes
        VT_NET.append(neat.nn.FeedForwardNetwork.create(genome, config))
        
    for net,pair in zip(VT_NET,genomes): 
        score = []
        pont = []
        for i in range(NC):
            P,s  = flappyenv(net,CENARIO[i])# Utilizo a cada rede da população em um conjunto de cenários
            score.append(s)# Guardo os scores (Quantidade de tubos)
            pont.append(P)#guardo a pontuação
            
        SCORE.append(median(score))#Adiciono a média dos scores do agente ao vetor de scores da população
        pair[1].fitness = median(pont)#Defino o fitness desse genoma
 
    VET_MED.append(median(SCORE))# Adiciono a média dos scores da população a um vetor de médias para plotagem
    VET_BEST.append(max(SCORE))#Busco o que obteve o maior score e guardo pra plotagem
    print(max(SCORE))
    print(median(SCORE))
         
def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)


    p = neat.Population(config) #Defino a população de genomas

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    
    winner = p.run(eval_genomes,150) #Retorna o melhor depois de 150 gerações

    print('\nBest genome:\n{!s}'.format(winner))

   
    node_names = {-2:'D_X',-1:'D_Y',0:'Prob'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    #visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    #plotagem do grafico da Média das Pontuações
    plt.plot(list(range(1,len(VET_MED)+1)),VET_MED,linewidth=2,color = 'blue')
    plt.plot(list(range(1,len(VET_BEST)+1)),VET_BEST,linewidth=2,color = 'red')
    plt.title("Graficos",fontsize=24)
    plt.xlabel("GERACAO",fontsize=14)
    plt.ylabel("P_M&P_B/Geracao",fontsize=14)
    plt.tick_params(axis='both',which = 'major',labelsize=5)
    plt.axis([1,(len(VET_MED)+1),0,5.1],fontsize=25)
    plt.savefig('G.png') 
    plt.show()

    #plotagem do grafico do Melhor Fenótipo
    '''plt.plot(list(range(1,len(VET_BEST)+1)),VET_BEST,linewidth=2,color = 'red')
    plt.title("Grafico do Melhor Fenotipo",fontsize=24)
    plt.xlabel("GERACAO",fontsize=14)
    plt.ylabel("Melhor_Pont/Geracao",fontsize=14)
    plt.tick_params(axis='both',which = 'major',labelsize=5)
    plt.axis([1,(len(VET_BEST)+1),0,5],fontsize=25)
    plt.savefig('Melhor.png') 
    plt.show()'''
 


if __name__ == '__main__':
 
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward_flappy')
    run(config_path)

#survival_threshold 0.10 - 0.20
#Depois Tentar entender tanto essa parte do __main__ quando o modulo visualize, 
#e a nn dessa neat

#Atenção a essa forma que eu faço esse fitness
#ao final guardar o mais avaliado e utilizarmais tarde
