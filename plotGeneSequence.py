import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import pandas as pd

def returnLabelsForCSVFile(csvFilePath, targetName):
    featureLabels = []
    file = pd.read_csv(csvFilePath)
    featureLabels = list(file.head(0))
    featureLabels.remove(targetName)
    return featureLabels

def plotBestGenome(resultDatasetPath, datasetPath, targetName,figSizeArray = [10, 8]):

    dataset = openFile(resultDatasetPath)
    bestGenomePerGenerationArray = []
    featureLabels = returnLabelsForCSVFile(datasetPath, targetName)

    for historicElem in dataset['historic']:
        bestGenomePerGenerationArray.append(historicElem['best_genome'])

    plt.subplots(figsize=figSizeArray)
    ax = sns.heatmap(bestGenomePerGenerationArray, vmin=0, vmax=1, linewidths=.2, xticklabels=featureLabels , cbar=False)
