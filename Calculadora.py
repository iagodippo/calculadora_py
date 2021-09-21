x = "1"
sinal1 = "+"
sinal2 = "-"
sinal3 = "*"
sinal4 = "/"

while x == "1":
    numero1 = int(input("primeiro número: "))
    numero2 = int(input("segundo número: "))
    sinal = input("sinal da operação: "

    if sinal == sinal1:
        soma = numero1 + numero2
        print(soma)
    elif sinal == sinal2:
        sub = numero1 - numero2
        print(sub)
    elif sinal == sinal3:
        multi = numero1 * numero2
        print(multi)
    elif sinal == sinal4:
        div = numero1 / numero2
        print(div)
    else:
        print("Caractére Inválido")

    x = input("Digite 1 para recomeçar ou qualquer outro número para sair: ")
if x != "1":
    print("Obrigado pela preferência!")