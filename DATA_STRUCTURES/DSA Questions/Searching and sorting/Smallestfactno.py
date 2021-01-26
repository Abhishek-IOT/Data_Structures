def factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n*factorial(n-1)
def trailingzero(no):
    for i in range(1,100):
        fact=factorial(i)
        print(fact)
        count=0
        for j in range(1,fact):
            if fact%10==0:
                count+=1
                if count==no:
                    return count
            else:
                break
    return -1
if __name__ == '__main__':
    n=6
    m=trailingzero(n)
    print(m)

