number = list(input('Enter a number: '))

product = 1

for num in number:
    product *= int(num)

print(product)

print(str(product)[::-1])

print(''.join(sorted(number)))

sorted_numbers = ''

for num in sorted(number):
    sorted_numbers += num

print(sorted_numbers)