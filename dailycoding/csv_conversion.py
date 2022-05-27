import sys
from io import StringIO
import pandas as pd
import os
import time

# csv_path="/mapr/bsbpmapr.cluster.com/user/mapr/CSV_FILE/bsbp_purchs_csv/dongbaek_upload_csv/"
# rs_path="/mapr/bsbpmapr.cluster.com/user/mapr/CSV_FILE/bsbp_purchs_csv/dongbaekjeon_csv2/"
# csvEnCd = 'utf-8'    # CSV encoding (euc-kr , utf-8)
csv_path = "D:\\python_workspace\\csv_org\\"
rs_path = "D:\\python_workspace\\csv_cvt\\"
csvEnCd = 'utf-8-sig'  # CSV encoding (euc-kr , utf-8)

file_list = os.listdir(csv_path)
file_list_csv = [file for file in file_list if file.endswith(".csv")]
rowsLen = len(file_list_csv)

print(file_list_csv)
print("------------------[총 ", rowsLen, " 개의 대상 파일]------------------")

for i in range(0, rowsLen):
    print("===================[", i + 1, " 번째 파일]===================")
    print("======[ 대상 csv ] " + file_list_csv[i])

    file_nm = file_list_csv[i].replace(".csv", "")
    print("======[ 처리시작 csv ] " + file_nm)
    file_nm = file_nm.replace("부산빅대이터_", "")

    try:
        orgCSV = pd.read_csv(csv_path + file_list_csv[i], encoding=csvEnCd, sep=',', engine='c', low_memory=False)
        file = csv_path + file_list_csv[i]
        if os.path.isfile(file):
            os.remove(file)
    except Exception as inst:
        old_stderr = sys.stderr
        result = StringIO()
        sys.stderr = result

        orgCSV = pd.read_csv(csv_path + file_list_csv[i], encoding=csvEnCd, sep=',', engine='c', low_memory=False, on_bad_lines='warn')

        sys.stderr = old_stderr
        result_string = result.getvalue()

        current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
        current_date = time.strftime("%Y_%m_%d", time.localtime(time.time()))

        with open(csv_path + file_nm + f"_{current_date}" + ".log", "a") as f:
             f.write(f"[{current_time}] : " + file_list_csv[i] + "\n")
             for line in result_string.split(r'\n'):
                 f.write(line)
                 f.write('\n')

    orgCSV.to_csv(rs_path + file_nm + ".csv", sep='|', encoding=csvEnCd, index=False, float_format='%.0f')

    print("======[ csv 변환완료 ] " + rs_path + file_nm + ".csv")
