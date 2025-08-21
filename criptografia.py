cripto = {chr(i): str(i - 96) for i in range(97, 123)}  # letras a-z
cripto[" "] = "-"

frase = input("Digite a palavra ou frase que deseja criptografar: ")
for letra in frase.lower():
    resultado = cripto.get(letra, "?")  # "?" para caracteres não mapeados
    print(resultado)

# {chr(i): str(i - 96) for i in range(97, 123)} cria o mapeamento de 'a' a 'z' para '1' a '26'.
# chr utiliza de código ASCII para exibir um número, onde 97 é a e 122 é z

#Adiciona o espaço " " como "-".

#Usa frase.lower() para garantir que letras maiúsculas também funcionem.
#Usa cripto.get(letra, "?") para evitar erro caso apareça um caractere não mapeado.
