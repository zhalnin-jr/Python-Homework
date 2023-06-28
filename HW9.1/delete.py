def delete(file_path, l):
    delete_param = (input('Введите контакт удаления: ' ).title())
    with open (file_path, 'w', encoding='utf8') as open_book:
        for line in l:
            if delete_param in line:
                print('Вы удалили контакт:', line)
            elif delete_param not in line:
               open_book.writelines(line)