def read(file_path):
    return open(file_path, 'r', encoding='utf8').readlines()

def read_all(file_path):
    with open(file_path, 'r', encoding='utf8') as open_book:
        print()
        for line in open_book:
            print(line)  