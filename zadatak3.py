import os

def zadatak():
	studenti = {}
	labs = {}
	# studenti[JMBAG] = student -> student[labos] = brojBodova
	files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) and f.endswith(".txt") ]
	for file in files:
		fileName = file.split('/').pop()
		if(fileName == 'studenti.txt'):
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
		labosi = {}
		for lab in labs.keys():
			# Lab_03_g08.txt
			pom = lab.split('.')[0].split('_')
			redniBroj = int(pom[1])
			grupa = int(pom[2][1:]) # [1:] mice slovo g		
			dat = labs[lab] # lista redova datoteke pojedinog labosa
			for line in dat:
				# jmbag brojBodova
				if int(line.split()[0]) == int(JMBAG):
					brojBodova = float(line.split()[1])
					if (JMBAG, redniBroj) in labosi:
						print("Student " + ime + ", " + prezime + " je vise puta obavio " + str(redniBroj) + ". labos!")
					else:
						labosi[(JMBAG, redniBroj)] = (grupa, brojBodova)
		studenti[JMBAG] = (ime, prezime, labosi)
	# za svakog studenta mi treba lista njegovih labosa
	print("JMBAG Prezime, Ime L1 L2 L3")
	for stud in studenti.items():
		print(stud)
