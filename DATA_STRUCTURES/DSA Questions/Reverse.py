"""
This is a Program for reversing a array or string
"""
def reverse(A,start,end):
    while(start<end):
        temp=A[start]
        A[start]=A[end]
        A[end]=temp
        start=start+1
        end=end-1
