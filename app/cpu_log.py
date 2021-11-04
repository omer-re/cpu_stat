 
import os
from time import time, sleep
import psutil
import datetime;



LOG_FN="cpu_mem_log.txt"
INTERVAL_SEC=60


print("=====   CPU LOGGER START   =====\n")
print("log interval: {} sec\n".format(INTERVAL_SEC))

#create file, override previously existing files.
log_file= open(LOG_FN,'w')
log_file.close()


while True:
    # Getting all memory using os.popen()
    _, used_memory, total_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    mem_stat = round((used_memory / total_memory) * 100, 2)
    cpu_stat= psutil.cpu_percent(interval=1)
    cts = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # prepare log string
    log_str='timestamp: {} | CPU usage: {}% | memory usage {}%\n'.format(cts, cpu_stat, mem_stat)

    # open log file in append access
    log_file = open(LOG_FN, 'a')
    log_file.write(log_str)
    print(log_str)
    log_file.close() # release file while not needed.
    sleep(INTERVAL_SEC)


print("=====   CPU LOGGER END   =====\n")

