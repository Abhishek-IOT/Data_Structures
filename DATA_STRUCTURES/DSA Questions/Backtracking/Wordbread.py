def dictionarycon(word):
    dictionary = {"mobile", "samsung", "sam", "sung", "man",
                  "mango", "icecream", "and", "go", "i", "love", "ice", "cream"}
    return word in dictionary
def wordbb(s):
    wordbbutil(s,len(s),"")
def wordbbutil(s,n,result):
    for i in range(1,n+1):
        prefix=s[:i]
        if dictionarycon(prefix):
            if i==n:
                result+=prefix
                print(result)
                return
            wordbbutil(s[i:],n-i,result+prefix+" ")
if __name__ == '__main__':

    wordbb("ilovesamsungmobile")
