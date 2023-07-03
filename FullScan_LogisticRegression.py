#Logistic regression classification of exometabolomes between four group of samples using the principal component-1 (PC1) values from sparse principal component analysis (sPCA) 
#Begin#

import pandas as pd
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

TrainData = pd.read_csv('ent4_SPCA_PC1.csv', header=0)  #Open the csv file containing PC1 values from sPCA analysis
SampleName = TrainData['Sample']
GroupNumber = TrainData['GroupNumber']

X_train = TrainData['PC1']
X_train_ = X_train.to_numpy()
X_train_ = X_train_.reshape(-1, 1)
sc = StandardScaler(with_mean=True, with_std=True)
X_train_std = sc.fit_transform(X_train_)

GroupNumber_le = LabelEncoder()
y_train = GroupNumber_le.fit_transform(TrainData['GroupNumber'])
y_train_ = y_train
print(y_train)

lr = LogisticRegression(penalty='none', random_state=1)
scores = []
kfold = list(StratifiedKFold(n_splits=4, random_state=1, shuffle=True).split(X_train_std, y_train_))
for k, (train, test) in enumerate(kfold):
    lr.fit(X_train_std[train], y_train_[train])
    score = lr.score(X_train_std[test], y_train_[test])
    scores.append(score)

scores_df = pd.DataFrame(scores)  #Prediction accuracy
print(scores_df)
scores_df.to_csv('ent4_LogisticRegression_ccuracy.csv')

#Exported csv files are used for further data analyses and drawing figures in Excel and Prism
#End#
