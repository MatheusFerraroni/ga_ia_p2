# -*- coding: utf-8 -*-

# Python imports
import os

# Libs
import numpy as np
import pandas as pd

# Sklearn
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.model_selection import StratifiedKFold, KFold, cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import warnings
warnings.filterwarnings('ignore')


class Model:
    """
        This class has the goal to preprocess a dataframe, train and test a model, and return the f1 score.
        Preprocess functions:
        - get_feature_types
        - impute
        - encode_categorical
        - encode_target
    """

    def get_feature_types(self, df):
        """Go through the pandas DataFrame columns, convert to the right dtype, and remove data features.
        Args:
            df (pd.DataFrame): the dataset.
        Returns:
            df: pandas.DataFrame.
            categorical_features: list of categorical features.
            numerical_features: list of numerical features.
        """

        cat_features = []
        num_features = []
        date_features = []

        for column, dtype in zip(list(df.columns), list(df.dtypes)):

            if 'datetime64[ns]' in str(dtype):
                date_features.append(column)

                df['{0}_day'.format(column)] = df[column].day
                df['{0}_month'.format(column)] = df[column].month
                df['{0}_year'.format(column)] = df[column].year

            elif dtype not in ['int64', 'float64']:
                cat_features.append(column)
                df[column] = df[column].astype(str)

            else:
                num_features.append(column)

        df = df.drop(date_features, axis=1)

        return df, cat_features, num_features


    def impute(self, df, cat, num):
        """Use SimpleImputer to impute missing values.
        'most_frequent' for categorical and 'mean' for numerical.
        Args:
            df (pd.DataFrame): the dataset.
            cat (list): list of categorical features.
            num (list): list of numerical features.
        """
        
        for c in df.columns:
            df.loc[df[c] == '?', [c]] = ''

        if len(cat) > 0:
            imputer = SimpleImputer(strategy='most_frequent')
            df.loc[:,cat] = imputer.fit_transform(df.loc[:,cat])

        if len(num) > 0:
            imputer = SimpleImputer(strategy='mean')
            df.loc[:,num] = imputer.fit_transform(df.loc[:,num])


    def encode_categorical(self, df, cat):
        """Encode categorical features using OrdinalEncoder.
        Args:
            df (pd.DataFrame): the dataset.
            cat (list): list of categorical features.
        """

        encoder = OrdinalEncoder()
        df.loc[:, cat] = encoder.fit_transform(df.loc[:, cat])


    def encode_target(self, target):
        """Encode target if it is categorical using LabelEncoder.
        Args:
            target (pd.Series): the target series.
        Returns:
            target: pandas.Series.
        """
        
        target = target.astype(str)

        encoder = LabelEncoder()
        target = pd.Series(encoder.fit_transform(target))
        return target


    def test(self, df, target):
        """Train a RandomForest model and get the f1-score.
        Args:
            df (pd.DataFrame): the dataset.
            target (pd.Series): the target series.
        Returns:
            float: the f1-score obtained.
        """

        model = DecisionTreeClassifier(random_state=0)

        kf = KFold(n_splits=10, shuffle=True, random_state=12345678)
        res = cross_val_score(model, df, target, cv=kf, scoring='f1_weighted')

        return res.mean()


    def evaluate(self, df: pd.DataFrame, target):
        """Apply transformations to df and target and return the f1-score.
        Args:
            df (pd.DataFrame): the dataset.
            target (pd.Series): the target series.
        Returns:
            float: the f1-score obtained.
        """

        df, cat, num = self.get_feature_types(df)

        self.impute(df, cat, num)

        self.encode_categorical(df, cat)

        if target.dtype not in ['int64', 'float64']:
            target = self.encode_target(target)

        return self.test(df, target)
