def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")
    return {'nome': nome, 'idade': idade, 'cpf': cpf}


todas_pessoas = {}
menores_18 = {}

while True:
    pessoa = cadastrar_pessoa()
    todas_pessoas[pessoa['cpf']] = pessoa
    continuar = input("Deseja cadastrar mais uma pessoa? (s/n): ")
    if continuar.lower() != 's':
       break 

for cpf, pessoa in todas_pessoas.items():
    if pessoa['idade'] < 18:
        menores_18[cpf] = pessoa
        del todas_pessoas[cpf]


print("\nTodas as pessoas:")
for cpf, pessoa in todas_pessoas.items():
    print(f'CPF: {cpf} - Nome: {pessoa["nome"]} - Idade: {pessoa["idade"]}')

print("\nMenores de 18 anos:")
for cpf, pessoa in menores_18.items():
    print(f'CPF: {cpf} - Nome: {pessoa["nome"]} - Idade: {pessoa["idade"]}')
