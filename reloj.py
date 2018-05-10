
import time
t = time.localtime()


h=t[3]
m= t[4]
s= t[5]+1
x="am"
y="pm"
c = y
while s<61:
        print("Time Ecuador: ",h,":",m,":",s,c)
        s=s+1
        time.sleep(1)
        if s==60:
            s=0
            m=m+1
            if m==60:
                m=0
                h=h+1
                if h==12:
                    h=0
                    c=x
                    if c==x and h==13:
                        h=1
                        c=y
                    
            
                

                
