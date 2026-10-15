with open('Coffe_sales.csv') as coffe:
    data = next(coffe)
    print(data)

    a = [1, 2, 3]
    iter_a = iter(a)
    print(next(iter_a))