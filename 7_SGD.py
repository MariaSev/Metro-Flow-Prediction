from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from joblib import dump
import pandas as pd
import numpy as np
import csv
from sklearn.linear_model import SGDClassifier
import random

def batches(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

        
data = pd.read_csv("PC_Dataframe.csv", sep=';')

features = [str(i) for i in range(15)]
X = data.loc[:, features].values
y = data.loc[:,'target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

report_writer = open("SGD_report.txt", "w")

clf = SGDClassifier(loss='log') # The ‘log’ loss gives logistic regression, a probabilistic classifier. 
shuffledRange = [ i for i in range(len(X_train)) ]
n_iter = 100
for n in range(n_iter):
    random.shuffle(shuffledRange)
    shuffledX = [X_train[i] for i in shuffledRange]
    shuffledY = [y_train[i] for i in shuffledRange]
    for batch in batches(range(len(shuffledX)), 7544):#105 * 8 23 41
        clf.partial_fit(shuffledX[batch[0]:batch[-1]+1], shuffledY[batch[0]:batch[-1]+1], classes=np.unique(y)) #?  last param
dump(clf,'SGD.pkl')

y_pred = clf.predict(X_test)

report_writer.write("MAE: " +str(mean_absolute_error(y_test, y_pred))+"\n")
report_writer.write("MSE: " +str( mean_squared_error(y_test, y_pred))+"\n")

report_writer.close()
print("done.")


        
