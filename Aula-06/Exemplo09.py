# Gerenciar Aluno
# 1 - Cadastrar
# 2 - Consular
# 3 - Atualizar
# 4 - Remover
# 5 - Listar
# 6 - Sair do programa


while True:
    print("Gerenciar Aluno")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Atualizar")
    print("4 - Remover")
    print("5 - Listar")
    print("6 - Sair do programa")
    opcao = input("Digite uma opção: ")

    # Função is digit é usada para verificar se a variável opcao é um número
    if opcao.isdigit():
        opcao = int(opcao)
        match opcao:
            case 1:
                print("Cadastrando Aluno")
            case 2:
                print("Consultar Aluno")
            case 3:
                print("Atualizar Aluno")
            case 4:
                print("Remover Aluno")
            case 5:
                print("Listar Aluno")
            case 6:
                print("Sair do sistema")
                break
            case _:
                print("Opção inválida, tente novamente")
    else:
        print("O valor informado não é um número, tente novamente")