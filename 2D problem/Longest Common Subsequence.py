# Recursive solution from back
def basicLCS(A, B):
    if len(A) == 0 or len(B) == 0:
        return 0
    else:
        if A[len(A)-1] == B[len(B)-1]:
            return basicLCS(A[:len(A)-2], B[:len(B)-2])+1
        else:
            return max(basicLCS(A[:len(A)-1], B), basicLCS(A, B[:len(B)-1]))


print(basicLCS("Apple", "pie"))
