import csv
import pandas as pd
import traceback
import time

def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    current_date = time.strftime("%Y_%m_%d", time.localtime(time.time()))

    with open(f"{current_date}"+"_Log.txt", "a") as f:
        f.write(f"[{current_time}] - {error}\n")
try:
    path = 'D:/PycharmProjects/dailyCoding/dailycoding/'
    file = 'DBJ_Wik_USER_USE_20210812081921.csv'
    f = open(path+file, 'r',  encoding='UTF8')
    reader = csv.reader(f)

    csv_list = []
    for l in reader:
        csv_list.append(l)
    f.close()

    log_df = pd.DataFrame(csv_list)
    print(log_df)

except Exception as inst:
    path = 'D:/PycharmProjects/dailyCoding/dailycoding/'
    file = 'DBJ_Wik_USER_USE_20210812081921.csv'
    f = open(path + file, 'r',  encoding='UTF8')
    reader2 = csv.reader(f)

    csv_list2 = []
    for l in reader2:
        csv_list2.append(l)
    f.close()
    log_df = pd.DataFrame(csv_list2)
    print(log_df)

    err = traceback.format_exc(limit=None, chain=True)
    ErrorLog(str(err))


#reader.to_csv('result4.csv', sep='|')
