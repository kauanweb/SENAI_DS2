
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
telefone = input("Digite o seu telefone: ")
endereco = input("Digite o seu endereço: ")


d = {
    'nome': nome,
    'idade': idade,
    'telefone': telefone,
    'endereço': endereco
}

for chave, valor in sorted(d.items()):
    print(f'{chave}: {valor}')
