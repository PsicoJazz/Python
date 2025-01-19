print ("COVID")

suspeitos = 0


while True:
    tosse = int(input("Tosse? \n1. Sim \n2.Não \nResposta."))
    febre = int(input("Febre? \n1. Sim \n2.Não \nResposta."))
    faltadear = int(input("falta de ar? \n1. Sim \n.Não \nResposta."))

    if tosse == 1 and febre == 1 and faltadear == 1:
        suspeitos += 1
        print ("Você esta com suspeita de COVID")
        
    resp = input("Ainda há pacientes a serem atendidos? [S|N]")
    if resp.upper() == "N":
        break

print ("o número de suspeitos foi {}".format (suspeitos))
 
