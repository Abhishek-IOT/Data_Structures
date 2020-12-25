"""
This is the program to implement the union and intersection
INPUT=[1, 2, 3, 1, 6, 7]
"""
def union(arr1,arr2):
    for i in range(len(arr2)):
        arr1.append(arr2[i])
    print(arr1)
    # print(len(arr1))
    l=[]
    p=[]
    for i in arr1:
        if i not in l:
            l.append(i)
        else:
            p.append(i)
    print(l)
    print(p)

if __name__ == '__main__':
    arr1=[1,2,3]
    arr2=[1,6,7]
    union(arr1,arr2)

