
import time
t = time.localtime()


h=t[3]
m= t[4]
s= t[5]+1

while s<61:
        print("Time Ecuador: ",h,":",m,":",s)
        s=s+1
        time.sleep(1)
        if s==60:
            s=0
            m=m+1
            if m==60:
                m=0
                h=h+1
                if h==24:
                    h=0
                    
                    
import time
t=time.localtime()
x=t[8]

while (x!=60):
    t=time.localtime()
    print(t[3],":",t[4],":",t[5])
    time.sleep(1)
                

                
