def factorial(inp):
    if inp==1:
        return 1
    else:
        return inp*factorial(inp-1)
if __name__ == '__main__':
    test=int(input())
    f=[]
    for i in range(test):
        inp=int(input())
        fact=factorial(inp)
        f.append(fact)
    for i in range(len(f)):
        print(f[i])