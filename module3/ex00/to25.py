number = int(input("Enter a number less than 25: \n"))

if number > 25:
    print ("Error")
while number <= 25:
    print(f"Inside the loop, my variable is {number}")
    number += 1
    if number > 25:
        break
