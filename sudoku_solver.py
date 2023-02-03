import numpy as np

tabl = []
alphaDic = {}
alphaVal = {}
rout1 = []
alpha = []


def printab(A):
    B = list(A)
    for k in B:
        print("".join(list(map(str,list(k)))))


def simulator(Y, X, k, A):
    global alphaDic, alphaVal
    if k in A[Y, :]:
        return 0
    if k in A[:, X]:
        return 0
    if k in A[(Y // 3) * 3: (Y // 3) * 3 + 3, (X // 3) * 3: (X // 3) * 3 + 3]:
        return 0
    letter = alpha[Y][X]
    maxi = alphaVal[letter]
    calc = k + sum(A[p[0]][p[1]] for p in alphaDic[letter])
    compt = [A[p[0]][p[1]] for p in alphaDic[letter]].count(0)
    if compt == 1 and calc != maxi:
        return 0
    if compt  > 1 and calc >= maxi:
        return 0
    return 1


def Dfs_sudo(poz, A, nextP):
    global rout1, alphaDic, alphaVal
    if poz < len(rout1):
        YX = rout1[poz]
    else:
        printab(A)
        return 1
    Y = YX // 9
    X = YX % 9
    rt = 0
    k = 1
    letter = alpha[Y][X]
    calc = sum(A[p[0]][p[1]] for p in alphaDic[letter])
    while k < 10 and rt == 0 and k + calc <= alphaVal[letter]:
        if nextP[YX][k] != 0 :
            A[Y][X] = 0
            if (simulator(Y, X, k, A)):
                A[Y][X] = k
                if poz == 80:
                    printab(A)
                    return 1
                rt = Dfs_sudo(poz + 1, A, nextP)
        k +=1
    if rt == 0:
        A[Y][X] = 0
    return rt


def lautcher(A):
    nextP = [[1]*10 for _ in range(81)]
    for k in range(81):
        Y = k // 9
        X = k % 9
        if A[Y][X] == 0 :
            Yl = list(A[Y, :])
            Xl = list(A[:, X])
            Nll =list(A[(Y // 3) * 3: (Y // 3) * 3 + 3, (X // 3) * 3: (X // 3) * 3 + 3])
            Nl = []
            for l in Nll:
                Nl += list(l)
            potentiel = list(set(Yl + Xl + Nl))
            potentiel.sort()
            for m in potentiel:
                nextP[k][m] = 0
    if Dfs_sudo(0, A, nextP) :
        return 1
    return 0


for i in range(9):
    grid_line, grid_cages = input().split()
    tabl += [list(map(int,list(grid_line.replace('.', '0'))))]
    alpha += [list(grid_cages)]
    for j in range(9):
        if alphaDic.get((grid_cages[j]), )== None:
                alphaDic[grid_cages[j]] = [[i, j]]
        else:
            alphaDic[grid_cages[j]] += [[i, j]]
cages = input().split(' ')
for cage in cages:
    alphaVal[cage[0]] = int(cage[2:])
A = np.array(tabl)
routes = "".join(list(alphaDic.keys()))
route = [len(alphaDic[i]) for i in routes]
rout = []
for k in range(len(routes)): #no new route needed, just a good begin
    r = alphaVal[routes[k]]
    for p in range(15):
        r += route[(k + p) % len(routes)]
    rout += [r]
rou = routes.index(routes[rout.index(min(rout))]) #im crazy
ro = routes[int(rou):] + routes[:rou] #we begining in the alphabett where the 15 next case have the less probability
for i in ro:
    cases =  alphaDic[i]
    for case in cases:
        if A[case[0]][case[1]] == 0:
            rout1 += [case[0]*9 + case[1]]
lautcher(A)