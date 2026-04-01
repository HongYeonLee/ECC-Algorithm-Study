from BinaryTree import BTNode, inorder, postorder, preorder

def evaluate(node): #루트 노드 전달
    if node is None:
        return ()
    
    elif node.isLeaf(): #단말 노드이면 -> 피연산자
        return node.data #그 노드의 값(데이터) 반환
    
    else: #루트나 가지노드라면 -> 연산자
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)

        if node.data == '+':
            return op1 + op2
        elif node.data == '-':
            return op1 - op2
        elif node.data == '*':
            return op1 * op2
        elif node.data == '/':
            return op1 / op2

def buildETree(expr): #후위표기 식을 expr로 전덜
    if len(expr) == 0:
        return None
    
    token = expr.pop() #후위순회는 수식을 뒤에서 앞으로 처리하기에 pop을해서 맨 뒤의 요소를 꺼냄
    if token in "+-*/": #연산자라면
        node = BTNode(token)
        node.right = buildETree(expr) #기존 후위표기 식에서 맨 뒤의 값을 하나 뺀 후위표기 식
        node.left = buildETree(expr)
        return node
    
    else: #피연산자라면
        return BTNode(float(token)) #피연산자이면 단말노드이므로 노드를 만들어 바로 리턴

#테스트 코드
str = input("입력 (후위표기): ") #후위표기식 입력
expr = str.split() #토큰 리스트로 변환
print("토큰분리(expr): ", expr)
root = buildETree(expr) #후위표기식을 수식 트리로 만들고 루트 리턴

print('\n  Pre-Order : ', end=''); preorder(root)
print('\n   In-Order : ', end=''); inorder(root)
print('\n Post-Order : ', end=''); postorder(root)
print('\n 계산 결과: ', evaluate(root)) #수식계산