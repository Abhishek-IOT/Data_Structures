def ispowerof2(n):
    if n&(n-1)==0:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    ispowerof2(16)
    ispowerof2(20)