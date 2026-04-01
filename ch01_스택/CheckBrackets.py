from StackClass import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)
    
    for char in statement:
        if char in ('{', '[', '('):
            stack.push(char)
        elif char in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if ((char == '}' and left != '{') or
                   (char == ']' and left != '[') or
                   (char == ')' and left != '(')):
                   return False
    
    return stack.isEmpty()
    
if __name__ == "__main__":
    message = input("문자열 입력: ")
    if checkBrackets(message):
        print("문자열이 맞습니다")
    else:
        print("문자열이 틀립니다")
