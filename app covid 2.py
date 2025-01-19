print ("APP COVID - 19")

suspeitos = 0
pacientes = int(input("Digite a quantidade de pacientes: "))

for x in range(pacientes):
    tosse = int(input("Está com tosse? 1.SIm 2.Não : "))
    febre = int(input("Está com febre? 1.SIm 2.Não : "))
    faltaar = int(input("Está com falta de ar? 1.SIm 2.Não : "))

    if tosse == 1 and febre == 1 and faltaar == 1:
        suspeitos += 1

print ("Número de paciente com suspeitas: {}".format (suspeitos))





