def helper(time):
    if int(time[:2])>12:
        return -1
    if int(time[3:5])>59:
        return -1
    d={'12':"00",'13':"01","14":"02",
       "15":"03","16":"04","17":"05","18":"06",
       "19":"07","20":"08","21":"09","22":"10","23":"11","24":"12"}
    if time[6:]=='AM':
        if time[:2] in d:
            return d[time[:2]]+":"+time[3:5]
        else:
            return time[:2]+":"+time[3:5]
    else:
        return time[:2]+":"+time[3:5]
def helper2(time):
    time1=helper(time[:8])
    time2=helper(time[9:])
    return time1,time2
def func(time,time2):
    time=helper(time)
    time2=helper2(time2)
    print(time[2:])
    if int(time[2:])>time2[0][2:]:
        pass

func("12:01 AM","12:00 AM 11:42 PM")
# if __name__ == '__main__':
#     test=int(input())
#     p = str(input())
#     # print(p[6:])
#     # print(p[3:5])
#     # print(p[:2])
#     m=helper("12:01 AM")
#     print(m)
#     for i in range(test):
#         no=int(input())
#         string=""
#         for j in range(no):
#             time=str(input())
#
