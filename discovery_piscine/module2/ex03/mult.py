first_num = int(input("Give me a number: "))
second_num = int(input("Give me an another number: "))
mult_num = first_num * second_num

if first_num * second_num < 0:
    print(first_num, "x", second_num, "=", (mult_num) )
    print("The result is negative")
elif first_num * second_num > 0:
    print(first_num, "x", second_num, "=", (mult_num) )
    print("The result is positive")
else:
    print("The result is nor positive nor negative")