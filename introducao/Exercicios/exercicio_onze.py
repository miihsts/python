# Lista de exercicios

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # 1. o produto do dobro do primeiro com metade do segundo .
    # 2. a soma do triplo do primeiro com o terceiro.
    # 3. o terceiro elevado ao cubo.

# Solicita os dois números inteiros e o número real ao usuário
numero_inteiro1 = int(input("Digite um número inteiro: "))
numero_inteiro2 = int(input("Digite um número inteiro: "))
numero_real = float(input("Digite um número real: "))

# Realiza os cálculos
resultado_1 = (numero_inteiro1 * 2) * (numero_inteiro2 /2)
resultado_2 = (numero_inteiro1 * 3) + numero_real
resultado_3 = numero_real**3

# Exibe os resultados
print("1. O produto do dobro do primeiro com metade do segundo é:", resultado_1)
print("2. A soma do triplo do primeiro com o terceiro é:", resultado_2)
print("3. O terceiro elevado ao cubo é:", resultado_3)
