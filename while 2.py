suspeitos = 0
pacientes = int(input("Quantidade de pacientes: "))
cont = 0

while cont < pacientes:    
    tosse = int(input("Tosse? \n1. SIM  \n2.Não  \nResp.: "))
    febre = int(input("Febre? \n1. SIM  \n2.Não    \nResp.:"))
    faltaar = int(input("Falta de ar? \n1. SIM  \n2.Não   \nResp.: "))

    if tosse == 1 and febre == 1 and faltaar == 1:
        suspeitos += 1
    cont += 1 
    
else:
    print ("Acabaram os pacientes")

print ("São esses total de pacientes suspeitos {}".format(suspeitos))
