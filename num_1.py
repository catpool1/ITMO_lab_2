import csv
import random


def find_name_with_lenght(csv_file, symbols_count):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=';')

    counter = 0

    for line in reader:
        if len(line['Название']) > symbols_count:
            counter += 1

    print(counter)


def search_by_name(csv_file, full=False):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=';')

    name = list(input('Введите ФИО: ').split())

    books = []

    for line in reader:
        for part in name:
            if part not in line['Автор (ФИО)']:
                break
        else:
            if full:
                books.append(line.values())
            else:
                books.append([line['Автор (ФИО)'], line['Название']])

    for book in books:
        print(*book, sep=' | ')


def generate_library_links(csv_file, count):
    csv_file.seek(0)
    csv_file.readline()
    file_lines_count = len(csv_file.readlines())
    lines = random.sample(range(file_lines_count+1), count)

    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=';')

    books = []

    for i, line in enumerate(reader):
        if i in lines:
            author = line['Автор (ФИО)']
            book_name = line['Название']
            year = line['Дата поступления'].split('.')[2][:4]

            books.append(f"{author}. {book_name} - {year}")


    with open('links.txt', 'w') as links:
        for i, line in enumerate(books, start=1):
            links.write(f"{i}. {line}\n")



with open('books.csv') as books_csv:
    # find_name_with_lenght(books_csv, 30)
    # search_by_name(books_csv)
    generate_library_links(books_csv, 20)