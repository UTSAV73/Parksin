# -*- coding: utf-8 -*-
"""ML_Models_with_Dimensionality_Reduction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1okXNRyMsMMpiHjIEsd6lBynyNNMi62-0
"""

import pandas as pd
import numpy as np

path = "bin/Reduced_Dimension_Dataset_1500_pd_swedd.csv"

feature_matrix = pd.read_csv(path)

dfXY = feature_matrix[list(feature_matrix.columns[1:-1])]
X = dfXY.values

Y = feature_matrix[["Class"]]
Y = Y.values
Y = Y.reshape(Y.shape[0],)

print(X.shape)
print(Y.shape)

neg = feature_matrix["Class"].values.tolist().count(0)
ratio = neg/(X.shape[0]-neg)
ratio

# Calculate class weights based on the inverse of class frequencies
class_counts = np.bincount(Y)
class_weights = {i: len(Y) / (len(class_counts) * count) for i, count in enumerate(class_counts)}

"""# SVM LINEAR"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear'],
    #'gamma': ['scale', 'auto'],
}

clf = SVC(class_weight="balanced")

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)

param_grid = {
    'C': [1, 10,100],
    'kernel': ['linear'],
    #'gamma': ['scale', 'auto'],
}

clf = SVC(class_weight="balanced")

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')
accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

#to be run
import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)

# Calculate class weights based on the inverse of class frequencies
# class_counts = np.bincount(Y)
# class_weights = {i: len(Y) / (len(class_counts) * count) for i, count in enumerate(class_counts)}

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear'],
    'gamma': ['scale', 'auto'],
}

clf = SVC(class_weight="balanced")

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)

print("Best parameters:", grid_search.best_params_)
print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))

"""# SVM RBF"""

#to be run
import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

kfold = KFold(n_splits=5, shuffle=True, random_state=12)

# Calculate class weights based on the inverse of class frequencies
Y = np.array([int(i) for i in list(Y)])
class_counts = np.bincount(Y)
class_weights = {i: len(Y) / (len(class_counts) * count) for i, count in enumerate(class_counts)}

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['rbf'],
    'gamma': ['scale', 'auto'],
}

clf = SVC(class_weight=class_weights)

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

"""# LOGISTIC REGRESSION"""

#to be run
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import precision_score, recall_score, f1_score

kfold = KFold(n_splits=5, shuffle=True, random_state=12)

# Calculate class weights based on the class frequencies
Y = np.array([int(i) for i in list(Y)])
class_counts = np.bincount(Y)
total_samples = len(Y)
class_weights = {i: total_samples / (len(class_counts) * count) for i, count in enumerate(class_counts)}

param_grid = {
    'C': [ 10,100,1000],
    'solver': ['liblinear'],
}
#class_weight=class_weights
clf = LogisticRegression(class_weight=class_weights)

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

params = {
    'C': 10,
    'solver': 'liblinear',
}

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True, random_state=12)

clf = LogisticRegression(**params)

clf.fit(X_train, y_train)

from sklearn.metrics import roc_curve, auc

# Predict the probabilities of the positive class
y_pred_proba = clf.predict_proba(X_test)[:, 1]

# Calculate the fpr, tpr, and thresholds for the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Calculate the AUC
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

"""# RANDOM FOREST"""

#to be run
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import precision_score, recall_score, f1_score
import random

kfold = KFold(n_splits=5, shuffle=True, random_state=12)

# Calculate class weights based on the class frequencies
Y = np.array([int(i) for i in list(Y)])
class_counts = np.bincount(Y)
total_samples = len(Y)
class_weights = {i: total_samples / (len(class_counts) * count) for i, count in enumerate(class_counts)}

param_grid = {
    'max_depth': [5, 10, 15],

    'n_estimators': [20, 40, 60, 80],
}

# Create the base classifier (Random Forest) with class weights
clf = RandomForestClassifier(class_weight='balanced', random_state=random.seed(12))

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import precision_score, recall_score, f1_score
import random

kfold = KFold(n_splits=5, shuffle=True, random_state=12)

# Calculate class weights based on the class frequencies
class_counts = np.bincount(Y)
total_samples = len(Y)
class_weights = {i: total_samples / (len(class_counts) * count) for i, count in enumerate(class_counts)}

param_grid = {
    'max_depth': [5, 10, 15, 20],
    'n_estimators': [200, 300, 400, 500],
    'n_estimators': [10, 20, 30, 40],
}

# Create the base classifier (Random Forest) with class weights
clf = RandomForestClassifier(class_weight='balanced',random_state = random.seed(12))

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

grid_search.fit(X, Y)

print("Best parameters:", grid_search.best_params_)
print("Best Score", grid_search.best_score_)

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

params = {
    'max_depth': 5,
    'n_estimators': 20,
    #'early_stopping_rounds':5
}

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, shuffle=True, random_state=12)

clf = RandomForestClassifier(class_weight='balanced', random_state = random.seed(12))

clf.fit(X_train, y_train)

from sklearn.metrics import roc_curve, auc

# Predict the probabilities of the positive class
y_pred_proba = clf.predict_proba(X_test)[:, 1]

# Calculate the fpr, tpr, and thresholds for the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Calculate the AUC
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

print(len(fpr))
print(len(tpr))
print(len(thresholds))

tpr = tpr.tolist()
fpr = fpr.tolist()
diff = [tpr[i]-fpr[i] for i in range(len(tpr))]

idx = diff.index(max(diff))

print(tpr[idx])
print(fpr[idx])

print("Optimal Threshold", thresholds[idx])

#Confusion matrix
#We compare labels and plot them based on correct or wrong predictions.
#Since sigmoid outputs probabilities we need to apply threshold to convert to label.

opt_thresh=0.71

y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = [1 if i>=opt_thresh else 0 for i in y_pred_proba]

import sklearn
cm= sklearn.metrics.confusion_matrix(y_test, y_pred)
print(cm)

true_rate =  (cm[0][0]+cm[1][1])
false_rate = (cm[0][1]+cm[1][0])

accuracy = float(true_rate/(true_rate+false_rate))
recall = float(cm[0][0]/(cm[0][0] + cm[0][1]))
precision = float(cm[0][0]/(cm[0][0] + cm[1][0]))
f1_score = 2*float(float(precision*recall)/float(precision+recall))

print("Accuracy = ", accuracy)
print("Recall = ", recall)
print("Precision = ", precision)
print("F1 Score = ", f1_score)

"""# XG BOOST"""

#to be run
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV, KFold, StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
import xgboost as xgb
from sklearn.metrics import f1_score, make_scorer

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)

# Calculate class weights based on the class frequencies
Y = np.array([int(i) for i in list(Y)])
class_counts = np.bincount(Y)
total_samples = len(Y)
class_weights = total_samples / (len(class_counts) * class_counts)

param_grid = {
    'max_depth': [5, 10, 15],
    'learning_rate': [0.4,0.05], #'learning_rate': [0.5, 0.01, 0.001]
    'n_estimators': [20, 30, 50, 60], # 'n_estimators': [20, 30, 40, 60],
    'scale_pos_weight': [ratio],
}

n = 1
for i in param_grid.keys():
    n = n * len(param_grid[i])

print("No. of Permutations =", n)

clf = xgb.XGBClassifier()

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

params = {
    'learning_rate': 0.4,
    'max_depth': 5,
    'n_estimators': 60,
    #'early_stopping_rounds':5
}

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=12)
clf = xgb.XGBClassifier(**params)
#clf = RandomForestClassifier(class_weight='balanced', random_state = random.seed(12))

clf.fit(X_train, y_train)

from sklearn.metrics import roc_curve, auc

# Predict the probabilities of the positive class
y_pred_proba = clf.predict_proba(X_test)[:, 1]

# Calculate the fpr, tpr, and thresholds for the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Calculate the AUC
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

print(len(fpr))
print(len(tpr))
print(len(thresholds))

tpr = tpr.tolist()
fpr = fpr.tolist()
diff = [tpr[i]-fpr[i] for i in range(len(tpr))]

idx = diff.index(max(diff))

print(tpr[idx])
print(fpr[idx])

print("Optimal Threshold", thresholds[idx])

#Confusion matrix
#We compare labels and plot them based on correct or wrong predictions.
#Since sigmoid outputs probabilities we need to apply threshold to convert to label.

opt_thresh=0.961

y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = [1 if i>=opt_thresh else 0 for i in y_pred_proba]

import sklearn
cm= sklearn.metrics.confusion_matrix(y_test, y_pred)
print(cm)

true_rate =  (cm[0][0]+cm[1][1])
false_rate = (cm[0][1]+cm[1][0])

accuracy = float(true_rate/(true_rate+false_rate))
recall = float(cm[0][0]/(cm[0][0] + cm[0][1]))
precision = float(cm[0][0]/(cm[0][0] + cm[1][0]))
f1_score = 2*float(float(precision*recall)/float(precision+recall))

print("Accuracy = ", accuracy)
print("Recall = ", recall)
print("Precision = ", precision)
print("F1 Score = ", f1_score)

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

params = {
    'max_depth': 5,
    'learning_rate': 0.4,
    'n_estimators': 60,
    # 'early_stopping_rounds':5
}

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

eval_set = [(X_test, y_test)]
clf = xgb.XGBClassifier(**params)

clf.fit(X_train, y_train, eval_set=eval_set)

probs_lr = clf.predict_proba(X_test)

from sklearn.metrics import roc_curve, auc

# Predict the probabilities of the positive class
y_pred_proba = clf.predict_proba(X_test)[:, 1]

# Calculate the fpr, tpr, and thresholds for the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Calculate the AUC
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

y_pred_proba

"""## LIGHT GBM"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import precision_score, recall_score, f1_score
import lightgbm as lgb

kfold = KFold(n_splits=5, shuffle=True, random_state=12)

# Calculate class weights based on the class frequencies
Y = np.array([int(i) for i in list(Y)])
class_counts = np.bincount(Y)
total_samples = len(Y)
class_weights = total_samples / (len(class_counts) * class_counts)

param_grid = {
    'max_depth': [5, 10, 15],
    'learning_rate': [0.1, 0.01, 0.001],
    'scale_pos_weight': class_weights,
}

clf = lgb.LGBMClassifier()

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold, scoring='accuracy')

accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

params = {
    'learning_rate': 0.1,
    'max_depth': 10,
    #'n_estimators': 60,
    #'early_stopping_rounds':5
}

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=12)
#clf = xgb.XGBClassifier(**params)
clf = lgb.LGBMClassifier(**params)
#clf = RandomForestClassifier(class_weight='balanced', random_state = random.seed(12))

clf.fit(X_train, y_train)

from sklearn.metrics import roc_curve, auc

# Predict the probabilities of the positive class
y_pred_proba = clf.predict_proba(X_test)[:, 1]

# Calculate the fpr, tpr, and thresholds for the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Calculate the AUC
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

print(len(fpr))
print(len(tpr))
print(len(thresholds))

tpr = tpr.tolist()
fpr = fpr.tolist()
diff = [tpr[i]-fpr[i] for i in range(len(tpr))]

idx = diff.index(max(diff))

print(tpr[idx])
print(fpr[idx])

print("Optimal Threshold", thresholds[idx])

#Confusion matrix
#We compare labels and plot them based on correct or wrong predictions.
#Since sigmoid outputs probabilities we need to apply threshold to convert to label.

opt_thresh=0.4203

y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = [1 if i>=opt_thresh else 0 for i in y_pred_proba]

import sklearn
cm= sklearn.metrics.confusion_matrix(y_test, y_pred)
print(cm)

true_rate =  (cm[0][0]+cm[1][1])
false_rate = (cm[0][1]+cm[1][0])

accuracy = float(true_rate/(true_rate+false_rate))
recall = float(cm[0][0]/(cm[0][0] + cm[0][1]))
precision = float(cm[0][0]/(cm[0][0] + cm[1][0]))
f1_score = 2*float(float(precision*recall)/float(precision+recall))

print("Accuracy = ", accuracy)
print("Recall = ", recall)
print("Precision = ", precision)
print("F1 Score = ", f1_score)

"""## CATBOOST"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import precision_score, recall_score, f1_score
from catboost import CatBoostClassifier

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Calculate class weights based on the class frequencies
class_counts = np.bincount(Y)
total_samples = len(Y)
class_weights = total_samples / (len(class_counts) * class_counts)

param_grid = {
    'max_depth': [3, 6, 9],
    'learning_rate': [0.1, 0.01, 0.001],
    'scale_pos_weight': class_weights,
}

clf = CatBoostClassifier()

grid_search = GridSearchCV(clf, param_grid=param_grid, cv=kfold)


accuracy_list = []
precision_list = []
recall_list = []
f1_list = []
specificity_list = []
sensitivity_list = []
roc_auc_list = []

for train_index, test_index in kfold.split(X, Y):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    grid_search.fit(X_train, Y_train)
    y_pred = grid_search.predict(X_test)

    accuracy = grid_search.score(X_test, Y_test)
    precision = precision_score(Y_test, y_pred)
    recall = recall_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred)

    tn, fp, fn, tp = confusion_matrix(Y_test, y_pred).ravel()
    specificity = tn / (tn + fp)
    sensitivity = tp / (tp + fn)
    roc_auc = roc_auc_score(Y_test, y_pred)

    specificity_list.append(specificity)
    sensitivity_list.append(sensitivity)
    roc_auc_list.append(roc_auc)

    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)


print("Accuracy List:", accuracy_list)
print("Mean Accuracy:", np.mean(accuracy_list))
print("Standard Deviation of Accuracy:", np.std(accuracy_list))
print()
print("Precision List:", precision_list)
print("Mean Precision:", np.mean(precision_list))
print("Standard Deviation of Precision:", np.std(precision_list))
print()
print("Recall List:", recall_list)
print("Mean Recall:", np.mean(recall_list))
print("Standard Deviation of Recall:", np.std(recall_list))
print()
print("F1-score List:", f1_list)
print("Mean F1-score:", np.mean(f1_list))
print("Standard Deviation of F1-score:", np.std(f1_list))
print()
print("Specificity List:", specificity_list)
print("Mean Specificity:", np.mean(specificity_list))
print("Standard Deviation of Specificity:", np.std(specificity_list))
print()
print("Sensitivity List:", sensitivity_list)
print("Mean Sensitivity:", np.mean(sensitivity_list))
print("Standard Deviation of Sensitivity:", np.std(sensitivity_list))
print()
print("AUC-ROC List:", roc_auc_list)
print("Mean AUC-ROC:", np.mean(roc_auc_list))
print("Standard Deviation of AUC-ROC:", np.std(roc_auc_list))
print()
print("Best parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)