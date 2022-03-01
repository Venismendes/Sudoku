import random

def sudoku():
	"""A função sudoku tem como objetivo gerar um sudoku aleatório e completo e armazenar o valor na variável em que foi chamado a função, irá armazenar em apenas uma variável, uma lista com 9 listas contendo os números de 1 a 9 em casa uma, de forma que complete um sudoku, sendo o primeiro índice a primeira linha, o segundo índice a segunda linha e assim por diante"""
	# checks if some element of "list1" is in "list2"
	def all_diferent(list1, list2):
		is_on = False
		for i in list1:
			if i in list2:
				is_on = True

		return is_on

	# remove elements of "list1" from "list2"
	def list_remove(list1, list2):
		for i in list1:
			if i in list2:
				list2.remove(i)

	# checks if have a variable in a list
	def var_in_list(variavle, list_sc):
		for i in list_sc:
			if variavle in i:
				return True
		return False

	while True:
		n = list(range(1, 10))
		line = [0] * 9
		sc = [line[:]] * 9

		# ==========================================================================================================
		# line 1
		line = random.sample(n, 9)
		sc[0] = line[:]

		bloco1 = sc[0][0:3]
		bloco2 = sc[0][3:6]
		bloco3 = sc[0][6:9]
		# ==========================================================================================================
		# line 2
		attempt = 0
		while True:
			start_end = [0, 3], [3, 6], [6, 9]
			sc[1] = [0] * 9
			for start, end in start_end:
				n = list(range(1, 10))
				no_repeat = sc[0][start:end] + sc[1][0:start]
				list_remove(no_repeat, n)
				
				try:
					line = random.sample(n, 3)
					sc[1][start:end] = line[:]
					if 0 not in sc[1]:
						break
				except:
					pass
			
			attempt += 1
			if 0 not in sc[1]:
				break
			if attempt >= 10:
				break
			
		bloco1 += sc[1][0:3]
		bloco2 += sc[1][3:6]
		bloco3 += sc[1][6:9]
		# ==========================================================================================================
		# line 3
		attempt = 0
		while True:
			start_end = [0, 3], [3, 6], [6, 9]
			sc[2] = [0] * 9
			for start, end in start_end:
				n = list(range(1, 10))
				no_repeat = sc[0][start:end] + sc[1][start:end] + sc[2][0:start]
				list_remove(no_repeat, n)
				
				try:
					line = random.sample(n, 3)
					sc[2][start:end] = line[:]
					if 0 not in sc[2]:
						break
				except:
					pass
			
			attempt += 1
			if 0 not in sc[2]:
				break
			if attempt >= 10:
				break
			
		bloco1 += sc[2][0:3]
		bloco2 += sc[2][3:6]
		bloco3 += sc[2][6:9]

		# ==========================================================================================================
		columns = []
		empty_column = []
		for i in range(0, 9):
			column = empty_column[:]
			for line in sc:
				column.append(line[i])
			columns.append(column)
		# ==========================================================================================================
		# line 4
		attempt = 0
		while True:
			sc[3] = [0] * 9
			for i in range(0, 9):
				n = list(range(1, 10))
				no_repeat = columns[i] + sc[3][0:i]
				list_remove(no_repeat, n)
				
				try:
					sc[3][i] = random.choice(n)
				except:
					pass
			
			attempt += 1
			if 0 not in sc[3]:
				break
			if attempt >= 10:
				break
			
		bloco4 = sc[3][0:3]
		bloco5 = sc[3][3:6]
		bloco6 = sc[3][6:9]
		# ==========================================================================================================
		# line 5
		attempt = 0
		while True:
			sc[4] = [0] * 9
			for i in range(0, 9):
				if i in range(0, 3):
					block = bloco4[:]
				elif i in range(3, 6):
					block = bloco5[:]
				elif i in range(6, 9):
					block = bloco6[:]
				
				n = list(range(1, 10))
				no_repeat = columns[i] + sc[4][0:i] + block
				list_remove(no_repeat, n)
				
				try:
					sc[4][i] = random.choice(n)
				except:
					pass
			
			attempt += 1
			if 0 not in sc[4]:
				break
			if attempt >= 10:
				break
			
		bloco4 += sc[4][0:3]
		bloco5 += sc[4][3:6]
		bloco6 += sc[4][6:9]
		# ==========================================================================================================
		# line 6
		attempt = 0
		while True:
			sc[5] = [0] * 9
			for i in range(0, 9):
				if i in range(0, 3):
					block = bloco4[:]
				elif i in range(3, 6):
					block = bloco5[:]
				elif i in range(6, 9):
					block = bloco6[:]
				
				n = list(range(1, 10))
				no_repeat = columns[i] + sc[5][0:i] + block
				list_remove(no_repeat, n)
				
				try:
					sc[5][i] = random.choice(n)
				except:
					pass
			
			attempt += 1
			if 0 not in sc[5]:
				break
			if attempt >= 10:
				break
			
		bloco4 += sc[5][0:3]
		bloco5 += sc[5][3:6]
		bloco6 += sc[5][6:9]

		# ==========================================================================================================
		columns = []
		empty_column = []
		for i in range(0, 9):
			column = empty_column[:]
			for line in sc:
				column.append(line[i])
			columns.append(column)
		# ==========================================================================================================
		# line 7
		attempt = 0
		while True:
			sc[6] = [0] * 9
			for i in range(0, 9):
				n = list(range(1, 10))
				no_repeat = columns[i] + sc[6][0:i]
				list_remove(no_repeat, n)
				
				try:
					sc[6][i] = random.choice(n)
				except:
					pass

			attempt += 1
			if 0 not in sc[6]:
				break
			if attempt >= 10:
				break

		bloco7 = sc[6][0:3]
		bloco8 = sc[6][3:6]
		bloco9 = sc[6][6:9]
		# ==========================================================================================================
		# line 8
		attempt = 0
		while True:
			sc[7] = [0] * 9
			for i in range(0, 9):
				if i in range(0, 3):
					block = bloco7[:]
				elif i in range(3, 6):
					block = bloco8[:]
				elif i in range(6, 9):
					block = bloco9[:]
				
				n = list(range(1, 10))
				no_repeat = columns[i] + sc[7][0:i] + block
				list_remove(no_repeat, n)
				
				try:
					sc[7][i] = random.choice(n)
				except:
					pass
			
			attempt += 1
			if 0 not in sc[7]:
				break
			if attempt >= 10:
				break

		bloco7 += sc[7][0:3]
		bloco8 += sc[7][3:6]
		bloco9 += sc[7][6:9]
		# ==========================================================================================================
		# line 9
		attempt = 0
		while True:
			sc[8] = [0] * 9
			for i in range(0, 9):
				if i in range(0, 3):
					block = bloco7[:]
				elif i in range(3, 6):
					block = bloco8[:]
				elif i in range(6, 9):
					block = bloco9[:]
				
				n = list(range(1, 10))
				no_repeat = columns[i] + sc[8][0:i] + block
				list_remove(no_repeat, n)
				
				try:
					sc[8][i] = random.choice(n)
				except:
					pass
			
			attempt += 1
			if 0 not in sc[8]:
				break
			if attempt >= 10:
				break

		bloco7 += sc[8][0:3]
		bloco8 += sc[8][3:6]
		bloco9 += sc[8][6:9]

		if not var_in_list(0, sc):
			break
	return sc

def sudoku_i(sc, dificuldade):
	""" A função sudoku_i(sudoku incompleto), tem como objetivo receber o sudoku gerado na primeira função e a dificuldade nesse sudoku, para esconder alguns números, para que assim seja possível jogar

	sc: o sudoku completo
	dificuldade: 'facil', 'medio', 'dificil'
	"""
	#Dados que serão exibidos
	sl1 = sc[0][:]
	sl2 = sc[1][:]
	sl3 = sc[2][:]
	sl4 = sc[3][:]
	sl5 = sc[4][:]
	sl6 = sc[5][:]
	sl7 = sc[6][:]
	sl8 = sc[7][:]
	sl9 = sc[8][:]
	nlista = [sl1, sl2, sl3, sl4, sl5, sl6, sl7, sl8, sl9]

	i = 0
	n = (0, 1, 2, 3, 4, 5, 6, 7, 8)

	if dificuldade == 'facil':
		for conteL in nlista:
			for c in range(0, 5):
				facil = random.choice(n)
				conteL[facil] = ''
			nlista[i] = conteL
			i = i + 1
	if dificuldade == 'medio':
		for conteL in nlista:
			for c in range(0, 6):
				medio = random.choice(n)
				conteL[medio] = ''
			nlista[i] = conteL
			i = i + 1

	if dificuldade == 'dificil':
		for conteL in nlista:
			for c in range(0, 7):
				dificil = random.choice(n)
				conteL[dificil] = ''
			nlista[i] = conteL
			i = i + 1
			
	return nlista

		
def verificar_sudoku(sv):
	""" A função verificar_sudoku, tem como objetivo receber um sudoku que o próprio usuário preencheu e analisar se ele está correto e retorna o valor True caso esteja correto e False caso esteja errado

	sv: sudoku a ser verificado
	"""

	#todas as linhas
	l1 = sv[0]
	l2 = sv[1]
	l3 = sv[2]
	l4 = sv[3]
	l5 = sv[4]
	l6 = sv[5]
	l7 = sv[6]
	l8 = sv[7]
	l9 = sv[8]

	#todos os blocos
	b1 = [l1[0], l1[1], l1[2], l2[0], l2[1], l2[2], l3[0], l3[1], l3[2]]
	b2 = [l1[3], l1[4], l1[5], l2[3], l2[4], l2[5], l3[3], l3[4], l3[5]]
	b3 = [l1[6], l1[7], l1[8], l2[6], l2[7], l2[8], l3[6], l3[7], l3[8]]	
	b4 = [l4[0], l4[1], l4[2], l5[0], l5[1], l5[2], l6[0], l6[1], l6[2]]
	b5 = [l4[3], l4[4], l4[5], l5[3], l5[4], l5[5], l6[3], l6[4], l6[5]]
	b6 = [l4[6], l4[7], l4[8], l5[6], l5[7], l5[8], l6[6], l6[7], l6[8]]	
	b7 = [l7[0], l7[1], l7[2], l8[0], l8[1], l8[2], l9[0], l9[1], l9[2]]
	b8 = [l7[3], l7[4], l7[5], l8[3], l8[4], l8[5], l9[3], l9[4], l9[5]]
	b9 = [l7[6], l7[7], l7[8], l8[6], l8[7], l8[8], l9[6], l9[7], l9[8]]

	#todas as colunas
	c1 = [l1[0], l2[0], l3[0], l4[0], l5[0], l6[0], l7[0], l8[0], l9[0]]
	c2 = [l1[1], l2[1], l3[1], l4[1], l5[1], l6[1], l7[1], l8[1], l9[1]]
	c3 = [l1[2], l2[2], l3[2], l4[2], l5[2], l6[2], l7[2], l8[2], l9[2]]
	c4 = [l1[3], l2[3], l3[3], l4[3], l5[3], l6[3], l7[3], l8[3], l9[3]]
	c5 = [l1[4], l2[4], l3[4], l4[4], l5[4], l6[4], l7[4], l8[4], l9[4]]
	c6 = [l1[5], l2[5], l3[5], l4[5], l5[5], l6[5], l7[5], l8[5], l9[5]]
	c7 = [l1[6], l2[6], l3[6], l4[6], l5[6], l6[6], l7[6], l8[6], l9[6]]
	c8 = [l1[7], l2[7], l3[7], l4[7], l5[7], l6[7], l7[7], l8[7], l9[7]]
	c9 = [l1[8], l2[8], l3[8], l4[8], l5[8], l6[8], l7[8], l8[8], l9[8]]

	#ll = lista com todas as linhas
	lista_linhas = l1, l2, l3, l4, l5, l6, l7, l8, l9
	#lc = lista com todas as colunas
	lista_colunas = c1, c2, c3, c4, c5, c6, c7, c8, c9
	#lb = lista com todos os blocos
	lista_blocos = b1, b2, b3, b4, b5, b6, b7, b8, b9

	ctd = 0
	ctdb = 0
	cb = 0
	correto = True
	for linha in lista_linhas:
		for num in linha:
			if lista_colunas[ctd].count(num) > 1 or lista_blocos[ctdb].count(num) > 1 or linha.count(num) > 1:
				correto = False
				ctd += 1
			else:
				ctd += 1
				
			if ctd == 3:
				ctdb += 1
			if ctd == 6:
				ctdb += 1
			if ctd == 8:
				cb += 1
				ctd -= ctd
				ctdb = 0
				if cb > 3:
					ctdb = 3
				if cb > 5:
					ctdb = 6
				
	return correto

if __name__ == '__main__':

	completed_sudoku = sudoku()
	for line in completed_sudoku:
		print(line)
	print(verificar_sudoku(completed_sudoku))


	uncompleted_sudoku = sudoku_i(completed_sudoku, 'facil')
	for line in uncompleted_sudoku:
		print(line)
	print(verificar_sudoku(uncompleted_sudoku))