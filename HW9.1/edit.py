def edit(file_path, l):
    seach_param = (input('Введите параметр для поиска: ' ).title())
    with open (file_path, 'w', encoding='utf8') as open_book:
        for line in l:
            if seach_param in line:
                print(line)
                add_f = (input('Введите фамилию: ' ).title())
                add_i = (input('Введите Имя: ' ).title())
                add_tel = (input('Введите телефон: ' ).title())
                new_line = add_f +' '+add_i +' '+ add_tel + '\n'
                line = line.replace(line, new_line)
            open_book.writelines(line)