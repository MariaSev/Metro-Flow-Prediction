import csv
import time
import matplotlib.pyplot as plt
from color_map import st_colors
from scipy.stats.stats import normaltest
import datetime
import numpy as np

 
with open("Row_Data.csv") as f_obj:
    sv=[]
    reader = csv.reader(f_obj, delimiter=',')
    next(reader) # skip first line 
    for row in reader:
        sv.append(int(row[3]+row[4]))

    print(datetime.datetime.now())
    
    o, d = np.histogram(sv)


    plt.hist(sv,1000)
    
    plt.show()
