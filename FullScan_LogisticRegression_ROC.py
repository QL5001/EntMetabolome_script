#Receiver operating characteristic (ROC) curve of Logistic regression classification of exometabolomes between four groups of samples using the principal component-1 (PC1) values from parse principal component analysis (sPCA) 
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
from sklearn.metrics import roc_curve, auc

TrainData = pd.read_csv('ent4_SPCA_PC1.csv', header=0)  #Open the csv file containing PC1 values from sPCA analysis
SampleName = TrainData['Sample']
GroupNumber = TrainData['GroupNumber']
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
kfold = list(StratifiedKFold(n_splits=4, random_state=1, shuffle=True).split(X_train_std, y_train_))

lr_fpr = []
lr_tpr = []
lr_auc = []
lr_thresholds = []
#lr_probas = pd.DataFrame()

for k, (train, test) in enumerate(kfold):
    probas = lr.fit(X_train_std[train], y_train_[train]).predict_proba(X_train_std[test])
    #print(pd.DataFrame(probas))
    fpr, tpr, thresholds = roc_curve(y_train_[test], probas[:, 0], pos_label=0, drop_intermediate=True)
    lr_fpr.append(fpr)
    lr_tpr.append(tpr)
    roc_auc = auc(fpr, tpr)
    lr_auc.append(roc_auc)
    lr_thresholds.append(thresholds)

lr_fpr_df = pd.DataFrame(lr_fpr)
lr_fpr_df.to_csv('ent4_LogisticRegression_ROC_fpr.csv')

lr_tpr_df = pd.DataFrame(lr_tpr)
lr_tpr_df.to_csv('ent4_LogisticRegression_ROC_tpr.csv')

lr_auc_df = pd.DataFrame(lr_auc)
lr_auc_df.to_csv('ent4_LogisticRegression_AUC.csv')

lr_thresholds_df = pd.DataFrame(lr_thresholds)
lr_thresholds_df.to_csv('ent4_LogisticRegression_Thresholds.csv')

#Exported csv files are used for further data analyses and drawing figures in Excel and Prism
#End#
