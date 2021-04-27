arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
arr.sort(key=lambda x:x[2])
arr.reverse()
print(*arr)
def getmaxjobs(arr):
      return arr[0][1]
l=[0]*getmaxjobs(arr)
print(l)
for j in range(len(l)):
       l[j]=arr[j][2]
print(l)
print(sum(l))



