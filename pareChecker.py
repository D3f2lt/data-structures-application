## Author: D3f2lt ##

from stack import Stack

def pareChecker(strSymbols):
    """strSymbols is a string object"""
    s = Stack()
    balanced = True
    index = 0
    while index < len(strSymbols) and balanced:
        char = strSymbols[index]
        if char == "(":
            s.push(char)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
