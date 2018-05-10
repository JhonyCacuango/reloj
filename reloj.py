import time
t=time.localtime()
x=t[5]
while (x!=60):
    t=time.localtime()
    print(t[3],":",t[4],"/",t[5])
