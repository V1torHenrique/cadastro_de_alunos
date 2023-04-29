from time import sleep

lista_alunos = []

while True:
    alunos = str(input('\nDigite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista_alunos.append(alunos)
    lista_alunos.append(media)
    print(f"""
        Aluno: {alunos},
        Média: {media},
""")

    if media <= 5:
        print(f'A nota {media} ficou abaixo da média, estude mais!')
    elif media <= 7:
        print(f'A nota {media} foi muito boa, estude mais.')
    else:
        print(f'A nota {media} foi maravilhosa, continue assim.')
        
    ver_lista = str(input('\nDeseja ver a lista <s/n>? '))[0].upper().strip()[0]
    while ver_lista not in 'SN':
        print('\n[ERROR] Digite uma resposta válida.')
        ver_lista = str(input('\nDeseja ver a lista <s/n>? '))[0].upper().strip()[0]
    if ver_lista == 'S':
        print('--- Lista ---')
        for i, v in enumerate(lista_alunos):
            print(f'{i} -> {v}')
        print()
    else:
        pass
    
    continuar = str(input('\nQuer continuar <s/n>? '))[0].upper().strip()[0]
    while continuar not in 'SN':
        print('Digite uma resposta válida.')
        continuar = str(input('\nQuer continuar <s/n>? '))[0].upper().strip()[0]
    if continuar != 'S' and continuar != 's':
        break
    
print('\nEncerrando..')
sleep(3)
print('\nObrigado por utilizar esse sistema, volte sempre! :)')