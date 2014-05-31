# bljljf

procitano = []

with open('matrice.txt', encoding='utf8') as dat:
    procitano = dat.readlines()

mat1 = matInit(priv[0])
mat2 = matInit(priv[1])

print(matMult(dictToMatrix(mat1, broj), dictToMatrix(mat2, broj))

# Učitava dvije matrice u zadanom formatu, odvojene su praznim redom
def matsInit(redovi):
    Matrices = {}
    # Matrices[0] = {} # Matrix1
    # Matrices[1] = {} # Matrix2

	mat1 = []

	while (line = First(redovi)) != '\n':    	
		mat1.append(line)
	mat2 = redovi # ono što je ostalo su retci druge matrice

	Matrices[0] = matInit(mat1)
	Matrices[1] = matInit(mat2)

	return Matrices


# Učitava jednu od tih matrica, prvi red je broj redaka i stupaca, ostalo su random retci i stupci sa vrijednostima
def matInit(redovi):
	Matrix = {}

	brojevi = First(redovi).split()
	brojRedaka = brojevi[0]
	brojStupaca = brojevi[1]

	for line in redovi:
		pom = line.split()
		redak = int(pom[0])
		stupac = int(pom[1])
		vrijednost = float(pom[2])

		Matrix[(redak, stupac)] = vrijednost
	return Matrix

# Množi dvije matrice dane u obliku [][]
def matMult(a,b):
    zip_b = zip(*b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) 
              for col_b in zip_b] for row_a in a]

# Pretvara matricu iz dicta u [][], gdje umjesto nepostojećiš kombinacija (i,j) stavlja 0
def dictToMatrix(dict, broj):
	mat = [][]
	for i in xrange(0, broj):
		for j in xrange(0, broj):
			mat[i][j] = dict.get((i,j), 0)
	return mat

# Vraća i briše prvi element liste
def First(a):
	return a.pop(0)
