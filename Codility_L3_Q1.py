def solution(X, Y, D):
    # D steps
    # X initial pos
    # Y final pos
    count = 0
    dif = (Y-X)//D
    if (Y-X)%D == 0:
        return dif
    else:
        return dif+1


X = 10
Y = 100
D = 10
print(solution(X, Y, D))