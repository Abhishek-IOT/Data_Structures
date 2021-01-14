"""
Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the function should return 'true' for exp = “[()]{}{[()()]()}” and 'false' for exp = “[(])”.
Logic=Firstly append the opening brackets and check for the closing bracket if present then
pop the pop the stack .If a bracket left that means not balanced else balanced.
"""
def balance(s):
    l=len(s)
    stack=[]
    for char in s:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            current=stack.pop()
            if current=='(' and char!=')':
                return False
            if current=='[' and char!=']':
                return False
            if current=='{' and char!='}':
                return False
    if(stack):
        return False
    return True
if __name__ == '__main__':
    expr = "{()}[]"
    if(balance(expr)):
        print("Yes")
    else:
        print("No")
