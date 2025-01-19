n = 0
divisor = 0
elementos = 0
media = 0

while True:

    n = int(input("Digite o número desejado: "))

    if n > 0:
        media += n
    if media > 0:
        elementos += 1        
        divisor = media / elementos
        

    resp = input("Existem mais números a serem incluídos? [S|N]")
    if resp.upper() == "N":
        break

print ("A média de seus elementos é {:.1f}".format (divisor))
