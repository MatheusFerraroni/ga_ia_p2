import matplotlib.pyplot as plt
import matplotlib.markers as plm
import numpy as np
import json
import itertools

def openFile(nameFile):
	try:
		f = open(nameFile + ".json", "r")
		dados = json.loads(f.read())
		f.close()
	except:
		dados = 0
		pass

	return dados

def bestConfig(vector):
	maximo = 0
	for i in range(len(vector)):
		for j in range(len(vector[i])):
			if vector[i][j] > maximo:
				maximo = vector[i][j]
				indice = i
	
	return maximo,indice

def minConfig(vector):
	minimo = vector[0][0]
	indice = 0
	for i in range(len(vector)):
		for j in range(len(vector[i])):
			if vector[i][j] < minimo:
				minimo = vector[i][j]
				indice = i
	
	return minimo,indice

def plotBest(y_gene,y_best):
	
	fig = plt.figure(1)
	
	maximo,indice = bestConfig(y_best)
	minimo,indiceM = minConfig(y_best)

	yMax = maximo + maximo * 0.02
	yMim = minimo - 0.02	# mudar o limite inferior (trocar o valor -0.02)
	plt.ylim(yMim, yMax)	
	
	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, 100)

	plt.xticks(rotation = "horizontal")

	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)    												
			
	for n in range(len(y_best)):		
		plt.errorbar(y_gene[n],y_best[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_bestIndividuals"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	titulo = nome(a)
	title = titulo + " - Best Individuals"

	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower right", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig(namePlot+'.png', bbox_inches='tight')
	plt.close(fig)

	return True			

def plotMin(y_gene,y_mins):
	
	fig = plt.figure(2)

	maximo,indice = bestConfig(y_mins)
	minimo,indiceM = minConfig(y_mins)

	yMax = maximo + maximo * 0.02
	yMim = minimo - 0.02	# mudar o limite inferior (trocar o valor -0.02)
	plt.ylim(yMim, yMax)

	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, 100)

	
	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
	for n in range(len(y_mins)):
		plt.errorbar(y_gene[n],y_mins[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_mins"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	titulo = nome(a)
	title = titulo + " - Minimum"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower left", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig(namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 			
	
	return True

def plotMax(y_gene,y_maxs):

	fig = plt.figure(3)

	maximo,indice = bestConfig(y_maxs)
	minimo,indiceM = minConfig(y_maxs)

	yMax = maximo + maximo * 0.02
	yMim = minimo - 0.02	# mudar o limite inferior (trocar o valor -0.02)
	plt.ylim(yMim, yMax)

	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, 100)
	
	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
	for n in range(len(y_maxs)):
		plt.errorbar(y_gene[n],y_maxs[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_max"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	titulo = nome(a)
	title = titulo + " - Maximum"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower left", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig(namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 

	return True	

def plotAvg(y_gene,y_meds):

	fig = plt.figure(4)

	maximo,indice = bestConfig(y_meds)
	minimo,indiceM = minConfig(y_meds)
	
	yMax = maximo + maximo * 0.02
	yMim = minimo - 0.02	# mudar o limite inferior (trocar o valor -0.02)
	plt.ylim(yMim, yMax)

	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, 100)
	
	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
	for n in range(len(y_meds)):
		plt.errorbar(y_gene[n],y_meds[n], ls=formats[n], label=labels[n],color=colors[n],yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_avg"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	titulo = nome(a)
	title = titulo + " - Average"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower right", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig(namePlot+'.png', bbox_inches='tight')
	plt.close(fig)

	return True


def plotIndividual(y_gene,y_maxs,y_mins,y_meds,y_best):

	fig = plt.figure(5)

	maximo,indice = bestConfig(y_maxs)
	minimo,indiceM = minConfig(y_mins)
	
	yMax = maximo + maximo * 0.02
	yMim = minimo - 0.02	# mudar o limite inferior (trocar o valor -0.02)
	plt.ylim(yMim, yMax)

	bestt,indice = bestConfig(y_best)
	xMax = len(y_gene[indice]) + len(y_gene[indice])*0.02
	xMim =  len(y_gene[indice])*-0.02
	plt.xlim(xMim, xMax)
		
	plt.grid(True, which="both", ls="-", linewidth=0.1,color='0.10', zorder=0)
	plt.errorbar(y_gene[indice],y_maxs[indice], ls=formats[indice], label='maximum', color='blue',yerr=y_y_std[indice], zorder=3)	
	plt.errorbar(y_gene[indice],y_meds[indice], ls=formats[indice], label='average', color='green',yerr=y_y_std[indice], zorder=3)	
	plt.errorbar(y_gene[indice],y_mins[indice], ls=formats[indice], label='minimum', color='pink',yerr=y_y_std[indice], zorder=3)
		
	namePlot = a + "_best_b_a_m"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	titulo = nome(a)
	title = titulo + " - Best, Average and Minimum"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower left", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig(namePlot+'.png', bbox_inches='tight')
	plt.close(fig)

	return True

def plotIndMult(y_gene,y_maxs,y_mins,y_meds,y_best):

	fig = plt.figure(6)

	maximo,indice = bestConfig(y_maxs)
	minimo,indiceM = minConfig(y_mins)
	
	yMax = maximo + maximo * 0.02
	yMim = minimo - 0.02	# mudar o limite inferior (trocar o valor -0.02)	
	plt.ylim(yMim, yMax)

	xMax = len(y_gene[0]) + len(y_gene[0])*0.02
	xMim =  len(y_gene[0])*-0.02
	plt.xlim(xMim, 100)

	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.10', zorder=0)
	for n in range(len(y_maxs)):
		plt.errorbar(y_gene[n],y_best[n], ls=formats[n],color='pink',yerr=y_y_std[n], zorder=3)	
	for n in range(len(y_maxs)):
		plt.errorbar(y_gene[n],y_meds[n], ls=formats[n],color='green',yerr=y_y_std[n], zorder=3)
	for n in range(len(y_maxs)):
		plt.errorbar(y_gene[n],y_mins[n], ls=formats[n],color='blue',yerr=y_y_std[n], zorder=3)
		
	namePlot = a + "_best_avg_min"
	ylabel = 'Fitness'
	xlabel = 'Number of generations'
	titulo = nome(a)
	title = titulo + " - Best and Average and Minimum"


	plt.ylabel(ylabel, fontweight="bold")
	plt.xlabel(xlabel, fontweight="bold") 	
	plt.title(title, fontweight="bold")

	plt.legend(numpoints=1, loc="lower left", ncol=3)	# ,bbox_to_anchor=(-0.02, 1.15)

	fig.savefig(namePlot+'.png', bbox_inches='tight')
	plt.close(fig) 	

	return True

def nome(a):
	if a == 'glass':
		return 'Glass'
	elif a == 'airline_customer_satisfaction':
		return 'Airline Customer Satisfaction'
	elif a == 'bands':
		return 'Bands'
	elif a == 'cellphone':
		return 'Cellphone'
	elif a == 'flag':
		return 'Flag'
	else:
		return a

if __name__ == '__main__':

	name            = ["glass","IBM","Kobe","mushrooms","airline_customer_satisfaction","bands","cellphone","flag"]
	population      = ["10", "50"]
	iteration_limit = ["100", "200"]
	stop_criteria   = ["0","1"]
	probs_type      = ["0"]
	crossover_type  = ["2", "3"]
	crossover_rate  = ["0.5","0.8"]
	mutation_type   = ["0", "1"]
	mutation_rate   = ["0.03", "0.15"]
	use_threads     = ["False"]
	cut_half_pop    = ["False"]
	replicate_best  = ["0.0", "0.1"]

	for a in name:

		name1 = a + ".csv"
		indice = 0
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

			dados = openFile("../results/"+nameFile)
			
			if dados != 0:

				print("File: ", nameFile)
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
					
		
		colors = ['m','c','pink','r','b','g','y','orange','k','green']	
		formats = ['solid', 'solid','solid','solid','solid','solid','solid','solid','solid','solid']	
		labels = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9']
		
		best1 = plotBest(y_gene,y_best)

		min1 = plotMin(y_gene,y_mins)

		max1 = plotMax(y_gene,y_maxs)

		average1 = plotAvg(y_gene,y_meds)

		indiv1 = plotIndividual(y_gene,y_maxs,y_mins,y_meds,y_best)	
