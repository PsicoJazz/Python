

genero = str(input('Qual o seu gênero: \n MASCULINO ou FEMININO:  '))
altura = float(input('Digite a sua altura: '))

if genero.upper() == ('MASCULINO'):
    imc = (altura * 72.7 )- 58
    print ('Seu imc é de {:.2f}'.format(imc))
    
else:
    imch = (altura * 62.1) - 44.7
    print ('Seu imc é de {:.2f}'.format(imch))
