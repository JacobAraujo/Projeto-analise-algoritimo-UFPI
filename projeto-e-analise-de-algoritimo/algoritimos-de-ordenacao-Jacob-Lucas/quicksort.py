import random
import time
import decimal

def quicksort(A, p, r):
    if p < r:
        q = randomizedPartition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def randomizedPartition(A, p, r):
    i = random.randint(p, r)
    troca(A, r, i)
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            troca(A, i, j)
    troca(A, i+1, r)
    return i+1

def troca(A, i1, i2): 
    A[i1], A[i2] = A[i2], A[i1] 
    
def createRandomList(numMax, tamList):
    return [random.randint(0, numMax) for i in range(0, tamList)]

test = []
for i in range(200000, 0, -1):
    test.append(i)
start = time.time()
quicksort(test, 0, len(test)-1)
end = time.time()
print(end - start)

