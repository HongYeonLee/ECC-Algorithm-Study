from BinaryTree import BTNode

#모스 코드 표 리스트에 (문자, 코드) 형의 튜플로 저장
table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

#모스 코드 인코딩 함수
def encode(ch):
    idx = ord(ch) - ord('A') #리스트에서 해당 문자의 인덱스
    return table[idx][1] #해당 문자의 모스 부호 변환


#단순 모스 코드 디코딩 함수
def decode_simple(morse):
    for tp in table: #모스 코드 표의 모든 문자들에 대해, 튜플을 하나씩 꺼내서
        if morse == tp[1]: #찾는 코드와 같으면
            return tp[0] #그 코드의 문자 리턴

#모스 코드 디코딩을 위한 결정 트리 만들기
def make_morse_tree():
    root = BTNode(None, None, None)
    for tp in table: #tp: 모스 코드 표의 각 항목
        code = tp[1] #tp[1]: 모스 코드
        node = root #루트부터 탐색
        for c in code:
            if c == '.':
                if node.left == None: #왼쪽 자식이 비었으면 빈 노드를 추가, 왼쪽 자식으로 진행
                    node.left = BTNode(None, None, None)
                node = node.left

            elif c == '-':
                if node.right == None: #선(-)이면 오른쪽으로 이동
                    node.right = BTNode(None, None, None)
                node = node.right
        
        node.data = tp[0] #최종 노드에 문자(tp[0]) 부여
    return root

#결정 트리를 이용한 디코딩
def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left 

        elif c == '-':
            node = node.right

    return node.data

#테스트 코드
morseCodeTree = make_morse_tree() #모스코드 결정트리를 만듦, morseCodeTree가 루트 노드
str = input("입력 문장: ")
mlist = []

#문자 -> 모스코드 인코드
for ch in str:
    code = encode(ch)
    mlist.append(code)

print("Morse Code: ", mlist)
print("Decoding: ", end='')

#모스코드 -> 문자 디코드
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')

print()
