def solution(sizes):
    for size in sizes:
        size.sort()

    xMax = sizes[0][0]
    yMax = sizes[0][1]
    for i in range(len(sizes)):
        if (xMax < sizes[i][0]):
            xMax = sizes[i][0]

        if (yMax < sizes[i][1]):
            yMax = sizes[i][1]
    
    return xMax * yMax

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))