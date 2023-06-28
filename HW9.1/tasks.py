from menu import print_menu
from addition import addition
from search import search
from delete import delete
from edit import edit
from read import read_all, read

def tasks(task):
   if task > 6: print('Вы ошиблись')
   if task == 6: print('До свидания!')
   else:
    match task:
        case 1: # вывести все контакты
            read_all(file_path)
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))   
        case 2: # поиск контактов
            search(file_path)
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 3: # добавить контакт
            addition(file_path)
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 4: # изменить контакт
            edit(read(file_path, l))
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 5: # удалить контакт
            delete(read(file_path, l))
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))     
file_path = 'phone_book.txt'