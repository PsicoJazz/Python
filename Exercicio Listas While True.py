lindas = []

while True:
    nome = input("Digite o nome de uma atriz: ")
    lindas.append(nome)
    
   

    resp = input("Existem mais nomes a ser adicionados:? [S|N]")
    if resp.upper() == "N":
        break

#print (lindas)

for nome in lindas:
    print (nome)
