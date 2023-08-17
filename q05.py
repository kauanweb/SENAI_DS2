def fazer_backup(dicionario_principal, dicionario_backup):
    for chave, valor in dicionario_principal.items():
        dicionario_backup[chave] = valor
    dicionario_principal.clear()

dicionario_principal = {}
dicionario_backup = {}
contador = 1

while True:
    chave = input("Digite uma chave (ou 'sair' para encerrar): ")
    
    if chave.lower() == 'sair':
        break
    
    valor = input("Digite um valor: ")
    
    dicionario_principal[chave] = valor
    
    if len(dicionario_principal) == 5:
        print(f"\nRealizando backup {contador}...")
        fazer_backup(dicionario_principal, dicionario_backup)
        contador += 1

print("\nDados no dicionário de backup:")
for chave, valor in dicionario_backup.items():
    print(f'{chave}: {valor}')
