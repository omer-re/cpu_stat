import os
from time import time, sleep
import psutil
import datetime;

print("=====   CPU LOGGER START   =====\n")
LOG_FN="cpu_mem_log.txt"
log_file= open(LOG_FN,'w')
log_file.close()


while True:
    # Getting all memory using os.popen()
    _, used_memory, total_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    # Memory usage
    #print("RAM memory % used:", round((used_memory / total_memory) * 100, 2))
    mem_stat = round((used_memory / total_memory) * 100, 2)
    #print(psutil.virtual_memory().used * 100 / psutil.virtual_memory().total)
    #print('memory % bytes used:', psutil.virtual_memory()[2])
    
    
    print('memory MiB used (mem+swap):', used_memory)
    cpu_stat= psutil.cpu_percent(interval=1)
    cts = datetime.datetime.now()
    log_str='timestamp: {}\tCPU usage: {}%\tmemory usage {}%'.format(cts, cpu_stat, mem_stat)
    log_file = open(LOG_FN, 'a')
    log_file.write(log_str)
    log_file.close()
    
    sleep(5)
    #sleep(60 -time() % 60)
    

print("=====   CPU LOGGER END   =====\n")

    


    

    


    


    