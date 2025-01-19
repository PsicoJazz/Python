
lista = []
par = []
impar = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)

    

    resp = input ("Existem mais numeros? [S|N]")
    if resp.upper() == "N":
        break

resul = print ("Você deseja  \n1. Pares  \n2. Ímpares ")

for x in lista:

    if resul == 1 and (lista % 2) == 0:
        par.append(x)
        print ("Números pares{}".format (par))

   
