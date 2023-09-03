# Lista de exercicios

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.


# Solciita ao usuário o peso dos peixes
peso = float(input("Digite o peso dos peixes: "))

# Define o limite estabelecido pelo regularmento
LIMITE_PESO = 50

# Inicia a validação do peso 
if peso > 50: # Verifica se o peso ultrapassou o limite
    # Calcula o excesso além do limite
    excesso = peso - LIMITE_PESO

    # Calcula o valor da multa
    multa = excesso * 4.0 # R$4.00 o quilo do valor excedente
    
    # Exibe o resultados para o usuário
    print(f"O peso dos peixes informado foi:{peso} quilos")
    print(f"O Excesso de peixes informado foi:{excesso} quilos")
    print(f"O valor da multa é: R$:{multa}")
else:
    print(f"{peso} quilos está dentro do limite permitido. Nenhuma multa é necessária") 

