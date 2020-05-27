# Python imports
import os

# Libs
import numpy as np
import pandas as pd

# Sklearn
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


class Model:


    def get_feature_types(df):

        categorical_features = []
        date_features = []

        # Convert to specific types
        for column, dtype in zip(list(df.columns), list(df.dtypes)):

            if 'datetime64[ns]' in str(dtype):
                date_features.append(column)

            elif dtype not in ['int64', 'float64']:
                categorical_features.append(column)
                df[column] = df[column].astype(str)

        df = df.drop(date, axis=1)

        return df, categorical_features


    def encode_categorical(self, df, cat):

        encoder = OrdinalEncoder()
        df.loc[:, cat] = encoder.fit_transform(df.loc[:, cat])


    def encode_target(self, target):

        encoder = LabelEncoder()
        target = encoder.fit_transform(target)


    def train_and_test_rf(self, df, target):

        model = DecisionTreeClassifier(random_state=0)

        kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=12345678)
        res = cross_val_score(model, df, target, cv=kf, scoring='f1')

        return res.mean()


    def evaluate(self, df, target):

        df, cat, date = self.get_feature_types(df)

        self.encode_categorical(df, cat)

        if target.dtype not in ['int64', 'float64']:
            self.encode_target(target)

        return self.train_and_test_rf(df, target)


def read_data(file_name, sep=','):

    return pd.read_csv(file_name, sep=sep)


if __name__ == '__main__':

    df = pd.read_csv('mushrooms.csv')
    target = df.pop('class')

    print('entrou')

    model = Model()
    res = model.evaluate(df, target)

    print(res)
