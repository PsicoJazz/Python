lista = []
elem = 0


while True:
    numero = int(input("Digite o número desejado "))
    lista.append(numero)
    elem += 1

    
    resp = input ("Existem mais números? [S|N]")
    if resp.upper() == "N":
        break

#sum(lista)
#len(lista)
#max(lista)
#min(lista)
#len(lista)

resul = (min(lista) * max(lista) ** (1 / (elem)))
print ("A média geométrica {:.2f}".format(resul))
