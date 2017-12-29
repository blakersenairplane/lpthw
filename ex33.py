i = 0
numbers = []
incremental = 2


def whileLoop(number, increment):
    while number < 6:
        print(f"At the top of the i is {i}")
        numbers.append(number)

        number = number + increment

        print("Numbers now: ", numbers)
        print(f"At the bottom of i is {i}")

# while i < 6:
#     print(f"At the top of i is {i}")
#     numbers.append(i)
#
#
#     i = i + 1
#
#     print("Numbers now:", numbers)
#     print(f"At the bottom of i is {i}")
#

whileLoop(i, incremental)
print("The numbers: ")

for num in numbers:
    print(num)


