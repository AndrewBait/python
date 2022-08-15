import math
print('-' * 20)
print('Calculo hipotenusa')
print('-' * 20)

co = float(input('cateto oposto: '))
ca = float(input('catetoadjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.3f}' .format(hi))
