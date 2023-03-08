# Basic Recursive solution from back
def basicLCSfromBack(A, B):
    if len(A) == 0 or len(B) == 0:
        return 0
    else:
        # len - 1이 string의 마지막 문자이다.
        if A[len(A)-1] == B[len(B)-1]:
            return basicLCSfromBack(A[:len(A)-2], B[:len(B)-2])+1
        else:
            return max(basicLCSfromBack(A[:len(A)-1], B), basicLCSfromBack(A, B[:len(B)-1]))

# Basic Recursive solution from front


def basicLCSfromFront(A, B):
    if len(A) == 0 or len(B) == 0:
        return 0
    else:
        if A[0] == B[0]:
            return basicLCSfromFront(A[1:], B[1:])+1
        else:
            return max(basicLCSfromFront(A[1:], B), basicLCSfromFront(A, B[1:]))


# Memoization (while loop or recursion)
# API
# Input: two words, A and B
# Output: size of the least common sequence string
def memoLCSfromBack(A, B):
    Solution = [[-1]*len(B) for i in range(len(A))]
    return meoLCSfromBackHelper(Solution, A, B)

# API
