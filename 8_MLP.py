from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
from joblib import dump
import pandas as pd
import numpy as np
import csv


data = pd.read_csv("PC_Dataframe.csv", sep=';')

features = [str(i) for i in range(15)]
X = data.loc[:, features].values
y = data.loc[:,'target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

report_writer = open("MLP_report.txt", "w")

for n in range(5,6):
    clf = MLPRegressor(hidden_layer_sizes=(n,), activation='logistic', solver='sgd', learning_rate='constant', learning_rate_init=0.002, momentum=0.8)

    clf.fit(X_train,y_train)
    dump(clf, 'MLP.pkl')

    
    y_pred = clf.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    report_writer.write(str(n)+"\n")
    report_writer.write("MAE: " +str(mae)+"\n")
    report_writer.write("MSE: " +str(mse)+"\n")

    print(n)
    print(mae)
    print(mse)
    print("")

report_writer.close()
print("done.")


        
