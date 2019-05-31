from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import csv

line_beg=88
#line_end=112

flows_3d = np.zeros(shape = (24,24,30*48))
features = np.zeros(shape = (552*(30*48-5),46))# (n!/(n-m)!)*time_series_length, features num

with open("Dataset.csv", 'r') as file:
    reader = csv.reader(file, delimiter=';') 
    with open("Principal_Components.csv", 'w', newline='') as dst:
        writer = csv.writer(dst, delimiter=';')
        
        next(reader)
        for row in reader:
            #if int(row[0])-1<30:
            flows_3d[(int)(row[2])-line_beg][(int)(row[3])-line_beg][ 48 * (int(row[0])-1) + int(row[1]) ] = int(float(row[6]))
            #       [origin]              [destination]         [time]
        row_num=0
        for target_time in range(30*48-5):
            for target_o in range(24):
                for target_d in range(24):
                    if target_o!=target_d:
                    
                        col_num=0
                        for o_spatial_step in [-1,0,1]:
                            for d_spatial_step in [-1,0,1]:
                                for time_step in [-5,-4,-3,-2,-1]:
                                    if (target_o + o_spatial_step)<0:
                                        o_spatial_step=1
                                    if (target_d + d_spatial_step)<0:
                                        d_spatial_step=1
                                    if (target_o + o_spatial_step)>23:
                                        o_spatial_step=-1
                                    if (target_d + d_spatial_step)>23:
                                        d_spatial_step=-1
                                    
                                    features[row_num][col_num]=flows_3d[target_o + o_spatial_step][target_d + d_spatial_step][target_time + time_step]
                                    col_num+=1
                        features[row_num][col_num]=flows_3d[target_o][target_d][target_time]
                        pca_row=[row_num,target_o,target_d,(target_time+5)//48,(target_time+5)%48] #row_num - соответствующая строка в features
                        writer.writerow(pca_row)
                        row_num+=1

        df = pd.DataFrame(features)
        features_num = [i for i in range(45)]
        x = df.loc[:, features_num].values
        y = pd.DataFrame( features[:,45])
        x = StandardScaler().fit_transform(x)

        pca = PCA(n_components=15)
        principalComponents = pca.fit_transform(x)
        principalDf = pd.DataFrame(data = principalComponents)
    #print(principalDf.to_string())
    #print(pca.explained_variance_ratio_)
    #print(principalDf.shape)
    #print(y.shape) 
        finalDf = pd.concat([principalDf,y], axis=1)
    #print(finalDf.shape)

    
        
        
                    

        finalDf.to_csv("PC_Dataframe.csv", sep=';',header=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,'target'])
    






    
