## Lista de exercicios

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
## C = 5 * ((F-32) / 9). 

celsius = float(input("Digite o valor de graus em Fahrenheit: "))

fahrenheint = (celsius*9/5)+32

print("Convertendo em Celsius o valor é de: ", fahrenheint)