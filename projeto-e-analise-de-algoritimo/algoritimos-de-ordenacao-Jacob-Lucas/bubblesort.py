import time
import decimal

def bubblesort(A):
    for i in range(0, len(A)):
        trocou = False
        for j in range(0, len(A)-i-1):
            if(A[j] > A[j+1]):
                troca(A, j, j+1)
                trocou = True
        if not trocou:
            break
        
def createRandomList(numMax, tamList):
    import random
    return [random.randint(0, numMax) for i in range(0, tamList)]

def troca(A, i1, i2): 
    A[i1], A[i2] = A[i2], A[i1] 

test = []
for i in range(100000, 0, -1):
    test.append(i)
start = time.time()
bubblesort(test)
end = time.time()
print(end - start)