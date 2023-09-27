numbers = input().split()
maior = int()

for n in numbers:
    n = int(n)
    if n > maior:
        maior = n

print(maior, 'eh o maior')
