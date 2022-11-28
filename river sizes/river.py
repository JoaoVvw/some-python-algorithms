m = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]


def river_sizes(matrix):
    c1 = 1
    c2 = 0
    c3 = 0
    c2temp = 0
    c3temp = 0
    history = []
    sizes = []
    for rows in matrix:
        for item in rows:
            if item == 1:
                c2temp = c2
                c3temp = c3
                while True:
                    matrix[c3temp][c2temp] = 2
                    if matrix[c3temp][c2temp - 1] == 1 and c2temp > 0:
                        history.append("left")
                        c2temp -= 1
                        c1 += 1
                    elif matrix[c3temp - 1][c2temp] == 1 and c3temp > 0:
                        history.append("up")
                        c3temp -= 1
                        c1 += 1
                    elif c2temp < len(matrix[0]) - 1 and matrix[c3temp][c2temp + 1] == 1:
                        history.append("right")
                        c2temp += 1
                        c1 += 1
                    elif c3temp < len(matrix) - 1 and matrix[c3temp + 1][c2temp] == 1:
                        history.append("down")
                        c3temp += 1
                        c1 += 1
                    else:
                        if len(history) > 0:
                            if history[-1] == "left":
                                c2temp += 1
                                history.pop()
                            elif history[-1] == "up":
                                c3temp += 1
                                history.pop()
                            elif history[-1] == "right":
                                c2temp -= 1
                                history.pop()
                            elif history[-1] == "down":
                                c3temp -= 1
                                history.pop()
                        else:
                            sizes.append(c1)
                            c1 = 1
                            c2 += 1
                            if c2 == len(matrix[0]):
                                c2 = 0
                                c3 += 1
                            break
            else:
                c2 += 1
                if c2 == len(matrix[0]):
                    c2 = 0
                    c3 += 1
    sizes.sort(reverse=True)
    print(sizes)


river_sizes(m)

