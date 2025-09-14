nestedDict = {}
row = int(input("Enter row: "))
col = int(input("Enter column: "))

for x in range(row):
    print(f"Row{x+1}: ")
    innerDict = {}
    for y in range(col):
        print(f"Enter score{y+1}: ", end=" ")
        score = float(input())
        innerDict[y] = score   
    nestedDict[x] = innerDict  

print("The numbers are: ")
for i, r in nestedDict.items():
    for j, c in r.items():
        print(f"{c:8}", end=" ")
    print()

search_val = float(input("Search: "))
found = False

for i, r in nestedDict.items():         
    for j, c in r.items():              
        if c == search_val:
            print(f"Number {search_val} found at Row {i}, Column {j}")
            found = True

if not found:
    print("Value not found")


