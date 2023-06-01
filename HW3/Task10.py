scores = {1: {'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'},
          2: {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'},
          3: {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'},
          4: {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'},
          5: {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'},
          8: {'J', 'X', 'Ш', 'Э', 'Ю'},
          10: {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}}
slovo = (input('Enter any word: '))
slovo = slovo.upper()
count = 0
a = 0
list_keys = list(scores.keys())
for i in range(len(slovo)):
    for j in scores:
        for b in scores.get(j):
            if b == slovo[i]:
                count = count + list_keys[a]
        a += 1
    a = 0
print('Scrabble sum =', count)