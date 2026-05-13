def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct_sum = [[1, 0], [2, 0], [3, 0]]

    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            correct_sum[0][1] += 1
        if answers[i] == two[i%len(two)]:
            correct_sum[1][1] += 1
        if answers[i] == three[i%len(three)]:
            correct_sum[2][1] += 1

    result = []
    max_score = max(c[1] for c in correct_sum)
    for c in correct_sum:
        if c[1] == max_score:
            result.append(c[0])

    return result

print(solution([1,3,2,4,2]))