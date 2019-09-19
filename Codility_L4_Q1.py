def solution(A):
    A = sorted(A)
    for i in range(0, len(A)):
        if A[i] != i+1:
            return 0
    return 1














A = [1,2,3,4]
B = [1,2,4]
print(solution(A))
print(solution(B))