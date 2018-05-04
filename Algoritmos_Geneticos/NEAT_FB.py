from __future__ import print_function
import os
import neat
import visualize
from numpy import *
from random import *
from flappybird import *


def eval_genomes(genomes, config):
    
    VT_NET = []
    cenario = Cena_Flp(10)
    cenario.preenche()
    
    for genome_id,genome in genomes:
        VT_NET.append(neat.nn.FeedForwardNetwork.create(genome, config))
        
    for net,pair in zip(VT_NET,genomes):
        pair[1].fitness  = flappyenv(net,cenario)
       
    
            
def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)


    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    
    winner = p.run(eval_genomes, 300)

    print('\nBest genome:\n{!s}'.format(winner))

    
    node_names = {-4:'X_P', -3: 'Y_P',-2: 'X_T',-1: 'Y_Pa',0:'Prob'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)



if __name__ == '__main__':
 
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward_flappy')
    run(config_path)

#Depois Tentar entender tanto essa parte do __main__ quando o modulo visualize, 
#e a nn dessa neat

#Atenção a essa forma que eu faço esse fitness
#ao final guardar o mais avaliado e utilizarmais tarde
