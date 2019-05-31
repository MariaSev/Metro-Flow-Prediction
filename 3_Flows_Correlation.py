import pandas as pd
import numpy as np
import csv
import seaborn as sns
import matplotlib.pyplot as plt

line_base=88
target_in_st=4
target_out_st=20


   
flows_3d = np.zeros(shape = (7, 7, 30, 48))

with open("Corr_Metro_201802.csv", 'r') as file:
    reader = csv.reader(file, delimiter=';') 
    next(reader)
    for row in reader:
        for i in range(7):# 0 1 2 3 4 5 6
            for j in range(7):
                if int(row[2]) == line_base+target_in_st+(i-3) and int(row[3]) == line_base+target_out_st+(j-3):
                    flows_3d[i][j][int(row[0])-1][int(row[1])] = row[6] #[строка в корр][столбец в корр][число][час]  int(row[0][8:10])-1   int(row[0][11:])

    flows_2d   = np.zeros(shape = (49, 30*48))
    
    row_num=0
    for row in flows_3d:
        flow_num=0
        for flow in row:
            flows_2d[row_num*7+flow_num] = np.ravel(flow)
            flow_num+=1
        row_num+=1
    

    df = pd.DataFrame(flows_2d.T)# нужно ли транспонировать?!
                                 # да, т.к. "Compute pairwise correlation of columns(!), excluding NA/null values."
    
    c1=df.corr('pearson')
    print("Pandas df.corr('pearson'): %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c1[24][0], c1[24][1], c1[24][2], c1[24][3], c1[24][4], c1[24][5], c1[24][6]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c1[24][7], c1[24][8], c1[24][9], c1[24][10],c1[24][11],c1[24][12],c1[24][13]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c1[24][14],c1[24][15],c1[24][16],c1[24][17],c1[24][18],c1[24][19],c1[24][20]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c1[24][21],c1[24][22],c1[24][23],c1[24][24],c1[24][25],c1[24][26],c1[24][27]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c1[24][28],c1[24][29],c1[24][30],c1[24][31],c1[24][32],c1[24][33],c1[24][34]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c1[24][35],c1[24][36],c1[24][37],c1[24][38],c1[24][39],c1[24][40],c1[24][41]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c1[24][42],c1[24][43],c1[24][44],c1[24][45],c1[24][46],c1[24][47],c1[24][48]))
    print("")
    
    c2=df.corr('kendall')
    print("Pandas df.corr('kendall'): %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c2[24][0], c2[24][1], c2[24][2], c2[24][3], c2[24][4], c2[24][5], c2[24][6]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c2[24][7], c2[24][8], c2[24][9], c2[24][10],c2[24][11],c2[24][12],c2[24][13]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c2[24][14],c2[24][15],c2[24][16],c2[24][17],c2[24][18],c2[24][19],c2[24][20]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c2[24][21],c2[24][22],c2[24][23],c2[24][24],c2[24][25],c2[24][26],c2[24][27]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c2[24][28],c2[24][29],c2[24][30],c2[24][31],c2[24][32],c2[24][33],c2[24][34]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c2[24][35],c2[24][36],c2[24][37],c2[24][38],c2[24][39],c2[24][40],c2[24][41]))
    print("                           %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c2[24][42],c2[24][43],c2[24][44],c2[24][45],c2[24][46],c2[24][47],c2[24][48]))
    print("")
    
    c3=df.corr('spearman')
    print("Pandas df.corr('spearman'): %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c3[24][0], c3[24][1], c3[24][2], c3[24][3], c3[24][4], c3[24][5], c3[24][6]))
    print("                            %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c3[24][7], c3[24][8], c3[24][9], c3[24][10],c3[24][11],c3[24][12],c3[24][13]))
    print("                            %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c3[24][14],c3[24][15],c3[24][16],c3[24][17],c3[24][18],c3[24][19],c3[24][20]))
    print("                            %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c3[24][21],c3[24][22],c3[24][23],c3[24][24],c3[24][25],c3[24][26],c3[24][27]))
    print("                            %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c3[24][28],c3[24][29],c3[24][30],c3[24][31],c3[24][32],c3[24][33],c3[24][34]))
    print("                            %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c3[24][35],c3[24][36],c3[24][37],c3[24][38],c3[24][39],c3[24][40],c3[24][41]))
    print("                            %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f"% (c3[24][42],c3[24][43],c3[24][44],c3[24][45],c3[24][46],c3[24][47],c3[24][48]))
    print("")
    
    fig1, subplots1 = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)
    
    corrs1=np.zeros(shape = (7, 7))
    k=0
    for i in range(7):
        for j in range(7):
            corrs1[i][j]=c1[24][k]
            k+=1
    heatplot0  = fig1.axes[0].imshow(corrs1, 'GnBu', origin='lower',  vmin=0., vmax=1.)
    fig1.axes[0].axis('off')
    fig1.axes[0].set_title("Pearson")
    #fig1.colorbar(heatplot0)
    
    corrs2=np.zeros(shape = (7, 7))
    k=0
    for i in range(7):
        for j in range(7):
            corrs2[i][j]=c2[24][k]
            k+=1
    heatplot1  = fig1.axes[1].imshow(corrs2, 'GnBu', origin='lower', interpolation='none', vmin=0., vmax=1.)
    fig1.axes[1].axis('off')
    fig1.axes[1].set_title("Kendall")
    #fig1.colorbar(heatplot1)
    
    corrs3=np.zeros(shape = (7, 7))
    k=0
    for i in range(7):
        for j in range(7):
            corrs3[i][j]=c3[24][k]
            k+=1
    heatplot2  = fig1.axes[2].imshow(corrs3, 'GnBu', origin='lower', interpolation='none', vmin=0., vmax=1.)
    fig1.axes[2].axis('off')
    fig1.axes[2].set_title("Spearman")
    #fig1.colorbar(heatplot2)
    
       
    fig2, subplots2 = plt.subplots(nrows=7, ncols=7, sharex=True, sharey=True)
    br_num=0
    for flow in flows_2d:
        fig2.axes[br_num].set_title(str(round(c1[24][br_num],2)),fontdict={'fontsize': 7, 'fontweight': 'light', 'verticalalignment':'center'})
        fig2.axes[br_num].scatter(flow, flows_2d[24], s = 0.5, color = 'steelblue')
        fig2.axes[br_num].spines["top"].set_visible(False)
        fig2.axes[br_num].spines["right"].set_visible(False)
        plt.xlim([0, 25])
        br_num+=1
        
    plt.show()
            
