suspeitos = 0

while True:
    tosse = int(input("Tosse ?  \n.1 Sim \n.2 Não \nResp.: "))
    febre = int(input("febre ?  \n.1 Sim \n.2 Não \nResp.: "))
    falta_ar = int(input("Falta de ar ?  \n.1 Sim \n.2 Não \nResp.: "))

    if tosse == 1 and febre == 1 and falta_ar == 1:
        suspeitos += 1

    resp = input ( "Ainda há pacientes a serem atendidos ? [S\N]")
    if resp.upper() == "N"
        break

print ("Suspeitos de COVID {}".format(suspeitos))
    
