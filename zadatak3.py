studenti = {}

# studenti[JMBAG] = {ime, prezime, labosi=(redniBroj, grupa, brojBodova)}

labs = {}

for file in os.listdir("."):
	fileName = file.split('/').pop()
	if(fileName == 'students.txt'):
		with open(file) as dat:
	    	students = dat.readlines()
	else:
		with open(file) as dat:
			labs[fileName] = dat.readlines()

for stud in students:
	# JMBAG Ime Prezime
	pom = stud.split()
	JMBAG = pom[0]
	ime = pom[1]
	prezime = pom[2]

	labosi = []

	for lab in labs.keys():
		# Lab_03_g08.txt
		pom = lab.split('_')
		redniBroj = int(pom[2])
		grupa = int(pom[3].pop(0)) # pop(0) miče slovo g
		
		dat = labs[lab] # lista redova datoteke pojedinog labosa
		for line in dat:
			# jmbag brojBodova
			if int(line.split()[0]) == JMBAG:
				brojBodova = line.split()[1]
		labosi.append((redniBroj, grupa, brojBodova))

	studenti[JMBAG] = {ime, prezime, labosi}

# za svakog studenta mi treba lista njegovih labosa
print("JMBAG Prezime, Ime L1 L2 L3")
for stud in studenti.items():
	print(stud)
