t=int(input())
while(t):
    h=int(input())
    a=int(input())
    time=0
    while(True):
        if time%2==0:
            h=h+3
            a=a+2
        else:
            if h>20:
                h = h - 20
                a = a + 5
            else:
                a = a - 10
                h = h - 5
        if a>0 and h>0:
            time+=1
        else:
            break
    t=t-1
    print(time)