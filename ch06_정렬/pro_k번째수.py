def solution(array, commands):
    answer = []
    for comm in commands:
        slicedArr = array[comm[0]-1:comm[1]] #배열 자르기
        slicedArr.sort() #배열 오름차순 정렬
        answer.append(slicedArr[comm[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))