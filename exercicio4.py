class palavra:




   entrada = input("Digite algo:")

   print(f'o tipo primitivo deste valor é {type(entrada)}')


    #saber se o texto possui apenas espacos

   if str.isspace(entrada):
       print(f'Possui apenas espacos? Sim')
   else:
       print(f'Possui apenas espacos? Nao')

   #saber se o texto e numerico
   if entrada.isnumeric():
       print('É um numero? Sim')
   else:
       print('É um numero? Nao')

   #saber se o texto e alfabetico
   if entrada.isalpha():
       print('É alfabético? Sim')
   else:
       print('É alfabético? Nao')

   #saber se o texto é alfanumérico
   if entrada.isalnum():
       print('É alfanumérico? Sim')
   else:
       print('É alfanumérico? Nao')

   #saber se o texto esta maiusculo
   if entrada.isupper():
       print('Esta todo em maiusculo? Sim')
   else:
       print('Esta todo em maiusculo? Nao')

   # saber se o texto esta minusculo
   if entrada.islower():
       print('Esta todo em minusculo ? Sim')
   else:
       print('Esta todo em minusculo ? Nao')

   # saber se o texto esta capitalizado
   if entrada[0].isupper():
       print('Esta capitalizado? Sim')
   else:
       print('Esta capitalizado? Nao')