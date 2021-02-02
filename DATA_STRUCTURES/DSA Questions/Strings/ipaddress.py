def is_valid(ip):
    # Splitting by "."
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        print(int(i),"i")
        if (len(i) > 3 or int(i) < 0 or
                int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
                i[0] == '0'):
            return False

    return True
def convert(s):
    l=len(s)
    if l>12:
        return []
    new=s
    l1=[]
    for i in range(1,l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                new=new[:k]+"."+new[k:]
                new=new[:j]+"."+new[j:]
                new=new[:i]+"."+new[i:]
                if is_valid(new):
                    l1.append(new)
    return l1
if __name__ == '__main__':
    A = "25525511135"
    l=convert(A)
    print(l)
