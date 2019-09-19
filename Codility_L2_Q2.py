def solution(A, K):
    #print(len(A))
    if len(A) <= 0:
        return A
    for j in range(K):
        temp = A[len(A)-1]
        for i in range(len(A)-1,-1,-1):
            A[i] = A[i-1]
        A[0] = temp
    return A




A = [3, 8, 9, 7, 6]
#A = []
K = 3
#K = 0
print(solution(A,K))