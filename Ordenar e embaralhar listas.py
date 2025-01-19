
nomes = []

while True:
    name = input("Digite o nome desejado: ")
    nomes.append(name)

    resp = input("Deseja digitar outro nome?  [S|N]")
    if resp.upper() == "N":
        break
            

# Coloca a lista em ordem alfabética (obs: Iniciais Maiúsculas vem antes de minúsculas)
nomes.sort()

# Coloca a lista em ordem Decrescente
nomes.sort(reverse = True)

# Embaralhar lista
random.shuffle(nomes)


for x in nomes:
    print(x)
