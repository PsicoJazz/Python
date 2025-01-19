


nota1 = int(input("Insira a nota do 1º bimestre: "))
nota2 = int(input("Insira a nota do 2º bimestre: "))
nota3 = int(input("Insira a nota do 3º bimestre: "))

print("Sua notas foram: ", nota1,",", nota2,",", nota3)

resultado = (nota1 + nota2 + nota3) / 3

print ("Sua média é de:", resultado)

if resultado >= 6:
    print ("Parabéns, você foi aprovado!")

else:
    resultado <= 5
    print ("Reprovado")

print ("fim")
