total1 = 0
total2 = 0
qt_dig1 = 10
qt_dig2 = 11
num = '222222222222'
for i in num:
    total1 = total1 + (int(i)*qt_dig1)
    qt_dig1 = qt_dig1 - 1


result1 = 11 - (total1 % 11)
num = num+str(result1)
print(num)

for i in num:
    total2 = total2 + (int(i)*qt_dig2)
    qt_dig2 = qt_dig2 - 1

result2 = 11 - (total2 % 11)

print(f'primeiro digito: {result1}')
print(f'segundo digito: {result2}')

def Cpf_isvalid(cpf):
    if len(cpf) == 11:
       pass

    else:
        return f'Cpf invalido, falta de digitos'