import matplotlib.pyplot as plt
import matplotlib.markers as plm
import numpy as np
import json
import itertools


name            = ["mushrooms.csv"] #a
population      = ["10", "20", "50"]      #b
iteration_limit = ["10", "20", "50"]            #c
stop_criteria   = ["0"]             #d
probs_type      = ["0"]             #e
crossover_type  = ["0", "1"]             #f
crossover_rate  = ["0.1", "0.5"]           #g
mutation_type   = ["0", "1"]             #h
mutation_rate   = ["0.0", "0.1"]           #i
use_threads     = ["False"]         #j 
cut_half_pop    = ["False"]         #k
replicate_best  = ["0.0", "0.1"]           #l



for a, b, c, d, e, f, g, h, i, j, k, l in itertools.product(name, population, iteration_limit, \
	stop_criteria, probs_type, crossover_type, crossover_rate, mutation_type, mutation_rate, \
	use_threads, cut_half_pop, replicate_best):
	
	gene = []
	maxs = []
	mins = []
	meds = []
	best = []
	y_std = []
	

	nameFile = a+"_"+b+"_"+c+"_"+d+"_"+e+"_"+f+"_"+g+"_"+h+"_"+i+"_"+j+"_"+k+"_"+l
	print("File: ", nameFile)

	f = open("../results/" + nameFile + ".json", "r")
	dados = json.loads(f.read())
	f.close()

	part = dados.get("historic")
	for i in range(len(part)):
	    gene.append(int(part[i]["geracao"]))
	    maxs.append(float(part[i]["max"]))
	    mins.append(float(part[i]["min"]))
	    meds.append(float(part[i]["avg"]))
	    best.append(float(part[i]["best"]))
	    y_std.append(0)


	# print("gene = ", gene)
	# print("maxs = ", maxs)
	# print("mins = ", mins)
	# print("meds = ", meds)
	# print("best = ", best)

	fig = plt.figure(1)

	yMax = max(maxs) + max(maxs)*0.02
	yMim = max(maxs)*-0.02
	plt.ylim(yMim, yMax)

	xMax = len(gene) + len(gene)*0.02
	xMim =  len(gene)*-0.02
	plt.xlim(xMim, xMax)
	#plt.xticks(x, rotation = "horizontal")

	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)    												

	plt.errorbar(gene,maxs, ls="solid", label='Max', color='g', yerr=y_std, zorder=3)			
	plt.errorbar(gene,mins, ls="solid", label='Min', color='r', yerr=y_std, zorder=3)						
	plt.errorbar(gene,meds, ls="solid", label='Average', color='b', yerr=y_std, zorder=3)	
	plt.errorbar(gene,best, ls="solid", label='Best', color='black', yerr=y_std, zorder=3)			

	namePlot = nameFile
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	title = a

	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	#plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="upper left", ncol=4, bbox_to_anchor=(-0.02, 1.15))

	fig.savefig('../plots/'+namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 			
	print("End")


	







