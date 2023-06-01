line1 = input().split()
line2 = input().split()

total = (float(line1[2]) * int(line1[1])) + (float(line2[2]) * int(line2[1]))
print(f'VALOR A PAGAR: R$ {total:.2f}')
