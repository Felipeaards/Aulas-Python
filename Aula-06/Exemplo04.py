contador = 1

while contador < 10:
    contador += 1
    if contador == 5:
        print("Pulei o 5")
        continue #Faz o laço voltar para o loop sem o finalizar
    print(contador)
print("Fora do laço")