notas: float
resto: float
troco = float(input("Digite seu troco!"))
i: int
quantidade: int

notas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]
quantidade = [0 for _ in range(11)]

i = 0

while i < 10:

    quantidade[i] = int(troco/notas[i])
    resto = troco%notas[i]

    print('R${} -> {}' .format(notas[i], quantidade[i]))
    troco = resto
    i = i+1

