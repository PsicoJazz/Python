

alunos = []
num = 0

while True:
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    num += 1 

    resp = input("Existem mais alunos na turma?  [S|N] ")
    if resp.upper() == "N":
        break

alunos.sort()

for lista in alunos:
    print (lista)

print ("O número de alunos na turma é: {}".format(num))
