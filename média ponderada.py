


nota1 = int(input("Digite sua 1º nota: "))
nota2 = int(input("Digite sua 2º nota: "))

print ("Sua 1ª nota é: ", nota1)
print ("Sua 2ª nota é: ", nota2)

resultado1 = nota1 * 2
resultado2 = nota2 * 3

print ("Sua 1ª nota ponderada é: ", resultado1)
print ("Sua 2ª nota ponderada é: ", resultado2)

media = (resultado1 + resultado2) / 2

print ("Sua média final é: ", media)

if media >= 15:
    print ("Parabéns, você está aprovado. ")

else:
        media <= 15
        print ("Reprovado!")
