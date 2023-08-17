def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)

alunos_notas = {}

while True:
    nome = input("Digite o nome do aluno (ou deixe vazio para encerrar): ")
    
    if nome == "":
        break
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    alunos_notas[nome] = [nota1, nota2]

nome_busca = input("\nDigite o nome do aluno para calcular a média: ")

if nome_busca in alunos_notas:
    media = calcular_media(alunos_notas[nome_busca])
    print(f'A média de {nome_busca} é: {media:.2f}')
else:
    print(f'Aluno {nome_busca} não encontrado.')
