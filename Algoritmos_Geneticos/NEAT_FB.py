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

CENARIO = Cena_Flp(50,0.12)
CENARIO.preenche()

def eval_genomes(genomes, config):
    
    VT_NET = []
    SCORE = []
    
    for genome_id,genome in genomes:
        VT_NET.append(neat.nn.FeedForwardNetwork.create(genome, config))
        
    for net,pair in zip(VT_NET,genomes):
        pair[1].fitness,score  = flappyenv(net,CENARIO)
        print(pair[1].fitness)
        SCORE.append(score)
 
    VET_MED.append(median(SCORE))
    VET_BEST.append(max(SCORE))
    print(max(SCORE))
   
         
def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)


    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    
    winner = p.run(eval_genomes,100)

    print('\nBest genome:\n{!s}'.format(winner))

   
    node_names = {-2:'D_X',-1:'D_Y',0:'Prob'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    #visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    #plotagem do grafico da Média das Pontuações
    plt.plot(list(range(1,len(VET_MED)+1)),VET_MED,linewidth=2,color = 'blue')
    plt.title("Grafico da Pontuacao Media",fontsize=24)
    plt.xlabel("GERACAO",fontsize=14)
    plt.ylabel("Pontuacao_Media/Geracao",fontsize=14)
    plt.tick_params(axis='both',which = 'major',labelsize=5)
    plt.axis([1,(len(VET_MED)+1),0,49],fontsize=25)
    plt.savefig('Media.png') 
    plt.show()

    #plotagem do grafico do Melhor Fenótipo
    plt.plot(list(range(1,len(VET_BEST)+1)),VET_BEST,linewidth=2,color = 'red')
    plt.title("Grafico do Melhor Fenotipo",fontsize=24)
    plt.xlabel("GERACAO",fontsize=14)
    plt.ylabel("Melhor_Pont/Geracao",fontsize=14)
    plt.tick_params(axis='both',which = 'major',labelsize=5)
    plt.axis([1,(len(VET_BEST)+1),0,49],fontsize=25)
    plt.savefig('Melhor.png') 
    plt.show()
 


if __name__ == '__main__':
 
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward_flappy')
    run(config_path)

#survival_threshold 0.10 - 0.20
#Depois Tentar entender tanto essa parte do __main__ quando o modulo visualize, 
#e a nn dessa neat

#Atenção a essa forma que eu faço esse fitness
#ao final guardar o mais avaliado e utilizarmais tarde
