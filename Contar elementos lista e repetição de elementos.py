idade = []

idade.append(8)
idade.append(9)
idade.append(10)
idade.append(7)
idade.append(8)
idade.append(5)

# Para contar os elementos de uma lista
print (len(idade))

# Para contar repetição de informaçoes (ex:8)
print (idade.count(8))


# Para saber valor mínimo e máximo da lista
print ("A menor idade é {}".format(min(idade)))
print ("A maior idade é {}".format(max(idade)))

# Para SOMAR os valores da lista
print ("A soma das idades é {}".format(sum(idade)))

# Para Calcular a MEDIA de uma lista
print ("A média da idade é {:.2f}".format (sum(idade) / len(idade)))
