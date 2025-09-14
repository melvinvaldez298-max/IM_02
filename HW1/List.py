nestedList = []
row = int(input("Enter row: "))
col = int(input("Enter column: "))

for x in range(row):
    print(f"Row{x+1}: ")
    innerList=[]
    for y in range(col):
        print(f"Enter score{y+1}: ", end = " ")
        score=float(input())
        innerList.append(score)
    nestedList.append(innerList)
print("The numbers are: ")

for r in nestedList:
    for c in r:
        print(f"{c:8}", end=" ")
    print()


search_val = float(input("Search: "))
found = False

for i, r in enumerate(nestedList):       # i = row index
    for j, c in enumerate(r):            # j = column index
        if c == search_val:
            print(f"Number {search_val} found at Row {i}, Column {j}")
            found = True

if not found:
    print("Value not found")