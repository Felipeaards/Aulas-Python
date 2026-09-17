dia = input("Digite o dia da semana: ").lower() #Transforma o texto em minúsculo

match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia de semana")
    case "domingo" | "sabado":
        print("Fim de semana")
    case _:
        print("Dia inválido")