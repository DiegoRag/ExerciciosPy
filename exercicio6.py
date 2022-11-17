import math


class Operacoes:
   dado = int(input("Digite um numero:"))

   print(f'O dobro de {dado} é {2 * dado}')

   print(f'O triplo de {dado} é {3 * dado}')


   #nao usei f string porque eu queria colocar o {:.2f} no codigo para tirar aquela quantidade desnecessaria de numeros.
   print('A raiz quadrada de {} é {:.2f}.'.format(dado, math.sqrt(dado)))

   print(f'A potencia de {dado} é {dado * dado}')