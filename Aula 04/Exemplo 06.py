idade = int(input("Digite a sua idade: "))
cnh = input("Tem CNH? (S/N): ")

if idade >= 18 and cnh == "S" or idade >= 18 and cnh =="s": #Por esse tipo de lógica
    # é melhor colocar um if dentro de outro, se não fica confuso e embaralhado
    print("Você tem permissão para dirigir!")
elif idade >= 18 and cnh == "N" or idade >= 18 and cnh == "n":
    print("Você pode solicitar a CNH para ter o direito de dirigir")
else:
    print("Você não pode dirigir por não ter idade ou a CNH para isso")