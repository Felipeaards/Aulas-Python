idade = int(input("Digite a idade"))
cnh = input("Tem CNH? (Sim ou Nao)")

match idade,cnh:
    case x,y if x>=18 and y=="Sim":  #x e y podem ser substituídos por valores diretamente
        print("Está apto a dirigir")
    case x,y if x < 18 and y=="Nao":
        print("Não pode dirigir")
    case _:
        print("Valores inválidos")