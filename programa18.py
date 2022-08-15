import math
angulo = int(input('Digite um angilo: '))
s = math.sin(math.radians(angulo))
print('O angulo de {}graus tem o SENO em {:.2f}'.format(angulo, s))
c = math.cos(math.radians(angulo))
print('O angulo de {}graus tem o COS em {:.2f}'.format(angulo, c))
t = math.tan(math.radians(angulo))
print('O angulo de {}graus tem o TANG em {:.2f}'.format(angulo, t))
