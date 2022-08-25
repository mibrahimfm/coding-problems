def isInputValid(s):
    parenthesesCount = 0
    bracketsCount = 0
    curlyBracesCount = 0
    
    for c in s:
        if parenthesesCount < 0 or bracketsCount < 0 or curlyBracesCount < 0:
            return False
        
        match c:
            case '(':
                parenthesesCount += 1
            case ')':
                parenthesesCount -= 1 
            case '[':
                bracketsCount += 1          
            case ']':
                bracketsCount -= 1
            case '{':
                curlyBracesCount += 1
            case '}':
                curlyBracesCount -= 1  
            case other:
                pass 
    
    if parenthesesCount == 0 and bracketsCount == 0 and curlyBracesCount == 0:
        return True
    return False

# Test Program
# should return False
print(isInputValid("()(){(())"))

# should return True
print(isInputValid(""))

# should return True
print(isInputValid("([{}])()"))

#should return False
print(isInputValid("(([]]}[{}])()))"))

#should return True
print(isInputValid("()[]{}"))

#should return False
print(isInputValid("]["))

#should return True
print(isInputValid("(((()(((()))))))"))