class Media:

    nome_aluno = input("Diga o nome do aluno:")

    Nota1 = float(input('Primeira nota do aluno:'))

    Nota2 = float(input('Segunda nota do aluno:'))

    lista_de_notas = [Nota1, Nota2]

    print(f'A média do {nome_aluno} é {(sum(lista_de_notas) / len(lista_de_notas))}')

    print("Bom dia!")