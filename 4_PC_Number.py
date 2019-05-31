from sklearn.decomposition import TruncatedSVD
import csv
import numpy as np

line_beg=88

flows_3d = np.zeros(shape = (24,24,30*48))
features = np.zeros(shape = (552*(30*48-5),45))# (n!/(n-m)!)*time_series_length

with open("Dataset.csv", 'r') as file:
    reader = csv.reader(file, delimiter=';') 
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
                    row_num+=1


svd = TruncatedSVD(algorithm='arpack', n_components=44, tol=0.0)
svd.fit(features)  



print(type(svd.singular_values_))  
print(sum(svd.singular_values_)/44)
av=sum(svd.singular_values_)/44
c=0
for i in svd.singular_values_:
    if i>av:
        c+=1
print("You shoud save "+str(c)+" components. (Kaiser)")

def myGenerator(n) :
    list = [1/i for i in range(1,n+1)]
    for i in range(n):
        yield sum(list[i:])

counter=0
br_stik = myGenerator(45)
for i in svd.singular_values_:
    if i/av > next(br_stik):
        counter+=1

print("You shoud save "+str(counter)+" components. (Broken srik)")
