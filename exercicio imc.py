
genero = str(input("Digite seu genero: masculino ou feminino "))
altura = float(input("Digite sua altura: "))


if genero.lower() == ("masculino"):
    imc1 = (altura * 72.7) - 58
    print ("Seu IMC é de: {:.2f} KG".format(imc1))

elif genero.lower() == ("feminino"):
    imc2 = (62.1 * altura) - 44.7
    print ("Seu imc é de: {:.2f} KG".format (imc2))

else:
    print ("Genero não encontrado")
