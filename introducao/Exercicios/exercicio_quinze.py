# Lista de exercicio

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
    # salário bruto.
    # quanto pagou ao INSS.
    # quanto pagou ao sindicato.
    # o salário líquido.
    # calcule os descontos e o salário líquido, conforme a tabela abaixo:
    # + Salário Bruto : R$
    # - IR (11%) : R$
    # - INSS (8%) : R$
    # - Sindicato ( 5%) : R$
    # = Salário Liquido : R$
    # Obs.: Salário Bruto - Descontos = Salário Líquido.

# Solicita ao usuário informar o salário por hora
salario_hora = float(input("Digite seu salário por hora: "))

# Solicita ao usuário informar a quantidade de horas trabalhadas no mês
horas_trabalhadas = float(input("Digite suas horas trabalhadas no mês: "))

# Calcula o salário bruto do usuário
salario_bruto = salario_hora * horas_trabalhadas

# Define as porcentagens de desconto
percentual_ir = 11  # 11%
percentual_inss = 8  # 8%
percentual_sindicato = 5  # 5%

# Calcula os descontos diretamente em porcentagem
ir = (salario_bruto * percentual_ir) / 100
inss = (salario_bruto * percentual_inss) / 100
sindicato = (salario_bruto * percentual_sindicato) / 100

# Calcula o total de descontos
desconto = ir + inss + sindicato

# Calcula o salário líquido
salario_liquido = salario_bruto - desconto 

# Exibe os resultados para o usuário

# Exibe o valor do salário bruto
print(f"Salário Bruto : R${salario_bruto:.2f}")

# Exibe o valor do desconto do IR
print(f"IR ({percentual_ir}%) : R${ir:.2f}")

# Exibe o valor do desconto do INSS
print(f"INSS ({percentual_inss}%) : R${inss:.2f}")

# Exibe o valor do desconto do sindicato
print(f"Sindicato ({percentual_sindicato}%) : R${sindicato:.2f}")

# Exibe o valor do salário líquido 
print(f"Salário Líquido : R${salario_liquido:.2f}")
