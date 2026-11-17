print("Bem-vindo a Pizzaria")
print("-" * 25 + "Cardápio" + "-" * 25 + "\n" + "-" * 58)

print("--- | Tamanho | Pizza Salgada (PS) | Pizza Doce (PD) | ---")
print("--- |    P    |      R$ 30,00      |     R$ 34,00    | ---")
print("--- |    M    |      R$ 45,00      |     R$ 48,00    | ---")
print("--- |    G    |      R$ 60,00      |     R$ 66,00    | ---")
print("-" * 58)

total_pedido = 0  # Acumulador para somar os valores dos pedidos

while True:  # Chama um loop infinito, até que seja interrompido pelo break.
    # Exibe os sabores e verifica se escolheu a opção disponível.
    sabor = input("\nEntre com o sabor desejado(PS/PD): ").upper()

    if sabor != "PS" and sabor != "PD":  # sabor diferente de PS e PD retorna sabor inválido.
        print("Sabor inválido. Tente novamente")
        continue

    tamanho = input("Selecione o tamanho desejado (P/M/G): ").upper()

    if tamanho not in [
        "P",
        "M",
        "G",
    ]:  # Se o tamanho não for uma das opções, então imprima "Tamanho inválido".
        print("Tamanho inválido. Tente novamente")
        continue  # usado para parar a iteração ou pular etapa

    # --- Lógica de Preços para Pizza Salgada (PS) ---
    if sabor == "PS":
        if tamanho == "P":
            valor = 30
            print("Você pediu uma Pizza Salgada Tamanho P: R$ 30,00")
        elif tamanho == "M":
            valor = 45
            print("Você pediu uma Pizza Salgada Tamanho M: R$ 45,00")
        elif tamanho == "G":
            valor = 60
            print("Você pediu uma Pizza Salgada Tamanho G: R$ 60,00")

    # --- Lógica de Preços para Pizza Doce (PD) ---
    elif sabor == "PD":
        if tamanho == "P":
            valor = 34
            print("Você pediu uma Pizza Doce Tamanho P: R$ 34,00")
        elif tamanho == "M":
            valor = 48
            print("Você pediu uma Pizza Doce Tamanho M: R$ 48,00")
        elif tamanho == "G":
            valor = 66
            print("Você pediu uma Pizza Doce Tamanho G: R$ 66,00")

    total_pedido += (
        valor  # itera os pedidos e soma os valores que serão exibidos na sequência.
    )
    pedir_mais = input("\nDeseja Pedir mais alguma coisa? (S/N): ").upper()

    if pedir_mais == "S":
        continue
    else:
        print(f"\nO valor total a pagar é: R${total_pedido:.2f}")
        break  # encerra o programa
