def solution(A):
    if len(A)>0:
        A = sorted(A)
        #print(A)
        for i in range(1,len(A)+1):
            #print("i=",i)
            if i != A[i-1]:
                #print(i,A[i],"U")
                return i
        return(i+1)
    else:
        #print("N")
        return 1

#N = 5
#A = [1]
A = [5,2,3,4,1,6]
print(solution(A))