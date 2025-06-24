def isValid(s: str) -> bool:

    stack = []
    dicto = {")" : "(",
             "]" : "[",
             "}" : "{"}
    
    if s[0] in dicto.keys():
        return False

    for i in s:
        if i in dicto.keys():
            if stack and stack[-1] == dicto[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    
    return True if not stack else False