# Lista de exercicio

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # comprar apenas latas de 18 litros;
    # comprar apenas galões de 3,6 litros;
    # misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# Solicita ao usuário informar o tamanho em metros quadrados a ser pintada

area = float(input("Digite o valor do tamanho em metros quadrados a ser pintada: "))

# Calcule a quantidade de litros necessário

litros = area / 3.0

# Calcule a quantidade de latar necessária

latas = litros / 18

# Calcule o preço total das latas a serem compradas
preco_total = latas * 80.0 

# Exibe para o usuário a área a ser pintada
print(f"Área a ser pintada: {area} metros quadrados")

# Exibe para o usuário a quantidade de litros necessários
print(f"Quantidade de litros necessários: {litros} litros")

# Exibe para o usuário a quantidade de latas de tintas a serem compradas
print(f"A quantidade de latas de tintas a ser compradas é: {int(latas)} latas")

# Exibe para o usuário o preço total a ser gasto
print(f"Preço total: R$ {preco_total}")
