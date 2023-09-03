# Lista de exercicios

# - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # 1. Para homens: (72.7*h) - 58
    # 2. Para mulheres: (62.1*h) - 44.7
opcao = -1

# Entrando na estrutura de repetição while
while opcao !=0:

    # Solicitando a altura para o usuário
    altura = float(input("Digite a altura desejada para o cálculo: "))

    # Solicitando o sexo para usuário
    opcao = int(input("[1] Mulher \n [2] Homem \n [0] Sair \n "))

    # Validando qual o sexo do usuário   
    if opcao == 1: # Se a resposta for 1 mulher irá realizar este bloco de código
            # Realizando o cálculo do peso
            peso = (62.1*altura) - 44.7
            # Exibindo o peso ideal para usuário
            print("Escolhido Mulher sendo assim o peso ideal de acordo com a altura é: ", peso)

    elif opcao == 2: # Se a resposta for 2 homem irá realizar este bloco de código
            # Realizando o cálculo do peso
            peso = (72.7*altura) - 58

            # Exibindo o peso ideal para usuário

            print("Escolhido Homem sendo assim o peso ideal de acordo com a altura é: ", peso)
    else: # Se a resposta for 0 realiza o seguinte código
            # Exibindo mensagem que usuário resolver sair do programa - saída do laço de repetição
            print("Você escolheu sair")
