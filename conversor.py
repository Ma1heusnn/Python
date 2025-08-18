import math

def escrita():
    while True:     
        numero = input("Digite o número que deseja transformar: ")
        base = int(input("""Qual é a base númerica desse algarismo?
             Ex: Hexadecimal = 16
             Decimal = 10
             Octal = 8
             Binário = 2
                         
            R: """))
        if base not in [16, 10, 8, 2]:
            print("Digite uma base válida!")
            continue
        try:
            valor_decimal = int(numero, base)
            break
        except ValueError:
            print("Número inválido para a base informada!")
    return valor_decimal, numero, base

def saida(valor_decimal):
    while True:
        desejo = int(input("""Digite para qual base deseja que seu número seja convertido!
             Ex: Hexadecimal = 16
             Decimal = 10
             Octal = 8
             Binário = 2
                           
        R: """))
        if desejo == 16:
            resultado = hex(valor_decimal)[2:]
        elif desejo == 10:
            resultado = int(valor_decimal)
        elif desejo == 8:
            resultado = oct(valor_decimal)[2:]
        elif desejo == 2:
            resultado = bin(valor_decimal)[2:]
        else:
            print("Digite uma base válida!")
            continue
        return resultado, desejo

# Execução principal
valor_decimal, numero, base = escrita()
resultado, desejo = saida(valor_decimal)
print(f"Seu número ({numero}) de base {base} foi convertido para um número de base {desejo} e é equivalente a {resultado}")
