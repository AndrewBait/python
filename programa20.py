import random

print('-' * 20)
print('ESCOLHA ALEATORIA APRESENTAÇÃO DE ALUNOS')
print('-' * 20)
a1 = input('Primneiro aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem da apresentação sera')
print (lista)
