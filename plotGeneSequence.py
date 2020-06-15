import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import pandas as pd
import os

import json

def openFile(nameFile):
	try:
		f = open(nameFile, "r")
		dados = json.loads(f.read())
		f.close()
	except:
		dados = 0
		pass

	return dados

targets = {'mushrooms.csv': 'class',
           'netflix_titles.csv': 'show_id',
           'Bulldozer.csv': 'SalePrice',
           'Porto_Seguro.csv': 'target',
           'Kobe.csv': 'shot_made_flag',
           'IBM.csv': 'Attrition',
           'sky.csv': 'class',
           'airline_customer_satisfaction.csv': 'satisfaction',
           'weatherAUS.csv': 'RainTomorrow',
           'activity_classification.csv':'Activity',
           'bands.csv': 'band type',
           'flag.csv': 'region',
           'glass.csv': 'Type',
           'cellphone.csv': 'price_range'
           }

def returnLabelsForCSVFile(csvFilePath, targetName):
    featureLabels = []
    file = pd.read_csv(csvFilePath)
    featureLabels = list(file.head(0))
    featureLabels.remove(targetName)
    return featureLabels

def returnBaseNameOfFileFullPath(resultDatasetPath):
    name = resultDatasetPath.split('/')
    baseName = name[len(name)-1]
    name = baseName.split('.')
    return name[0]

def plotBestGenome(resultDatasetPath, figSizeArray = [10, 8], plotSavedInFolder = "bestGenomeSequencePlots/"):

    dataset = openFile("results2/"+resultDatasetPath)
    bestGenomePerGenerationArray = []
    baseName = returnBaseNameOfFileFullPath(resultDatasetPath)
    datasetPath = "data/" + baseName
    targetName = targets[baseName+".csv"]
    featureLabels = returnLabelsForCSVFile(datasetPath+".csv", targetName)

    if len(featureLabels) == 0:
        print("Error in getting feature labels")
        return

    for historicElem in dataset['historic']:
        bestGenomePerGenerationArray.append(historicElem['best_genome'])

    plt.subplots(figsize=figSizeArray)
    ax = sns.heatmap(bestGenomePerGenerationArray, vmin=0, vmax=1, linewidths=.2, xticklabels=featureLabels , cbar=False)
    ax.invert_yaxis()
    imageFullPath = plotSavedInFolder+resultDatasetPath+'.png'
    plt.savefig(imageFullPath, bbox_inches='tight')
    fig = plt.gcf()
    plt.close(fig)


for filename in os.listdir("results2/"):
    plotBestGenome(filename)
print("done")
