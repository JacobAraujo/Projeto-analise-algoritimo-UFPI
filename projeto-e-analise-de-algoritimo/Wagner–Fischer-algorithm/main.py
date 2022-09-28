def main():
    word1 = 'esrdtfy'
    word2 = 'aewsrfyokj'
    table = []
    
    for i in range(len(word1)+1):
        table.append([])
    
    for i in range(len(word1)+1):
        for j in range(len(word2)+1):
            table[i].append([0,'u'])
    
    for i in range(0, len(word2)+1):
        table[len(word1)][len(word2)-i] = [i,'direita']
    
    for i in range(0, len(word1)+1):
        table[len(word1)-i][len(word2)] = [i,'baixo']

    for i in range(len(word1)+1): # print table
        print('\n', end='')
        for j in range(len(word2)+1):
            print(table[i][j][0], end='  ')
    
    for j in range(len(word2)-1, -1, -1):
        for i in range(len(word1)-1, -1, -1):
            if table[i+1][j][0] == table[i+1][j+1][0] and table[i+1][j][0] == table[i][j+1][0]:
              menor = [table[i+1][j][0] + 1, 'baixo']
            elif table[i+1][j+1][0] <= table[i+1][j][0] and table[i+1][j+1][0] <= table[i][j+1][0]:
              if word1[i] == word2[j]:
                menor = [table[i+1][j+1][0], 'diagonal']
              else:
                menor = [table[i+1][j+1][0]+1, 'diagonal']
            else:
              menor = [table[i][j+1][0]+1,'direita']
            table[i][j] = menor

        
    print('\n\n', end='')
    for i in range(len(word1)+1): # print table
        print('\n', end='')
        for j in range(len(word2)+1):
            if table[i][j][1] == 'baixo':
                print(table[i][j], end='        ')
            elif table[i][j][1] == 'u':
                print(table[i][j], end='            ')
            elif table[i][j][1] == 'direita':
                print(table[i][j], end='      ')
            else:
                print(table[i][j], end='     ')
    
    print('\nLevenshtein Distance: ', table[0][0][0])
    print('\nThis is the path: ', end='')
    i = 0
    j = 0
    while i < len(word1) or j < len(word2):
        if table[i][j][1] == 'diagonal':
            print('replace - ' if table[i][j][0] != table[i+1][j+1][0] else 'Its equal - ', end='')
            i += 1
            j += 1
        elif table[i][j][1] == 'baixo':
            print('delete - ' if table[i][j][0] != table[i+1][j][0] else 'Its equal - ', end='')
            i += 1
        elif table[i][j][1] == 'direita':
            print('insert - ' if table[i][j][0] != table[i][j+1][0] else 'Its equal - ', end='')
            j += 1
        else:
            print('error')
            break
    
main()