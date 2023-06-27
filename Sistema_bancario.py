from colorama import Fore, Style

estilo_1 = Fore.RED
estilo_2 = Fore.LIGHTGREEN_EX
estilo_3 = Fore.BLACK
parar_estilo = Style.RESET_ALL

menu = f'''
{estilo_3}==========={parar_estilo}{estilo_1}MENU{parar_estilo}{estilo_3}==========={parar_estilo}
{estilo_3}[{estilo_1}1{parar_estilo}{estilo_3}]{parar_estilo} {estilo_2}Depósito{parar_estilo}
{estilo_3}[{estilo_1}2{parar_estilo}{estilo_3}]{parar_estilo} {estilo_2}Saque{parar_estilo}
{estilo_3}[{estilo_1}3{parar_estilo}{estilo_3}]{parar_estilo} {estilo_2}Extrato{parar_estilo}
{estilo_3}[{estilo_1}4{parar_estilo}{estilo_3}]{parar_estilo} {estilo_2}Sair{parar_estilo}
{estilo_3}=========================={parar_estilo}
'''
print(menu)
saldo = 1250
while True:
    saldo = saldo
    limite_saque = 500
    opcao = int(input())
    if opcao == 1:
        deposito = float(input('Informe o valor do depósito.\n'))
        saldo += deposito
        print(f'Seu saldo atual é R${saldo:.2f}')
    elif opcao == 2:
        saque = float(input('Informe o valor do saque.\n'))
        saldo -= saque
        if saque <= limite_saque:
            print(f'Saque efetuado com sucesso!\nSeu saldo atual é R${saldo:.2f}')
        else:
            print(f'O valor excede o limite de saque diário de R${limite_saque:.2f}')
    elif opcao == 3:
        print(f'Seu saldo atual é de R${saldo:.2f}')
    else:
        print('Menu encerrado')
        break
    print(menu)
