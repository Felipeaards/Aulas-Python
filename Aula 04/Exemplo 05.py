nome = input("Digite o nome de Usuário: ")
senha = input("Digite a senha: ")

if (nome != "Felipe" or senha != "1234"): #Se a senha OU o nome for diferentes, ele dá o primeiro resultado
    print("Usuário ou senha incorretos!!")
else:
    print("Usuário e senha corretos!!")


if (nome == "Felipe" and senha == "1234"):
    print("Usuário e senha corretos!!")
else:
    print("Usuário ou senha incorretos!!")