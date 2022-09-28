import heapsort
import bubblesort
import mergesort
import quicksort

escolha = 1
vetorFixo = heapsort.createRandomList(10000, 100) # Cria um vetor de 500 elementos aletórios(min 0 e max 500)
print(vetorFixo)

teste = vetorFixo

print('1 - HeapSort')
print('2 - BubbleSort')
print('3 - MergeSort')
print('4 - QuickSort')
print('0 - Sair')

escolha = input('\nAlgoritimo escolhido: ')

print('Vetor desordenado: ', vetorFixo)

if escolha == '1':
    heapsort.heapsort(teste)
    print('Vetor ordenado: ', teste)


if escolha == '2':
    bubblesort.bubblesort(teste)
    print('Vetor ordenado: ', teste)

if escolha == '3':
    mergesort.mergesort(teste, 0, len(teste)-1)
    print('Vetor ordenado: ', teste)

if escolha == '4':
    quicksort.quicksort(teste, 0, len(teste)-1)
    print('Vetor ordenado: ', teste)
