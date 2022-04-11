def grau(g_mat: list, v: int) -> int:
    count = 0

    for number in g_mat[v]:
        if number != 0:
            count += 1

    return count


def regular(g_mat) -> bool:
    aux = grau(g_mat, 0)

    for i in range(1, len(g_mat)):
        if grau(g_mat, i) != aux:
            return print(False)

    return print(True)


def completo(g_mat) -> bool:
    for i in range(len(g_mat)):
        if grau(g_mat, i) != len(g_mat) - 1:
            return print(False)

    return print(True)


def grauList(gList: list, v: int) -> int:
    return len(gList[v])


def regularList(gList: list) -> bool:
    aux = grauList(gList)

    for i in range(1, len(gList)):
        if grauList(gList, i) != aux:
            return print(False)

    return print(True)


def completoList(gList) -> bool:
    for i in range(len(gList)):
        if grauList(gList, i) != len(gList) - 1:
            return print(False)

    return print(True)
