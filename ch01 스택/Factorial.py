#반복을 이용해 팩토리얼 구하기
def factorial_iter(n):
    result = 1
    for k in range(2, n+1): #k = 2, 3, 4 ... n
        result = result * k
    return result

#재귀 호출을 이용해 팩토리얼 구하기

def factorial_recurr(n):
    if n == 1:
        return n
    else:
        return n * factorial_recurr(n-1)
    

if __name__ == "__main__":
    num = int(input("구하려고 하는 팩토리얼 값을 입력하세요: "))
    result = factorial_recurr(num)
    print("답은 ", result, " 입니다")