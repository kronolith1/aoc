with open('input.txt') as input_file:
    input_array = input_file.readlines()

for x in input_array:
    x = int(x)
    for y in input_array:
        y = int(y)
        if x + y == 2020:
            print(f"X is: {x}")
            print(f"Y is: {y}")
            print(f"Z is: {z}")
            print(f"Answer is: {x * y * z}")

