lista = []
segredo = ""
cont = 0

palavra = input("Digite uma palavra: ")
lista.append(palavra)

for x in lista:
    if (x == "z"): x == "a"
    elif (x == "Z"): x == "A"
    else: x += chr(ord(x)+1)
print (x)
