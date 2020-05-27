import GA
import numpy as np
import matplotlib.pyplot as plt
import time





# para override no GA
def custom_fitness(genome):
    g = genome.reshape(9,9)


    def check_coluna(mat, ind, num):
        contador_found = 0
        for i in range(9):
            if mat[i][ind]==num:
                contador_found +=1
        return not contador_found > 1
    def check_linha(mat, ind, num):
        contador_found = 0
        for i in range(9):
            if mat[ind][i]==num:
                contador_found +=1
        return not contador_found > 1

    def check_box(mat, bx, by, val):
        contador_found = 0
        for i in range(3):
            for j in range(3):
                if mat[bx*3+i][by*3+j]==val:
                    contador_found += 1

        return not contador_found > 1

    total_valid = 0
    for i in range(9):
        for j in range(9):
            still_valid = True
            still_valid = check_coluna(g, i, g[i][j])

            if still_valid:
                still_valid = check_linha(g, j, g[i][j])

            if still_valid:
                still_valid = check_box(g, i//3, j//3, g[i][j])


            if still_valid:
                total_valid += 1
    
    return total_valid/81


# para override no GA
def custom_random_genome():
    return np.random.randint(low=0,high=9,size=81,dtype=int)

# para override no GA
def custom_random_genome2():
    ar = []

    for i in range(9):
        for j in range(9):
            ar.append(i)

    ar = np.array(ar)
    np.random.shuffle(ar)
    return ar


# para override no G1111A
# inverte os valores do genoma
def custom_mutate(index, genome):
    genome[index] = np.random.randint(low=0,high=9,size=1,dtype=int)
    return genome


# swap index e index+1
def custom_mutate2(index, genome):
    p = np.random.randint(low=0,high=len(genome),size=1,dtype=int)
    genome[index], genome[p] = genome[p], genome[index]
    return genome



def main():




    g = GA.GeneticAlgorithm(custom_random_genome2)
    g.set_evaluate(custom_fitness)
    g.set_mutate(custom_mutate2)

    g.set_iteration_limit(1000)
    g.set_population_size(100)
    g.set_mutation_rate(0.011)
    g.set_crossover_type(2)
    g.set_cut_half_population(True)
    # g.threads(False) # Não ta funcionando bem isso, a fitness function também devesse ser paralelizada nesse caso
    g.set_replicate_best(0.05) # se isso estiver ativo o best element total e o melhor da populaçõa serão os mesmos

    start = time.time()
    g.run()
    end = time.time()
    print("Tempo total: ",end - start)




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


    main()