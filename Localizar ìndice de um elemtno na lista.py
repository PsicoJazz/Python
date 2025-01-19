#for x in range(5):
#    nome = input("Nome: ")
#    t = input("Tempo: ")

#    nadadoras.append(nome)
#    tempo.append(t)

# Índice -->   0       1         2       3       4
nadadoras = ["Susy","Anastacia","Elis","Maria","Tonha"]
tempo =     [17.3  , 15        , 13   , 19    , 16]

# Informar melhor e pior tempo
# Nome da lista.index(elemento)

melhor_tempo = tempo.index(min(tempo))
pior_tempo   = tempo.index(max(tempo))

print ("Melhor tempo é {}".format(nadadoras[melhor_tempo]))
print ("Pior tempo é {}".format(nadadoras[pior_tempo]))
