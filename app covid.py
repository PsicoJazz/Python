print ("APP DIAGNÍSTICO COVID - 19 ")


suspeitos = 0
pacientes = int(input("Informe a quantidade de pacientes: "))

for x in range(pacientes):
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nResp.: "))
    febre = int(input("Febre? \n1. Sim \n2. Não \nResp.: "))
    faltaar = int(input("Falta de ar? \n1. Sim \n2. Não \nResp.: "))

    if tosse == 1 and febre == 1 and faltaar == 1:
        suspeitos += 1

print ("Paciente com suspeita de COVID: {}".format (suspeitos))


 



