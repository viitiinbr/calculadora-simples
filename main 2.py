from calculadora import soma,sub,multi,divi

# Implementação da calculadora simples
while True:

    print('\n\t\t\t -- Calculadora Simples --\n')




#menu
    print("1. soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. divisão")
    print("5. sair")


    op = int(input("Opção: "))

    if op == 1:
        print("Soma")

        v1 = int(input("Informe o valor 1: "))
        v2 = int(input("Informe o outro numero : "))

        total = soma(v1,v2)

        print(f"A soma é {total}")


    elif op == 2:
        print("Subtração")

        v1 = int(input("Informe o valor1: "))
        v2 = int(input("Informe o outro numero: "))

        total = sub(v1,v2)

        print(f"A sub é: {total}")

    elif op == 3:
        print('Multiplicação')

        v1 = int(input("Informe o valor 1: "))
        v2 = int(input("Informe o outro numero: "))

        total = multi(v1,v2)
        print(f'A multiplicação é: {total}')

    elif op == 4:
        print('Divisão')

        v1 = int(input("Informe o valor 1: "))
        v2 = int(input("Informe o outro numero: "))

        total = divi(v1, v2)
        print(f'A divisão é: {total} ')


    elif op == 5:
        print("Forte abraço!")
        break
    else:
        print("Erro: Esse número de opção não existe")
        #Tratamento de erro