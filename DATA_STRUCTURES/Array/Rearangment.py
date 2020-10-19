class Rearangment:
    """
    This is the method for rearrangment of the array
    """
    def fix(self,arr):
        for i in range(0,len(arr)):
            if arr[i]!=-1 and arr[i]!=i:
                x=arr[i]
                print(x,"The value of x")
            while(arr[x]!=-1 and arr[x]!=x):
                y=arr[x]
                arr[x]=x
                x=y
                print(y,"Tje value of y")
            if arr[i]!=i:
                arr[i]=-1
            #This is for having the value that are not present so we will place -1 there0


        for i in range(0,len(arr)):
            print(arr[i],end=" ")

if __name__ == '__main__':
    rearrange=Rearangment()
    arr=[3,1,2,0,4,-1]
    rearrange.fix(arr)
