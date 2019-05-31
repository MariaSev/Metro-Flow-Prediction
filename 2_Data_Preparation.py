import csv
import numpy as np

flows = np.zeros(shape = (30, 48, 24, 24, 2)) #[день][получасие суток][стонция от][станция до][]

with open("Row_Data.csv", 'r') as src:    
    reader = csv.reader(src, delimiter=',')        
    next(reader) # skip first line 
    for row in reader:
        day  = int(row[0][8:10])-1
        hour = int(row[0][11:13])
        half_hour=(hour*2+1) if int(row[0][14:15]) else hour*2
        orig = int(row[1])
        dest = int(row[2])
        val1 = int(row[3])
        val2 = int(row[4])
        if 88<=orig<=111 and 88<=dest<=111:
            flows[day][half_hour][orig-88][dest-88][0] = val1
            flows[day][half_hour][orig-88][dest-88][1] = val2          
    with open("Dataset.csv", 'w', newline='') as dst:
        writer = csv.writer(dst, delimiter=';')
        writer.writerow(['day','half-hour','orig_id','dest_id','customers_cnt','customers_cnt_end','average'])
        day_num=0
        for day in flows:
            half_hour_num=0
            for half_hour in day:
                orig_num=0
                for orig in half_hour:
                    dests_num=0
                    for dests in orig:
                        row=[day_num+1,half_hour_num,orig_num+88,dests_num+88,dests[0],dests[1],dests[0]+dests[1]]
                        writer.writerow(row)
                        dests_num  += 1
                    orig_num    += 1
                half_hour_num += 1
            day_num += 1
