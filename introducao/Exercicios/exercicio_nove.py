## Lista de exercicios

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
## C = 5 * ((F-32) / 9). 

fahrenheint = float(input("Digite o valor de graus em Fahrenheit: "))

celsius = (fahrenheint-32)/1.8

print("Convertendo em Celsius o valor é de: ", celsius)