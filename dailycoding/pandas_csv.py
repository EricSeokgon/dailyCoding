import sys
from io import StringIO
import pandas as pd
import time


def ErrorLog(error: str):
    current_time = time.strftime("%Y.%m.%d/%H:%M:%S", time.localtime(time.time()))
    current_date = time.strftime("%Y_%m_%d", time.localtime(time.time()))

    with open(f"{current_date}"+"_bad_lines_log.txt", "a") as f:
        f.write(f"[{current_time}]\n")
        for line in error.split(r'\n'):
            f.write(line)
            f.write('\n')

old_stderr = sys.stderr
result = StringIO()
sys.stderr = result

try:

    csv_input = pd.read_csv(filepath_or_buffer="D:/PycharmProjects/dailyCoding/dailycoding/DBJ_Wik_USER_USE_20210812081921.csv", encoding="utf-8", sep=',', engine='c')

except Exception as inst:

    csv_input = pd.read_csv(filepath_or_buffer="D:/PycharmProjects/dailyCoding/dailycoding/DBJ_Wik_USER_USE_20210812081921.csv", encoding="utf-8", sep=',', engine='c', error_bad_lines=False)

    sys.stderr = old_stderr
    result_string = result.getvalue()

    err = result.getvalue()
    ErrorLog(str(err))

csv_input.to_csv('result1.csv', sep='|')
