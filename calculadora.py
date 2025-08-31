import sympy

conta = input("""Digite a operação que deseja fazer
        obs:
        Adição = +
        Subtração = -
        Divisão = /
        Multiplicação = x
              
        Sua conta: """)

conta = conta.strip() #aqui retiramos todos os espaços vazios que foram digitados pelo usuário

conta = conta.replace("x", "*")

try:
    resultado = sympify(conta)
    print("O resultado da sua conta é {}" .format(resultado))
except ValueError:
    print("Expressão Inválida!")

#abaixo a versão anterior, baseando-se em manipulação de string e uso de condicionais (if, elif e else)

"""import math

conta = input("""Digite a operação que deseja fazer
        obs:
        Adição = +
        Subtração = -
        Divisão = /
        Multiplicação = x
              
        Sua conta: """)

conta = conta.strip() #aqui retiramos todos os espaços vazios que foram digitados pelo usuário

for i in range(len(conta)):
    if conta[i] in ["+", "-", "/", "x"]:
        operador = conta[i]
        sinal = i
        break #aqui nós atribuímos ao operador o sinal que foi encontrado no input do usuário; já no sinal, encontramos sua posição, para saber aonde exatamente fatiar nossa string



numero1 = int(conta[:sinal])
numero2 = int(conta[sinal+1:]) #aqui fazemos o fatiamento, onde o numero1 irá receber o input até antes da aparição do operador, já o numero2 será equivalente ao que restou após o operador

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "/":
    resultado = numero1 / numero2
elif operador == "x":
    resultado = numero1 * numero2


print(f"O resultado da sua conta ({conta}) é equivalente a {resultado}!")










