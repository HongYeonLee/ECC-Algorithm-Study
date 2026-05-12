from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a: #a = 3, b = 30일 때, 330 > 303 이므로 정렬시 a, b순서로 되어야함
        return -1 #-1의 의미: 입력값 a, b 중 a가 b보다 작으므로 오름차순 정렬시 a, b로 정렬
    elif a + b < b + a: #a=5, b=90일 때, 590 < 905이므로 정렬시 b, a 순서로 되어야함 (b가 a보다 작다고 해야함)
        return 1 #1의 의미: 입력값 a, b 중 a가 b보다 크므로 오름차순 정렬시 b, a로 정렬
    else:
        return 0 #0의 의미: 입력값 a=b이므로 순서를 그대로 둠

def solution(numbers):
    numStr = list(map(str, numbers))
    sortedNum = sorted(numStr, key=cmp_to_key(compare)) #cmp_to_key는 key에 원소 2개를 비교하는 함수를 정렬 기준으로 사용할 수 있게 해준다.
    answer = "".join(sortedNum)

    if answer[0] == "0":
        return "0"
    
    return answer

print(solution([3, 30, 34, 5, 9]))