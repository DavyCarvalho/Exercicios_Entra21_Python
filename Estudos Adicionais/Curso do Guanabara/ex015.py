dias = int(input("Quantos dias rodou com o carro?\n"))
km = float(input("Quantos Km rodou com o carro?\n"))
custo_por_km = 0.15
custo_diaria = 60.0
valor_a_pagar = dias * custo_diaria + km * custo_por_km

print("O total a pagar é R${}".format(valor_a_pagar))