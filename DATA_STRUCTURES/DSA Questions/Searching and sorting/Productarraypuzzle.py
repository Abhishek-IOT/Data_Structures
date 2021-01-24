"""
Problem
 Editorial
 Submissions
Doubt Support
Product array puzzle
Easy Accuracy: 37.58% Submissions: 9275 Points: 2
Given an array A[] of size N, construct a Product Array P (of same size N) such that P[i] is equal to the product of all the elements of A except A[i].
Logic=Done the question wuthout using division operator.Make two functions leftprod and rightprod....We will find find the product according to
the index of the product.If the index is 0 then we will return the product of right prod else we will call both of the leftprod and rightprod and then
mutilply them both then append in the list.
"""
def leftprod(arr,start,index):
    prod=1
    for i in range(start,index):
        prod=prod*arr[i]
    return prod

def rightprod(arr,index):
    prod=1
    for i in range(index,len(arr)):
        prod=prod*arr[i]
    return prod
def prodpuzz(arr,l):
    pro=[]
    for i in range(l):
        if i==0:
             pro.append(rightprod(arr,i+1))
             print(pro)
        if i>0:
            right= rightprod(arr,i+1)
            print(right,"Right")
            left=leftprod(arr,0,i)
            print(left,"Left")
            mul=left*right
            pro.append(mul)
    return pro
if __name__ == '__main__':
    arr=[10, 3, 5, 6, 2]
    you=prodpuzz(arr,len(arr))
    print(you)
