import time
import decimal

def mergesort(A, p, u):
    if p < u:
        q = (p + u) // 2
        mergesort(A, p, q)
        mergesort(A, q + 1, u)
        merge(A, p, q, u)

def merge(A, p, q, u):
    n1 = q - p + 1
    n2 = u - q
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[p + i])
    for j in range(0, n2):
        R.append(A[q + j + 1])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range(p, u+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            
def createRandomList(numMax, tamList):
    import random
    return [random.randint(0, numMax) for i in range(0, tamList)]

# test the time algorithm with a growing ordered list

def testTime(numMax, tamList):
    testList = createRandomList(numMax, tamList)
    start = time.time()
    mergesort(testList, 0, len(testList)-1)
    end = time.time()
    return end - start

test = []
for i in range(200000, 0, -1):
    test.append(i)
start = time.time()
mergesort(test, 0, len(test)-1)
end = time.time()
print(end - start)