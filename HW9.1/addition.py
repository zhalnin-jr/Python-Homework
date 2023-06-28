def addition(file_path):
    with open(file_path, 'a', encoding='utf8') as open_book:
        add_f = (input('Введите фамилию: ' ).title())
        add_i = (input('Введите Имя: ' ).title())
        add_tel = (input('Введите телефон: ' ).title())
        new_line = add_f +' '+add_i +' '+ add_tel 
        open_book.writelines(f'\n{new_line}')
        print(new_line)
