import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

def plotBestGenome(dataset, featureLabels, figSizeArray = [10, 8]):

  bestGenomePerGenerationArray = []
  bestGenomeScorePerGenerationArray = []

  if len(featureLabels) == 0:
    featureLabels = []
    numberOfGenes = len(dataset['historic'][0]['best_genome'])
    i = 0
    while i < numberOfGenes:
      featurelabel =  "feature " + str(i)
      featureLabels.append(featurelabel)
      i = i + 1

  generationArray=  []
  for historicElem in dataset['historic']:
    bestGenomePerGenerationArray.append(historicElem['best_genome'])

  plt.subplots(figsize=figSizeArray)
  ax = sns.heatmap(bestGenomePerGenerationArray, vmin=0, vmax=1, linewidths=.2, xticklabels=featureLabels , cbar=False)
