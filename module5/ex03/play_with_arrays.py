array = [1,3,4,56,4,9,90]

new_array = []
for value in array:
    new_array.append(value+2)

print (array)

bigger_numbers = []

for x in new_array: 
    if x > 5:
        bigger_numbers.append(x)

# 

set1 = set(bigger_numbers)
print(set1)