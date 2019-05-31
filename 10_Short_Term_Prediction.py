import csv
from joblib import load
import warnings
import time
warnings.filterwarnings("ignore")

stations = {'Медведково':0,'Бабушкинская':1,'Свиблово':2,'Ботанический сад':3,
            'ВДНХ':4,'Алексеевская':5,'Рижская':6,'Проспект Мира':7,
            'Сухаревская':8,'Тургеневская':9,'Китай-город':10,'Третьяковская':11,
            'Октябрьская':12,'Шаболовская':13,'Ленинский проспект':14,
            'Академическая':15,'Профсоюзная':16,'Новые Черемушки':17,
            'Калужская':18,'Беляево':19,'Коньково':20,'Тёплый Стан':21,
            'Ясенево':22,'Новоясеневская':23 }

def get_day():
    print("Введите день:", end=' ')
    d=eval(input())
    if 0<=d<=28:
        return d
    else:
        raise Exception

def get_time():
    print("        время:", end=' ')
    hour, min = input().split(':')
    if 0<=int(hour)<=24 and 0<=int(min)<=59:
        return int(hour)*2+1 if int(min)>29 else int(hour)*2
    else:
        raise Exception

def get_orig():
    print("        станцию отбытия:", end=' ')
    return stations[input()]

def get_dest():
    print("        станцию прибытия:", end=' ')
    return stations[input()]

while True:
    try:
        day=get_day()
        h_hour=get_time()
        orig_st=get_orig()
        dest_st=get_dest()
    except Exception:
        print("Ошибка. Попробуйте снова\n")
    else:
        start_time = time.time()
        features_links=[]
        with open("Principal_Components.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if int(row[1])==orig_st and int(row[2])==dest_st\
                   and int(row[3])==day and int(row[4])==h_hour:
                    features_link = int(row[0])
        features_array=[]
        act_value=[]
        with open("PC_Dataframe.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            for row in reader:
                if int(row[0])==features_link:
                    features_array.append([float(i) for i in row[1:-1]])
                    act_value.append(float(row[-1]))
        y1, y2 = [], []
        with open('knn.pkl', 'rb') as file:
            regressor = load(file)
            y1=regressor.predict(features_array)        
        with open('MLP.pkl', 'rb') as file:
            regressor = load(file)
            y2=regressor.predict(features_array)
            
        interval = str(h_hour//2)+":00-"+str(h_hour//2)+":30" if h_hour%2==0\
                   else str(h_hour//2)+":30-"+str(h_hour//2+1)+":00"
        print("Прогноз по данному маршруту для интервала "+interval+" : "+str(int((y1[0]+y2[0])/2))+" пассажиров.")
        print("(истинное значение -- "+str(int(act_value[0]))+")")
        print("Время выполнения -- %s секунд\n" % (time.time() - start_time))
        
