
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
for marca, valor in enumerate(marca):
    print ("{} --> {}".format(marca, valor))
