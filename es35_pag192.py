conto = ["IT 34 G 57382 85723 485735124853", "IT 63 V 67825 79823 878376892363", "IT 45 S 49823 89683 939859344532"]
saldi = ["60000 €", "40000 €", "100000 €"]
d = {}

for n in range(len(conto)):
    d[conto[n]] = saldi[n]

conto_domanda = input("Inserisci il conto corrente di cui vuoi conoscere il sando: ")
risp = conto_domanda.upper()

if risp in conto:
    print("Su questo conto il sando è di:", d[risp])
else:
    print("Il conto corrente inserito non è inesistente nella mappa!")