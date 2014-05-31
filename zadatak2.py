# Vaš zadatak: Potrebno je napisati skriptu koja ce na temelju ulazne datoteke ( ulaz.txt) generirati
# tablicu, u kojoj ce pojedini redak odgovarati hipotezi, a u njemu će biti navedene vrijednosti mjere
# HD za razlicite vrijednosti parametra HD (korak neka bude 10%, odnosno 0.1)
# Ispis treba biti u sljedecem obliku (prvi zapis u retku je redni broj hipoteze, tj. odgovaraju ćeg retka
# ulazne datoteke, a prvi redak je zaglavlje tablice):
# 	Hyp#Q10#Q20#Q30# ... #Q90
# 	001#1.25#1.75#2.21# ... #21.34

ulaz = []
with open('ulaz.txt') as dat:
    ulaz = dat.readlines()

print("Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90")
for red in ulaz:
	brojevi = red.split()
	brojevi.sort()
	print("#".join(Hyp(brojevi).values))

def Hyp(brojevi):
	lista = {}
	indeksi = vratiIndekseZaDanuVelicinuPolja(brojevi)
	for i in range(1, 9):
		indeks = indeksi[i]
		lista[i] = brojevi[indeks]
	return lista

def vratiIndekseZaDanuVelicinuPolja(polje):
	indeksi = {}
	for i in range(1, 9):
		indeksi[i] = int(len(polje) * (i/10))
	return indeksi
