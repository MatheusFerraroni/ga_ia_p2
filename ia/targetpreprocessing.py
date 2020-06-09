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

    if dataname == "Bulldozer":
        df_raw.SalePrice = np.log(df_raw.SalePrice)
        return df_raw.SalePrice

    if dataname == "Porto Seguro":
        return df_raw.target

    if dataname == "Kobe":
        df_raw = df_raw[ df_raw.shot_made_flag.notnull() ]
        return df_raw

    if dataname == "IBM":
        df_raw.Attrition = (df_raw.Attrition == "Yes").astype(int)
        return df_raw.Attrition

    if dataname == "Zillow":
        return []

def returnTargetColumnName(dataname):

    if dataname == "Bulldozer":
        return "SalePrice"

    if dataname == "Porto Seguro":
        return 'target'

    if dataname == "Kobe":
        return 'shot_made_flag'

    if dataname == "IBM":
        return 'Attrition'

    if dataname == "Zillow":
        return ''
