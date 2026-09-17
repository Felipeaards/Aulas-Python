opcao = int(input("Digite a opção (0 a 3): "))

#A estrutura Match-Case compara por padrão valores por igualdade
#Não há limitação para cases, mas sempre deve haver no mínimo
#um CASE e um CASE DEFAUT (_)

match opcao: #Variável que será verificada
    case 0: #Opção caso igual a esse valor
        print("Opção 0")
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case _:
        print("Nenhuma das alternativas")