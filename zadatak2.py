def vratiIndekseZaDanuVelicinuPolja(polje):
	indeksi = {}
	for i in range(1, 10):
		indeksi[i] = int(len(polje) * (i/10))
	return indeksi

def Hyp(brojevi):
	lista = []
	indeksi = vratiIndekseZaDanuVelicinuPolja(brojevi)
	for i in range(1, 10):
		indeks = indeksi[i]
		lista.append(brojevi[indeks])
	return lista

ulaz = []
with open('ulaz.txt') as dat:
    ulaz = dat.readlines()

print("Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90")
for red in ulaz:
	brojevi = red.split()
	brojevi.sort(key=float)
	print("#".join(Hyp(brojevi)))
