
marca = []
valor = []


while True:
    nome_produto = input("Digite o produto: ")
    preço        = float(input("Digite o preço"))


    marca.append(nome_produto)
    valor.append(preço)
    
    resp = input("Deseja digitar mais produtos? [S|N]")
    if resp.upper() == "N":
        break

barato = valor.index(min(valor))
caro   = valor.index(max(valor))

print ("O produto mais barato é {}".format(marca[barato]))
print ("O produto mais caro é {}".format(marca[caro]))
