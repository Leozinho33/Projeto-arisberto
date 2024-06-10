apresentapalavra(letras,palavra):
novapalavra = " _ " * len (palavra)
for lin range (0, len(letras)):
    for P in range (0,len(palavra)):
        if palavra[P] == letras [L]:
            novapalavra = novapalavra[0:p*2]
            palavra[P] + " " +
            novapalavra [P*2: ]
return novapalavra
