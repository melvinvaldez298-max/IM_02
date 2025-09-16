def converter(dollars):
    peso = dollars * 57.17
    yen = dollars * 146.67
    return peso, yen

value = [59, 200, 500]
print("Enter currency in ($):", ", ".join((map(str, value))))
print("\nDollar($)\t\tPh Peso(P)\t\tJpn Yen(Y)")

for d in value:
    peso, yen = converter(d)
    print(str(d) + "\t\t\t" + str(round(peso, 2)) + "\t\t\t" + str(round(yen, 2)))