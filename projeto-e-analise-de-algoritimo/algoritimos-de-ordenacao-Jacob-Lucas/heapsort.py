import time
import decimal

def heapsort(A):
    preparaHeap(A)
    tamanhoHeap = tamHeap(A)
    constroiHeapMax(A)
    for i in range(tamanhoHeap, 1, -1):
        troca(A, 1, i)
        tamanhoHeap -= 1
        refazHeapMax(A, 1, tamanhoHeap)
    corrigirHeap(A)


def constroiHeapMax(A):
    for i in range((tamHeap(A))//2, 0, -1):
        refazHeapMax(A, i, tamHeap(A))

def refazHeapMax(A, i, tamanhoHeap):
    e = esquerda(i)
    d = direita(i)
    maior = i
    if(e <= tamanhoHeap and A[e] > A[maior]):
        maior = e
    if(d <= tamanhoHeap and A[d] > A[maior]):
        maior = d
    if(maior != i):
        troca(A, i, maior)
        refazHeapMax(A, maior, tamanhoHeap)

def esquerda(i):
    return i*2 

def direita(i):
    return i*2 + 1

def tamHeap(A):
    return len(A)-1 


def preparaHeap(A):
    A.insert(0, '-')

def corrigirHeap(A):
    del A[0]
    
def troca(A, i1, i2): 
    A[i1], A[i2] = A[i2], A[i1] 
    
def createRandomList(numMax, tamList):
    import random
    return [random.randint(0, numMax) for i in range(0, tamList)]

test = []
for i in range(200000, 0, -1):
    test.append(i)
start = time.time()
heapsort(test)
end = time.time()
print(end - start)