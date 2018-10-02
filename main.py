A = [2,3,5,6,7]
X = 7

def getIndices(A,X):
    arry = []
    for i in range(0,len(A)):
        remainder = X - A[i]
        if (((remainder-1)>0) and (remainder in arry)):
            return i, A.index(remainder)
        arry.append(A[i])
    return "ERROR: Indices not found!"

print(getIndices(A,X))
