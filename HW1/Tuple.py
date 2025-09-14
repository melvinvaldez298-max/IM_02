nestedTuple = ()
row = int(input("Enter row: "))
col = int(input("Enter column: "))

temp_list = []  # temporary list to hold rows

for x in range(row):
    print(f"Row{x+1}: ")
    innerList = []
    for y in range(col):
        print(f"Enter score{y+1}: ", end=" ")
        score = float(input())
        innerList.append(score)
    temp_list.append(tuple(innerList))  

nestedTuple = tuple(temp_list)  

print("The numbers are: ")
for r in nestedTuple:
    for c in r:
        print(f"{c:8}", end=" ")
    print()

search_val = float(input("Search: "))
found = False

for i, r in enumerate(nestedTuple):      
    for j, c in enumerate(r):            
        if c == search_val:
            print(f"Number {search_val} found at Row {i}, Column {j}")
            found = True

if not found:
    print("Value not found")
