import os, sys
import numpy as np
import time
file = sys.argv[1]
long = sys.argv[2]
#f = open("%s"%file,"r")
#data = f.readlines()
#f.close()
def view_bar(num, sum, bar_word):
    bar_word=bar_word.encode()
    rate = float(num) / float(sum)
    rate_num = int(rate * 100)
    print('\r%d%% :'%(rate_num))
    for i in range(0, num):
        os.write(1, bar_word)
    sys.stdout.flush()
data = []
for line in open('%s'%file,'r'):
        data.append(line)
i=0
os.system("mkdir jobs")
while i < len(data):
        a=float(i)
        b=float(long)
        Y = a//b
        with open("jobs/sh_%d_%d.sh"%(b,Y),"a+") as f:
                f.writelines("./submit/"+data[i])
        view_bar(i,len(data),"#")
        i+=1
        #time.sleep(0.1)
