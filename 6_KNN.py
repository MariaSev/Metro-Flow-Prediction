from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from joblib import dump
import pandas as pd
import numpy as np
import csv
import numpy as np

def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


data = pd.read_csv("PC_Dataframe.csv", sep=';')

features = [str(i) for i in range(15)]
X = data.loc[:, features].values
y = data.loc[:,'target'].values
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


report_writer = open("knn_report.txt", "w")


knn = KNeighborsClassifier(n_neighbors = 2)




knn.fit(X_train,y_train)
dump(knn, 'knn.pkl')

y_pred = knn.predict(X_test)

report_writer.write(str(2)+"\n")

report_writer.write("MAE: " +str(mean_absolute_error(y_test, y_pred))+"\n")
report_writer.write("MSE: " +str(mean_squared_error(y_test, y_pred))+"\n")

report_writer.write("\n")

	
report_writer.close()
print("done.")


