salario = int(input("Qual o valor do salário?\n"))
porcentagem_de_aumento = int(input("Qual a porcentagem de aumento salarial?\n"))

print("Seu salario de R${} vai ter um aumento de {}% e passará a ser de R${}"
      .format(salario, porcentagem_de_aumento, salario+((salario*porcentagem_de_aumento)/100)))