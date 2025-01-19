
numeros = 0
pares = 0

for x in range (5):
    n = int(input("Digite o número desejado: "))
    numeros += 1
    if (n % 2) == 0:
        pares += 1

print ("O total de números pares é de {}".format (pares))
print ("O total de números digitados é de {}".format (numeros))
