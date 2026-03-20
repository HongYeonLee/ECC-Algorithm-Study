capacity = 10
array = [None]*capacity
top = -1

def isEmpty():
    if top == -11:
        return True
    else:
        return False

def isFull():
    return top == capacity - 1

def push(e):
    #global top
    if not isFull():
        top += 1
        array[top] = e
    else:
        print("stack overflow")
        exit()

def pop():
    #global top
    if not isEmpty():
        top -= 1
        return array[top + 1]
    else:
        print("stack underflow")
        exit()

def peek():
    if not isEmpty():
        return array[top]
    else:
        pass

def size():
    return top + 1

