print('Bem-vindo à Madeireira do Lenhador do Tiago Souza')


def escolha_madeira():
    """Permite ao usuário escolher o tipo de madeira e retorna o preço por m³."""
    precos = {
        'PIN': 150.40,
        'PER': 170.20,
        'MOG': 190.90,
        'IPE': 210.10,
        'IMB': 220.70
    }
    
    while True:
        print(
            'Entre com o tipo de madeira desejado:\n'
            'PIN - Tora de Pinho\n'
            'PER - Tora de Peroba\n'
            'MOG - Tora de Mogno\n'
            'IPE - Tora de Ipê\n'
            'IMB - Tora de Imbuia'
        )
        tipo = input('>> ').strip().upper()
        
        if tipo in precos:
            return precos[tipo]
        print('Escolha inválida, entre com o tipo novamente.\n')


def qtd_tora():
    """Lê e valida a quantidade de toras, calculando o desconto aplicável."""
    while True:
        try:
            qtd = float(input('Entre com a quantidade de toras (m³): '))
            
            if qtd > 2000:
                print('Não aceitamos pedidos com essa quantidade de toras. Por favor, entre com a quantidade novamente...\n')
                continue
            
            if qtd < 100:
                desconto = 0.0
            elif qtd < 500:
                desconto = 0.04
            elif qtd < 1000:
                desconto = 0.09
            else:
                desconto = 0.16
                
            return qtd, desconto
            
        except ValueError:
            print('Por favor, utilize apenas valores numéricos. Entre com a quantidade novamente.\n')


def transporte():
    
    custos_transporte = {
        '1': 1000.00,
        '2': 2000.00,
        '3': 2500.00
    }
    
    while True:
        print(
            'Escolha o tipo de Transporte:\n'
            '1 - Transporte Rodoviário - R$ 1000.00\n'
            '2 - Transporte Ferroviário - R$ 2000.00\n'
            '3 - Transporte Hidroviário - R$ 2500.00'
        )
        opc_transporte = input('>> ').strip()
        
        if opc_transporte in custos_transporte:
            return custos_transporte[opc_transporte]
        print('Opção escolhida inválida. Por favor, selecione uma das opções descritas.\n')


try:
    tora_valor = escolha_madeira()
    qtd, desconto = qtd_tora()
    frete = transporte()
    
    total = (tora_valor * qtd) * (1 - desconto) + frete

    print(f'\nTotal: R$ {total:.2f}')

except Exception as erro:
    print(f'Ocorreu um erro: {erro}')