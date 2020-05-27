import GA
import numpy as np
import matplotlib.pyplot as plt
import argparse

from ia.model import Model
import pandas as pd

targets = {'mushrooms.csv': 'class'}




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

    df = pd.read_csv(args.dataset[0])
    target = targets[args.dataset[0].split('/')[2]]
    target = df.pop(target)

    model = Model()

    def custom_fitness(genome):
        bool_genome = list(map(bool, genome))
        return model.evaluate(df.loc[:, bool_genome].copy(), target)

    def custom_random_genome():
        return np.random.randint(low=0,high=2,size=len(df.columns),dtype=int)

    g = GA.GeneticAlgorithm(custom_random_genome)
    g.set_evaluate(custom_fitness)
    g.set_mutate(custom_mutate)

    g.run()




    geracoes = []
    maxs = []
    mins = []
    meds = []
    bests = []
    for i in range(len(g.historic)):
        geracoes.append(g.historic[i]["geracao"])
        maxs.append(g.historic[i]["max"])
        mins.append(g.historic[i]["min"])
        meds.append(g.historic[i]["avg"])
        bests.append(g.historic[i]["best"])



    fig, ax = plt.subplots()
    line1, = ax.plot(geracoes, maxs, label='Max Score')
    line2, = ax.plot(geracoes, meds, label='Average Score')
    line2, = ax.plot(geracoes, mins, label='Min Score')
    line2, = ax.plot(geracoes, bests, label='Best Score')



    ax.legend()
    plt.show()

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Execution parameters')
    parser.add_argument('--dataset', metavar='t', type=str, nargs=1, action='store', help='Dataset path (csv file)')
    args = parser.parse_args()



    main(args)
