def matInit(i):
	Matrix = {}
	with open('matrice.txt', encoding='utf8') as dat:
		text = dat.read()
		text = text.split('\n\n')
		lines = text[i].split('\n')
		size = lines[0].split()

		
		Matrix['r'] = int(size[0])
		Matrix['s'] = int(size[1])

		for line in lines[1:]:
			element = line.split()
			Matrix[(int(element[0]), int(element[1]))] = float(element[2])
	return Matrix

def matPrint(mat):
	output = ''
	for i in range(1, mat['r'] + 1):
		for j in range(1, mat['s'] + 1):
			output += "%9g" % float(mat.get((i, j), 0))
		output += '\n'
	print(output)

def matMult(mat1, mat2):
	mat = {}
	mat['r'] = mat1['r']
	mat['s'] = mat2['s']
	for i in range(1, mat1['r'] + 1):
		for j in range(1, mat2['s'] + 1):
			mat[(i, j)] = 0
			for k in range(1, mat1['s'] + 1):
				mat[(i, j)] += float(mat1.get((i, k), 0) * mat2.get((k, j), 0))
			if mat[(i, j)] == 0:
				del mat[(i, j)]
	return mat

mat1 = matInit(0)
mat2 = matInit(1)

print("1st matrix:")
matPrint(mat1)
print("2nd matrix:")
matPrint(mat2)

if mat1['s'] != mat2['r']:
	exit("Matrice nisu ulancane!!!")

umnozak = matMult(mat1, mat2)

print("Matrix multiplication gives:")
matPrint(umnozak)
