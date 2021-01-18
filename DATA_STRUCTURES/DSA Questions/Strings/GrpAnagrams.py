"""
Print Anagrams Together
Medium Accuracy: 55.49% Submissions: 3524 Points: 4
Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array.
Look at the sample case for clarification.
Input:
N = 5
words[] = {act,god,cat,dog,tac}
Output:
god dog
act cat tac
Explanation: There are 2 groups of
anagrams god, dog make group 1.
act, cat, tac make group 2.
Logic=sort the words of the lexicographically and then check that the sortedword is present in the dictionary
if present then assign the value that are anagram else append the sortedword in dictionsry.
"""
def groupana(s):
    d={}
    for word in s:
        sortedword="".join(sorted(word))
        if sortedword not in d:
            d[sortedword]=[word]
        else:
            d[sortedword].append(word)
    r=[]
    for i in d.values():
        r.append(i)
    return r




if __name__ == '__main__':
    arr=['act','god','cat','dog','tac']
    my=groupana(arr)
    print(my)
