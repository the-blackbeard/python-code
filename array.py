numbers = [10,200,40,50,39]

# print(numbers[1])

# for num in numbers:
#     print(num)

# for i in range(len(numbers)):
#     print(numbers[i])
#
# print(numbers[0:2])

max = numbers[0]
for num in numbers:
    if num > max:
        max = num

print(max)
