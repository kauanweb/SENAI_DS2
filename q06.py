def contar_vogais(texto):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in texto:
        if letra.lower() in vogais:
            vogais[letra.lower()] += 1
    
    return vogais

texto = input("Digite um texto: ")
resultado = contar_vogais(texto)

print("\nQuantidade de vogais:")
for vogal, quantidade in resultado.items():
    print(f'{vogal}: {quantidade}')
