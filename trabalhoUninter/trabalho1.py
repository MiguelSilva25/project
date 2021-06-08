# Entrada de dados do lutador! Ex: Jose aldo e o seu pesso
nomeDoLutador = input('Informe o nome do Lutador: ') # O nome que será exibido do lutador é string ou entrada de dados
pesoDoLutador = float(input('Informe o peso do Lutador: ')) #O float serve para para qualquer número que tiver em casas decimais

# Programa Principal
# Aqui será apresentada onde o lutado se enquadra nas categorias de seu peso para luta!
if pesoDoLutador <= 55:
    print('O lutador',nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria mosca')
elif pesoDoLutador >= 55 and pesoDoLutador < 65:
    print('O lutador',nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria pena')
elif pesoDoLutador >= 65 and pesoDoLutador < 72:
    print('O lutador',nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria leve')
elif pesoDoLutador >= 72 and pesoDoLutador < 79:
    print('O lutador',nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria Ligeiro')
elif pesoDoLutador >= 79 and pesoDoLutador < 86:
    print('O lutador',nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria Meio-médio')
elif pesoDoLutador >= 86 and pesoDoLutador < 93:
    print('O lutador' ,nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria Médio')
elif pesoDoLutador >= 93 and pesoDoLutador < 100:
    print('O lutador' ,nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria Meio-pesado')
elif pesoDoLutador >= 100:
    print('O lutador' ,nomeDoLutador,'pesa',pesoDoLutador,'kg e se enquadra na categoria Pesado')




