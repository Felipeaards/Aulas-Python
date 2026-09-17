idade = int(input("Digite sua idade: "))

match idade:
    case x if x >=18:  #O "x" sempre se refere à variável do match (idade nesse caso)
        print("Maior de idade")
    case x if x < 18:
        print("Menor de idade")
    case _:
        print("Valor inválido")