
cargo = str(input("Digite seu cargo "))

salario = float(input("Digite seu salario "))

if cargo == ("programador"):
    reajuste1 = (salario * 50)/100
    print ("Seu salário final é de: ", (salario + reajuste1))

elif cargo == ("analista de sistemas"):
    reajuste2 = (salario * 40)/100
    print ("Seu salário final é de: ", salario + reajuste2)

elif cargo == ("analista de dados"):
    reajuste3 = (salario * 30)/100
    print ("Seu salário final é de: ", salario + reajuste3)

else:
    print("Cargo inválido")







