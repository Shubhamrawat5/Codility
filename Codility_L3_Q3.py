def solution(A):
    Down = A[0]
    Up = sum(A[1:])
    #print(Down,Up)
    S= dif = abs(Up - Down)
    #print(dif)
    for i in range(1,len(A)-1):
        #print(A[i])
        Down = Down + A[i]
        Up = Up - A[i]
        #print(Down, Up)
        dif = abs(Up - Down)
        if S > dif:
            S = dif
        #print(S)
    return S

A = [-2, -3, -4, -1]
#A = [3, 1, 2, 4, 3]
#A = [-1000, 1000]
print(solution(A))
#print(abs(-100+100))