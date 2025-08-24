import calendar

def bissexto(ano):
    if calendar.isleap(ano):
        print(f"Sim! o ano de {ano} é bissexto")
    else:
        print(f"Não, o ano de {ano} não é bissexto.")

def calendario(ano, mês):
    print(f"{calendar.month(ano, mês)}")

def escolha (ano, mês): 
    while True:
        escolha = input("""O que deseja ver em relação ano e/ou mês escolhido?"
                    
                    1 : Exibição do Calendário 
                    2 : Saber se o ano é Bissexto
                    
                    R:  """)

        if escolha not in ["1", "2"]:
            print("Esse valor é inválido, digite outro.")
            continue
        elif escolha == "1":
            calendario(ano, mês)
        elif escolha == "2":
            bissexto(ano)
            
        
ano = int(input("Digite o ano que deseja ver no calendário: "))
mês = int(input("Digite o mês que deseja ver no calendário (1-12): "))
escolha(ano, mês)

            

    



