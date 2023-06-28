def search(file_path):
    with open(file_path, 'r', encoding='utf8') as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if seach_param in line:
                print(line)
