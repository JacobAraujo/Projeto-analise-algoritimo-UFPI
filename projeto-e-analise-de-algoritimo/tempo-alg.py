import heapsort
import bubblesort
import mergesort
import quicksort

import time

escolha = 1
vetorFixo = heapsort.createRandomList(500, 50000)

while (escolha):

    print('1 - HeapSort')
    print('2 - BubbleSort')
    print('3 - MergeSort')
    print('4 - QuickSort')
    print('0 - Sair')

    escolha = input("Escolha o algoritmo de ordenar: ")

    teste = vetorFixo

    if escolha == '1':
        # pegar o tempo do algoritmo
        start_time = time.time()
        heapsort.heapsort(teste)
        print("--- %s seconds ---" % (time.time() - start_time))
        print('\n')

    if escolha == '2':
        start_time = time.time()
        bubblesort.bubblesort(teste)
        print("--- %s seconds ---" % (time.time() - start_time))
        print('\n')

    if escolha == '3':
        start_time = time.time()
        mergesort.mergesort(teste, 0, len(teste)-1)
        print("--- %s seconds ---" % (time.time() - start_time))
        print('\n')

    if escolha == '4':
        start_time = time.time()
        quicksort.quicksort(teste, 0, len(teste)-1)
        print("--- %s seconds ---" % (time.time() - start_time))
        print('\n')

