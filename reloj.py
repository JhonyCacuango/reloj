import time
t=time.localtime()
x=t[5]
for x in range(1, 60):
    
    print(t[3],":",t[4],":",t[5])
    t=time.localtime()
    