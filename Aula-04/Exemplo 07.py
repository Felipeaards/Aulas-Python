dia = int(input("Digite o dia da semana em formato de número: "))

if dia >= 2 and dia <= 6:
    print("Não é final de semana :(")
elif dia == 1 or dia == 7:
    print("É fim de semana :)")
else:
    print("Dia não existe")