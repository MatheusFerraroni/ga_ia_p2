import GA
import numpy as np
import matplotlib.pyplot as plt
import argparse
import json
from datetime import datetime

from ia.model import Model
from ia import targetpreprocessing
import pandas as pd

targets = {'mushrooms.csv': 'class',
           'netflix_titles.csv': 'show_id',
           'Bulldozer.csv': 'SalePrice',
           'Porto_Seguro.csv': 'target',
           'Kobe.csv': 'shot_made_flag',
           'IBM.csv': 'Attrition'
           }


# para override no GA
# inverte os valores do genoma
def custom_mutate(index, genome):
    if genome[index]==0:
        genome[index] = 1
    else:
        genome[index] = 0
    return genome

# swap index e index+1
def custom_mutate2(index, genome):
    p = np.random.randint(low=0,high=len(genome),size=1,dtype=int)
    genome[index], genome[p] = genome[p], genome[index]
    return genome


def main(args):

    dataset_name      = args.dataset[0].split('/')[-1]
    population_size   = int(args.population[0].split('/')[-1])
    iteration_limit   = int(args.iteration_limit[0].split('/')[-1])
    stop_criteria     = int(args.stop_criteria[0].split('/')[-1])
    probs_type        = int(args.probs_type[0].split('/')[-1])
    crossover_type    = int(args.crossover_type[0].split('/')[-1])
    crossover_rate    = float(args.crossover_rate[0].split('/')[-1])
    mutation_type     = int(args.mutation_type[0].split('/')[-1])
    mutation_rate     = float(args.mutation_rate[0].split('/')[-1])
    use_threads       = bool(int(args.use_threads[0].split('/')[-1]))
    cut_half_pop      = bool(int(args.cut_half_pop[0].split('/')[-1]))
    replicate_best    = float(args.replicate_best[0].split('/')[-1])

    name = dataset_name+"_"+ \
    		str(population_size)+"_"+\
    		str(iteration_limit)+"_"+\
    		str(stop_criteria)+"_"+\
    		str(probs_type)+"_"+\
    		str(crossover_type)+"_"+\
    		str(crossover_rate)+"_"+\
    		str(mutation_type)+"_"+\
    		str(mutation_rate)+"_"+\
    		str(use_threads)+"_"+\
    		str(cut_half_pop)+"_"+\
    		str(replicate_best)

    now = datetime.now()
    simTime = str(now.strftime("%Y %m %d %H-%M-%S"))
    print("Simulation: ", name, " time =", simTime)

    # print("\n\n**** Start **** ")
    # print("Dataset: ", dataset_name)
    # print("Population Size: ", population_size)
    # print("Iteration limit: ", iteration_limit)
    # print("Stop criteria: ", stop_criteria)
    # print("Probs type: ", probs_type)
    # print("Crossover type: ", crossover_type)
    # print("Crossover rate: ", crossover_rate)
    # print("Mutation type: ", mutation_type)
    # print("Mutation rate: ", mutation_rate)
    # print("Use threads: ", use_threads)
    # print("Cut half population: ", cut_half_pop)
    # print("Replicate_best: ", replicate_best)


    df = pd.read_csv(args.dataset[0])
    df = targetpreprocessing.preprocessDataFrame(df, dataset_name)
    target = targets[dataset_name]
    target = df.pop(target)

    model = Model()

    def custom_fitness(genome):
        bool_genome = list(map(bool, genome))
        return model.evaluate(df.loc[:, bool_genome].copy(), target)

    def custom_random_genome():
        return np.random.randint(low=0,high=2,size=len(df.columns),dtype=int)

    g = GA.GeneticAlgorithm(custom_random_genome)
    g.set_evaluate(custom_fitness)


    g.set_population_size(population_size)
    g.set_iteration_limit(iteration_limit)
    g.set_stop_criteria_type(stop_criteria)
    g.set_probs_type(probs_type)
    g.set_crossover_type(crossover_type)
    g.set_crossover_rate(crossover_rate)
    if mutation_type==0:
    	g.set_mutate(custom_mutate)
    else:
    	g.set_mutate(custom_mutate2)
    g.set_mutation_rate(mutation_rate)
    g.threads(use_threads)
    g.set_cut_half_population(cut_half_pop)
    g.set_replicate_best(replicate_best)


    g.run()

    infos = {}
    infos["dataset_name"] = dataset_name
    infos["ga_config"] = g.get_config()
    infos["historic"] = g.historic


    #
    #f = open("./results/"+dataset_name+" "+current_time+".json","w")
    f = open("./results/"+name+".json","w")
    f.write(json.dumps(infos))
    f.close()


    # geracoes = []
    # maxs = []
    # mins = []
    # meds = []
    # bests = []
    # for i in range(len(g.historic)):
    #     geracoes.append(g.historic[i]["geracao"])
    #     maxs.append(g.historic[i]["max"])
    #     mins.append(g.historic[i]["min"])
    #     meds.append(g.historic[i]["avg"])
    #     bests.append(g.historic[i]["best"])

    # print("Generations = ", geracoes)
    # fig, ax = plt.subplots()
    # line1, = ax.plot(geracoes, maxs, label='Max Score')
    # line2, = ax.plot(geracoes, meds, label='Average Score')
    # line2, = ax.plot(geracoes, mins, label='Min Score')
    # line2, = ax.plot(geracoes, bests, label='Best Score')
    # ax.legend()
    # plt.show()

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Execution parameters')
    parser.add_argument('--dataset', metavar='t', type=str, nargs=1, action='store', help='Dataset path (csv file)')
    parser.add_argument('--population', metavar='t', type=str, nargs=1, action='store', help='Population Size')
    parser.add_argument('--iteration_limit', metavar='t', type=str, nargs=1, action='store', help='Iteration Limit')
    parser.add_argument('--stop_criteria', metavar='t', type=str, nargs=1, action='store', help='Stop Criteria E(0,1,2)')
    parser.add_argument('--probs_type', metavar='t', type=str, nargs=1, action='store', help='Probs type E(0,1)')
    parser.add_argument('--crossover_type', metavar='t', type=str, nargs=1, action='store', help='Crossover type E(0,1,2,3)')
    parser.add_argument('--crossover_rate', metavar='t', type=str, nargs=1, action='store', help='Crossover Rate Pr~(0-1)')
    parser.add_argument('--mutation_type', metavar='t', type=str, nargs=1, action='store', help='Mutation Type E(0,1)')
    parser.add_argument('--mutation_rate', metavar='t', type=str, nargs=1, action='store', help='Mutation Rate Pr~(0-1)')
    parser.add_argument('--use_threads', metavar='t', type=str, nargs=1, action='store', help='Multi-thread (True or False)')
    parser.add_argument('--cut_half_pop', metavar='t', type=str, nargs=1, action='store', help='Cut half population  (True or False)')
    parser.add_argument('--replicate_best', metavar='t', type=str, nargs=1, action='store', help='Replicate best Pr~(0-1)')


    args = parser.parse_args()



    main(args)
