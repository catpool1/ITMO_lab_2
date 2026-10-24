from xml.dom import minidom


charcodes = []
values = []



with open('currency.xml') as f:
    data = minidom.parse(f)

valutes = data.getElementsByTagName("Valute")

for valute in valutes:
    value = valute.getElementsByTagName("Value")[0]
    values.append(value.firstChild.data)

    charcode = valute.getElementsByTagName("CharCode")[0]
    charcodes.append(charcode.firstChild.data)


print(charcodes)
print(values)