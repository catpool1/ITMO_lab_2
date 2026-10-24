import csv


def get_tags(csv_file):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=';')

    tags = set()

    for line in reader:
        for tag in line['Жанр книги'].split('#'):
            tags.add(tag)

    return tags


def find_popular(csv_file, count):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=';')

    books_count_dict = dict()

    for line in reader:
        book = line['Название']
        if book not in books_count_dict:
            books_count_dict[book] = 0
        
        books_count_dict[book] += int(line['Кол-во выдач'])


    books_rating_dict = dict()

    for book in books_count_dict:
        if books_count_dict[book] not in books_rating_dict:
            books_rating_dict[books_count_dict[book]] = []

        books_rating_dict[books_count_dict[book]].append(book)

    result = []

    while len(result) < count:
        max_count = max(books_rating_dict.keys())
        result.extend(books_rating_dict[max_count][:(count-len(result))])
        books_rating_dict.pop(max_count)

    return result
        


with open('books.csv') as books_csv:
    # print(get_tags(books_csv))
    print(find_popular(books_csv, 20))