totalEconomizado = 0  #Isso já é inicializar uma variável
mes = 1 #Isso já é inicializar uma variável


while mes <= 3:
    valor = float(input("Digite o valor a ser economizado: "))
    totalEconomizado = totalEconomizado + valor  #acumulador
    mes += 1 # contador

print("Paravéns, você economizou ", totalEconomizado)

#Contador normalmente é utilizado na condição loop, incrementa valores por padrão
#Acumulador PODE ser utilizado na condição loop, não soma ou acumula valores padronizados



