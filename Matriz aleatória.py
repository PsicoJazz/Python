import random

while True:
    lin  = int(input("Informe a quantidade de linhas: "))
    col  = int(input("Informe a quantidade de colunas: "))
    if lin > 0 and col > 0:
        M= []

        for i in range(lin):
            LINHA = []
            for j in range(col):
                num = random.randint(1, 11)
                LINHA.append(num)
            M.append(LINHA)
        break

        

#for x in (M):
    #print ("Sua matriz é : {}".format(x))

# Imprimir elemento específico matriz:
# print (M[linha][coluna])

for i in range(lin):
    for j in range (col):
        print (M[i][j], end = " ")
    print(" ")
