m = 0
f = 0
maior = 0
media = 0

while True:

    sexo = int(input("Qual o seu gênero: \n.1 Masculino \n.2 Feminino  \n Resposta: "))
    idade = int(input("Digite sua idade: "))

    if sexo == 1:
        m += 1
    if sexo == 2:
        f += 1
    if sexo == 1 and idade > 17:
        maior += 1
    if sexo == 2 and idade > 0:
        media += idade / sexo

    resp =  input("Existem mais alunos na turma? [S|N]")
    if resp.upper() == "N":
        break

print ("A média aritimética das meninas é {:.2f}".format (media))   
print ("São de maior idade {} meninos".format (maior))
print ("O números de meninas é {}".format (f))
print ("O números de meninos é {}".format (m))
print ("Uma idade negativa -{}".format (idade))
