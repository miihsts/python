# Lista de exercicios

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58


# Solicitando a altura para o usuário

altura = float(input("Digite a altura desejada para o cálculo"))

# Realizando o cálculo de peso ideal utilizando a fórmula fornecida no enuciado da questão

peso = (72.7*altura) - 58

# Exibindo o peso ideal para usuário

print("O peso ideal para esta pessoa é: " , peso)