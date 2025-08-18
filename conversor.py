import math
#Esse código tem intuito de poder escolher qualquer tipo de número, independentemente da sua base e transformar em um número de qualquer outra base à preferência do usuário
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
            #Esse try tem função de realizar a operação e, caso haja erro, há o salto direto para a seção do except, onde realizamos o retorno para o começo. Caso a operação seja realizada com sucesso, será realizado o break para sair do loop
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
            resultado = hex(valor_decimal)[2:] #Usamos o "[2:]" pois nas operações de hex, oct e bin, são gerados dois caracteres antes do resultado, dessa forma, podemos pulá-los e exibir unicamente aquilo que nos importa
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

# Execução principal serve para processarmos os dados para que o sistema consiga realizar sua impressão na tela.
valor_decimal, numero, base = escrita()
resultado, desejo = saida(valor_decimal)
print(f"Seu número ({numero}) de base {base} foi convertido para um número de base {desejo} e é equivalente a {resultado}")

