import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from joblib import load
import warnings
warnings.filterwarnings("ignore")

day = 13

out_st=21
in_st=12

features_links=[]

with open("Principal_Components.csv", 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        if int(row[1])==out_st and int(row[2])==in_st and int(row[3])==day:
            features_links.append(int(row[0]))

features_array=[]
values=[]
with open("PC_Dataframe.csv", 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        if int(row[0]) in features_links:
            features_array.append([float(i) for i in row[1:-1]])
            values.append(float(row[-1]))


fig1, subplots = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

x=[0.5*i for i in range(48)]
fig1.axes[0].plot(x, values,color='black',linewidth=1)
print(values)
y1=[]
with open('knn.pkl', 'rb') as fid:
    regressor = load(fid)
    y1=regressor.predict(features_array)
fig1.axes[0].plot(x, y1.tolist(),color='forestgreen',linewidth=0.8)

y2=[]
with open('SGD.pkl', 'rb') as fid:
    regressor = load(fid)
    y2=regressor.predict(features_array)
fig1.axes[0].plot(x, y2.tolist(),color='crimson',linewidth=0.8)

y3=[]
with open('MLP.pkl', 'rb') as fid:
    regressor = load(fid)
    y3=regressor.predict(features_array)
fig1.axes[0].plot(x, y3.tolist(),color='dodgerblue',linewidth=0.8)

knn_patch        = mpatches.Patch(color='forestgreen',label='KNN')
sgd_patch        = mpatches.Patch(color='crimson',    label='SGD')
mlp_patch        = mpatches.Patch(color='dodgerblue', label='MLP')
true_value_patch = mpatches.Patch(color='black',      label='True value')
plt.legend(handles=[knn_patch, sgd_patch, mlp_patch, true_value_patch])

plt.xlabel('Time')
plt.ylabel('Passengers number')

plt.xticks([i for i in range(0,25,4)], [i for i in range(0,25,4)])
plt.show()



