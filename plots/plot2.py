import matplotlib.pyplot as plt
import matplotlib.markers as plm
import numpy as np
import json
import itertools


name            = ["IBM","Kobe","mushrooms"] #a
population      = ["10", "50"]      #b
iteration_limit = ["100", "200"]    #c
stop_criteria   = ["0","1"]             #d
probs_type      = ["0"]             #e
crossover_type  = ["2", "3"]             #f
crossover_rate  = ["0.8","0.5"]           #g
mutation_type   = ["0", "1"]             #h
mutation_rate   = ["0.03", "0.15"]           #i
use_threads     = ["False"]         #j 
cut_half_pop    = ["False"]         #k
replicate_best  = ["0.0", "0.1"]           #l

def openFile(nameFile):
	try:
		f = open("../results/" + nameFile + ".json", "r")
		dados = json.loads(f.read())
		f.close()
	except:
		dados = 0
		pass

	return dados

for a in name:

	name1 = a + ".csv"
	nComb = 0
	maximo = 0

	y_gene = []
	y_maxs = []
	y_mins = []
	y_meds = []
	y_best = []
	y_y_std = []
	teste = []

	for b, c, d, e, f, g, h, i, j, k, l in itertools.product(population, iteration_limit, \
		stop_criteria, probs_type, crossover_type, crossover_rate, mutation_type, mutation_rate, \
		use_threads, cut_half_pop, replicate_best):							

		nameFile = name1+"_"+b+"_"+c+"_"+d+"_"+e+"_"+f+"_"+g+"_"+h+"_"+i+"_"+j+"_"+k+"_"+l		

		test = b+"_"+c+"_"+d+"_"+e+"_"+f+"_"+g+"_"+h+"_"+i+"_"+j+"_"+k+"_"+l				

		dados = openFile(nameFile)
		
		if dados != 0:

			#print("File: ", nameFile)
			teste.append(test)

			gene = []
			maxs = []
			mins = []
			meds = []
			best = []
			y_std = []

			part = dados.get("historic")
			
			for i in range(len(part)):
			    gene.append(int(part[i]["geracao"]))
			    maxs.append(float(part[i]["max"]))
			    if float(part[i]["max"]) > maximo:
			    	maximo = float(part[i]["max"])
			    mins.append(float(part[i]["min"]))
			    meds.append(float(part[i]["avg"]))
			    best.append(float(part[i]["best"]))
			    y_std.append(0)					
						
			y_gene.append(gene)
			y_maxs.append(maxs)
			y_mins.append(mins)
			y_meds.append(meds)
			y_best.append(best)
			y_y_std.append(y_std)
	
	
	colors = ['m','c','pink','r','b','g','y','orange','k']	
	formats = ['solid', 'solid','solid','solid','solid','solid','solid','solid','solid']	
	labels = ['C0','C1','C2','C3','C4','C5','C6','C7','C8']

	# best

	fig = plt.figure(1)

	yMax = maximo + maximo * 0.02
	yMim = maximo * -0.02	
	plt.ylim(0.3, yMax)	
	
	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, xMax)

	plt.xticks(rotation = "horizontal")

	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)    												
		
		
	for n in range(len(y_best)):
		plt.errorbar(y_gene[n],y_best[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_bestIndividuals"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	title = a + " - Best Individuals"

	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower right", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig('../plots/'+namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 			
	

	# average

	yMax = maximo + maximo * 0.02
	yMim = maximo * -0.02
	plt.ylim(0.2, yMax)

	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, xMax)

	fig = plt.figure(1)
	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
	for n in range(len(y_meds)):
		plt.errorbar(y_gene[n],y_meds[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_avg"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	title = a + " - Average"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower right", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig('../plots/'+namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 			

	# Min

	yMax = maximo + maximo * 0.02
	yMim = maximo * -0.02
	plt.ylim(-0.05, yMax)

	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, xMax)

	fig = plt.figure(1)
	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
	for n in range(len(y_mins)):
		plt.errorbar(y_gene[n],y_mins[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_mins"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	title = a + " - Minimum"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower left", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig('../plots/'+namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 			

	# Max

	yMax = maximo + maximo * 0.02
	yMim = maximo * -0.02
	plt.ylim(-0.05, yMax)

	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, xMax)

	fig = plt.figure(1)
	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
	for n in range(len(y_maxs)):
		plt.errorbar(y_gene[n],y_maxs[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_max"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	title = a + " - Maximum"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower left", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig('../plots/'+namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 			
