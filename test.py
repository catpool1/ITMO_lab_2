import csv
import statistics

def slice_file(csv_file, start, end):
    csv_file.seek(0)

    next(csv_file)

    data = []
    for i, line in enumerate(csv_file):
        if i >= start:
            data.append(line.split(','))
        if i >= end:
            break

    return data


def find_popular(csv_file):
    csv_file.seek(0)

    reader = csv.DictReader(csv_file, delimiter=',')
    # print(next(reader))


    drinks = {}

    for data in reader:
        drink = data['coffee_name']
        if drinks.get(drink) is None:
            drinks[drink] = 0
        drinks[drink] += 1

    return max(drinks, key=lambda drink_key: drinks[drink_key])

def find_popular2(csv_file):
    csv_file.seek(0)

    reader = csv.DictReader(csv_file, delimiter=',')

    drinks = [data["coffee_name"] for data in reader]
    return statistics.mode(drinks)



def compute_month_income(csv_file, month_input):
    csv_file.seek(0)

    reader = csv.DictReader(csv_file, delimiter=',')

    income = 0

    for data in reader:
        money = float(data["money"])
        month = data["Monthsort"]

        if month == month_input:
            income += money
    return income
    


st = 1
en = 2

if __name__ == '__main__':
    with open('Coffe_sales.csv') as coffe_csv:
        # print(*slice_file(coffe_csv, st, en), sep='\n')

        # result = slice_file(coffe_csv, st, en)
        # for line in result:
        #     print(' | '.join(line))

        # print(find_popular(coffe_csv))
        # print(find_popular2(coffe_csv))

        print(compute_month_income(coffe_csv, input()))