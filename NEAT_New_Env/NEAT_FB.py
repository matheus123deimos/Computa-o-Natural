from __future__ import print_function
import matplotlib.pyplot as plt
import os
import neat
import visualize
from numpy import *
from ple import PLE
from ple.games import *


#Obs: 
#     Gráficos no Seaborn
VET_MED1 =[]
VET_BEST1 = []
VET_MED2 =[]
VET_BEST2 = []
Cenario = 3
Canos = 10
#INIT_GAP = list(map(lambda x:192 if(x>192) else x,list(map(lambda x:25 if(x<25) else x,list(map(lambda x:abs(x),list(random.normal(108.5,82,(1,Canos))[0])))))))
INIT_GAP = [25 if(i%2==0) else 25 for i in range(Canos)]
GAME = FlappyBird(True,INIT_GAP,Canos)
ENV = PLE(GAME)
#GAP = [list(map(lambda x:192 if(x>192) else x,list(map(lambda x:25 if(x<25) else x,list(map(lambda x:abs(x),
                                  #list(random.normal(108.5,82,(1,int(Canos)))[0])))))))for i in range(Cenario)]# Cálculo baseado nos atributos da classe flappy
GAP = [[25 if(i%2==0) else 82.5*j for i in range(Canos)] for j in range(Cenario)]


def eval_genomes(genomes, config):
    
    VT_NET = []
    SCORE1 = []
    SCORE2 = []
    
    for genome_id,genome in genomes:#Decoifica os Genomas em Redes
        VT_NET.append(neat.nn.FeedForwardNetwork.create(genome, config))
        
    for net,pair in zip(VT_NET,genomes): 
        score = []
        pont = []
        ENV.init()
        
        for i in range(Cenario):
            Score = 0.0
            Pont = 0.0
            Fator_y = 0.0
            while(True):
                #Armazene o Estado pré-Rede;Repasse para a Rede; Obtenha sua Resposta
                
                State1 = ENV.game.getGameState()
                INP1 = State1["player_y"]
                INP2 = State1["next_pipe_bottom_y"]
                INP3= (-State1["next_pipe_top_y"]+State1["next_pipe_bottom_y"])/2
                #INP4 = State1["next_pipe_dist_to_player"]
               
                OUTPUT = net.activate((INP1,INP2,INP3))
                VAL = 119 if OUTPUT[0]>=0.4 else None
                RESP = ENV.act(VAL)
                ENV.display_screen = True
                ENV.force_fps = True
                #Trate a Resposta do Ambiente 
                if(RESP>0):
                    Score += 1
                    if(Score==Canos):
                        if(i<Cenario-1):
                            ENV.reset_game(GAP[i+1],Canos)
                            break
                        
                        break

                Pont += 1.0
                if(ENV.game_over()):#Se for game_over() o estado pós-Rede é filtrado
                    State2 = ENV.game.getGameState()
                    if(i<Cenario-1):
                        Fator_y = State2["player_y"] - (State2["next_pipe_top_y"]+(State2["next_pipe_top_y"]-State2["next_pipe_bottom_y"])/2)
                        ENV.reset_game(GAP[i+1],Canos)
                        break
                    
                    break
                    
                
            pont.append(Pont/10 + (Score*10) - (Fator_y/100))
            score.append(Score)
        
        SCORE1.append(round(sum(pont)/len(pont),4))
        SCORE2.append(round(sum(score)/len(score),4))
        
        pair[1].fitness = round(sum(pont)/len(pont),4)
        
    VET_MED1.append(round(sum(SCORE1)/len(SCORE1),4))# Adiciono a média dos scores da população a um vetor de médias para plotagem
    VET_BEST1.append(max(SCORE1))#Busco o que obteve o maior score e guardo pra plotagem

    VET_MED2.append(round(sum(SCORE2)/len(SCORE2),4))
    VET_BEST2.append(max(SCORE2))
    
    print(max(SCORE1))
    print(round(sum(SCORE1)/len(SCORE1),4))

    print(max(SCORE2))
    print(round(sum(SCORE2)/len(SCORE2),4))
    
def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-996')
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    
    winner = p.run(eval_genomes,100) #Retorna o melhor depois de 150 gerações

    print('\nBest genome:\n{!s}'.format(winner))

   
    node_names = {-3:'Y_P',-2:'Y_B',-1:'Y_C',0:'Prob'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    #visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    #Plotagem do Grafico do Médio e do Melhor Fitness
    plt.plot(list(range(1,len(VET_MED1)+1)),VET_MED1,linewidth=2,color = 'blue',label='Fitness Medio')
    plt.plot(list(range(1,len(VET_BEST1)+1)),VET_BEST1,linewidth=2,color = 'red',label='Fitness Maior')
    plt.title("Fitness",fontsize=24)
    plt.xlabel("GERACAO",fontsize=14)
    plt.ylabel("P_M&P_B/Geracao",fontsize=14)
    plt.tick_params(axis='both',which = 'major',labelsize=5)
    plt.axis([1,(len(VET_MED1)+1),0,153],fontsize=25)
    plt.grid()
    legend = plt.legend(loc='upper right')
    plt.savefig('Fitness.png')
    plt.show()

    #Plotagem do Grafico do Médio e do Melhor Score
    plt.plot(list(range(1,len(VET_MED2)+1)),VET_MED2,linewidth=2,color = 'blue',label='Score Medio')
    plt.plot(list(range(1,len(VET_BEST2)+1)),VET_BEST2,linewidth=2,color = 'red',label='Score Maior')
    plt.title("Score",fontsize=24)
    plt.xlabel("GERACAO",fontsize=14)
    plt.ylabel("S_M&S_B/Geracao",fontsize=14)
    plt.tick_params(axis='both',which = 'major',labelsize=5)
    plt.axis([1,(len(VET_MED2)+1),0,11],fontsize=25)
    plt.grid()
    legend = plt.legend(loc='upper right')
    plt.savefig('Score.png')
    plt.show()

 


if __name__ == '__main__':
 
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward_flappy')
    run(config_path)


