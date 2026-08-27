print('Bem vindo ao Sistema de desconto Saúde')

ValorBase = float(input('Informe o valor base do plano: R$ '))
idade = int(input('Informe a idade do cliente: '))

if idade>= 0 and idade <19: 
    desconto = (100/100)
elif idade>= 19 and idade <29:
    desconto = (150/150)
elif idade>= 29 and idade <39: 
    desconto = (225/100)
elif idade>= 39 and idade <49:
    desconto = (240/100)
elif idade >= 49 and idade <59:
    desconto = (350/100)
else:
    desconto = (600/100) 

ValorMensal = ValorBase * desconto

print(f'O valor mensal do plano é de: R$ {ValorMensal:.2f}')