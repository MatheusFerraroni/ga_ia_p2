import pandas as pd
import numpy as np

"""
NOTE:

Zillow data isn't ready yet.
Issues:
1) The training dataset needs preprocessing since it is divided into two sets.
Need to join tables first.
2) Lots of empty values for various features. It could be complicated
to preprocess the data before training.

"""

def preprocessDataFrame(df_raw, dataname):

    if dataname == "Bulldozer.csv":
        df_raw.SalePrice = np.log(df_raw.SalePrice)
        return df_raw

    if dataname == "Porto_Seguro.csv":
        return df_raw

    if dataname == "Kobe.csv":
        df_raw = df_raw[ df_raw.shot_made_flag.notnull() ]
        return df_raw

    if dataname == "IBM.csv":
        df_raw.Attrition = (df_raw.Attrition == "Yes").astype(int)
        return df_raw

    if dataname == "mushrooms.csv":
        return df_raw

    if dataname == "airline_customer_satisfaction.csv":
        df_raw.satisfaction = (df_raw.satisfaction == "satisfied").astype(int)
        df_raw = df_raw.drop(columns=["Unnamed: 0","id","Arrival Delay in Minutes"])
        return df_raw

    if dataname == "sky.csv":
        df_raw=df_raw.drop(columns=["objid", 'camcol', 'field', 'objid', 'specobjid', 'fiberid'])
        labels = {'STAR':1, 'GALAXY':2, 'QSO':3}
        df_raw.replace({'class':labels}, inplace = True)
        return df_raw

    if dataname == "weatherAUS.csv":
        df_raw = pd.read_csv(f'/content/weatherAUS.csv', low_memory=False)
        df_raw.drop(['RISK_MM'], axis=1, inplace=True)
        df_raw.RainTomorrow = (df_raw.RainTomorrow != "No").astype(int)
        return df_raw

    if dataname == 'activity_classification.csv':
        labels = {'LAYING':1, 'STANDING':2, 'SITTING':3, 'WALKING':4, 'WALKING_UPSTAIRS':5, 'WALKING_DOWNSTAIRS':6}
        df_raw.replace({'Activity':labels}, inplace = True)
        return df_raw

def returnMinimumScore(dataname):
    defaultScore = 0.8

    if dataname == "Porto_Seguro.csv":
        return 0.97

    if dataname == "Kobe.csv":
        return defaultScore

    if dataname == "IBM.csv":
        return 0.84

    if dataname == "airline_customer_satisfaction.csv":
        return defaultScore

    if dataname == "sky.csv":
        return defaultScore

    return defaultScore


#Won't be used in main.py but keep it in case
def returnTargetColumnName(dataname):

    if dataname == "Bulldozer":
        return "SalePrice"

    if dataname == "Porto_Seguro":
        return 'target'

    if dataname == "Kobe":
        return 'shot_made_flag'

    if dataname == "IBM":
        return 'Attrition'
