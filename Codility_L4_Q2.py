def solution(X, A):
    L = [-1] * X
    print(A)
    uncovered = X
    print(L)
    for i in range(0,len(A)):
        print(A[i]-1)
        if L[A[i]-1] == -1:
            L[A[i] - 1] = i
            uncovered -= 1
            if uncovered == 0:
                return i

    return -1

def solutionz(X, A):
    #print(A)
    covered_time = [-1] * X  # Record the time, each position is covered
    #print(covered_time)
    uncovered = X  # Record the number of uncovered position
    for index in range(0, len(A)):
        #print(index)

        if covered_time[A[index] - 1] != -1:
            # This position is already covered
            continue
        else:
            # This position is to be covered
            covered_time[A[index] - 1] = index
            #print(covered_time)
            uncovered -= 1
            if uncovered == 0:
                # All positions are covered
                return index
    # Finally, some positions are not covered
    return -1

def solutions(X, A):
    """
    :param X: an integer. the frogs destination
    :param A: non-empty list of integers
    :return: an integer - the earliest time, or -1
    """
    # count unique leaf positions and stop when there are enough
    leaves = {}
    print(leaves)
    for second in range(0, len(A)):
        leaves[A[second]] = True
        print(leaves)
        if len(leaves) == X:
            return second
    return -1

X = 5
A = [1, 3, 1, 5, 2, 3, 4, 4]
print(solution(X, A))
print("\n\n")
print(solutionz(X, A))
print(solutions(X, A))

