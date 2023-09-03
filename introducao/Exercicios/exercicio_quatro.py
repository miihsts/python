## Lista de exercicios

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 = input("Digite a primeira nota bimestral:  ")
nota_2 = input("Digite a segunda nota bimestral:  ")
nota_3 = input("Digite a terceira nota bimestral:  ")
nota_4 = input("Digite a quarta nota bimestral:  ")

media = (float(nota_1) + float(nota_2) + float(nota_3) + float(nota_4)) / 4

print("A média é: ",media)