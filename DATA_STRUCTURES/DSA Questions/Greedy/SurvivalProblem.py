def wesurvive(s,n,m):
    if (((n*6)<(m*7) and s>6) or m>n):
        print("NO we can not survive")
    else:
        days=(m*s)//n
        if (m*s)%n!=0:
            days+=1
            print("Yes we can survive")
            print(days)
if __name__=='__main__':
    wesurvive(10,16,2)
