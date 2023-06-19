def search_rytm(list_input):
    list_stixi = list_input.copy()
    list_stixi = list(map(lambda word: list(filter(lambda letter: letter in glasnie, word)), list_stixi))
    for i in range(1, len(list_stixi)):
        if len(list_stixi[i]) != len(list_stixi[i - 1]):
            return False
        else:
            return True 

glasnie = ('у', 'е', 'ё', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю')
stix = input('Введите стихотвроение Винни Пуха: ')
stix = stix.lower()
stix_list = list(stix.split())
if search_rytm(stix_list) == True:
    print('Парам пам-пам (с ритмом все впорядке)')
else:
    print('Пам парам (ритма нет)')