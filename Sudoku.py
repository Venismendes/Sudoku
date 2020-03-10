import random

def sudoku():
	"""A função sudoku tem como objetivo gerar um sudoku aleatório e completo e armazenar o valor na variável em que foi chamado a função, irá armazenar em apenas uma variável, uma lista com 9 listas contendo os números de 1 a 9 em casa uma, de forma que complete um sudoku, sendo o primeiro índice a primeira linha, o segundo índice a segunda linha e assim por diante"""
	n = (1, 2, 3, 4, 5, 6, 7, 8, 9)
	c = 0
	loop = 0
	
	#cada linha do sudoku
	l1 = [0,0,0,0,0,0,0,0,0]
	l2 = [0,0,0,0,0,0,0,0,0]
	l3 = [0,0,0,0,0,0,0,0,0]
	l4 = [0,0,0,0,0,0,0,0,0]
	l5 = [0,0,0,0,0,0,0,0,0]
	l6 = [0,0,0,0,0,0,0,0,0]
	l7 = [0,0,0,0,0,0,0,0,0]
	l8 = [0,0,0,0,0,0,0,0,0]
	l9 = [0,0,0,0,0,0,0,0,0]
	
	nl = 0
	while nl < 10:
		#sorteando os numeros de cada linha
		for i in range(0, 9): #linha 1
		   l1[i] = random.choice(n)
		   veri = i
		   while l1[veri] in  l1[:veri]:
		      l1[i] = random.choice(n)
		
		
		#adicionando os dados para comparar nos próximos sorteios
		bloco1 = l1[0:3]
		bloco2 = l1[3:6]
		bloco3 = l1[6:9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 2
		   l2[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l2[veri] in l2[:veri] or l2[veri] in bloco1:
		         l2[i] = random.choice(n)
		
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0   
		   if i >= 3 and i <6:
		      while l2[veri] in l2[:veri] or l2[veri] in bloco2:
		         l2[i] = random.choice(n)         
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break                        
		   c = 0   
		   if i >= 6 and i < 9:
		      while l2[veri] in l2[:veri] or l2[veri] in bloco3:
		         l2[i] = random.choice(n)
		         
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100: #caso entre em loop a linha será reiniciada
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break
		
		
		bloco1 = bloco1 + l2[0:3]
		bloco2 = bloco2 + l2[3:6]
		bloco3 = bloco3 + l2[6:9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 3
		   l3[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l3[veri] in l3[:veri] or l3[veri] in bloco1:
		         l3[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 3 and i <6:
		      while l3[veri] in l3[:veri] or l3[veri] in bloco2:
		         l3[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 6 and i < 9:
		      while l3[veri] in l3[:veri] or l3[veri] in bloco3:
		         l3[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100:
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break
		
		
		bloco1 = bloco1 + l3[0:3]
		bloco2 = bloco2 + l3[3:6]
		bloco3 = bloco3 + l3[6:9]
		
		c1 = [l1[0], l2[0], l3[0]]
		c2 = [l1[1], l2[1], l3[1]]
		c3 = [l1[2], l2[2], l3[2]]
		c4 = [l1[3], l2[3], l3[3]]
		c5 = [l1[4], l2[4], l3[4]]
		c6 = [l1[5], l2[5], l3[5]]
		c7 = [l1[6], l2[6], l3[6]]
		c8 = [l1[7], l2[7], l3[7]]
		c9 = [l1[8], l2[8], l3[8]]
		llista = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 4
		   l4[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l4[veri] in l4[:veri] or l4[veri] in llista[veri]:
		         l4[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 3 and i <6:
		      while l4[veri] in l4[:veri] or l4[veri] in llista[veri]:
		         l4[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 6 and i < 9:
		      while l4[veri] in l4[:veri] or l4[veri] in llista[veri]:
		         l4[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100:
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break
		   	
		
		bloco4 = l4[0:3]
		bloco5 = l4[3:6]
		bloco6 = l4[6:9]
		
		
		c1 = c1 + [l4[0]]
		c2 = c2 + [l4[1]]
		c3 = c3 + [l4[2]]
		c4 = c4 + [l4[3]]
		c5 = c5 + [l4[4]]
		c6 = c6 + [l4[5]]
		c7 = c7 + [l4[6]]
		c8 = c8 + [l4[7]]
		c9 = c9 + [l4[8]]
		llista = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 5
		   l5[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l5[veri] in l5[:veri] or l5[veri] in bloco4 or l5[veri] in llista[veri]:
		         l5[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 3 and i <6:
		      while l5[veri] in l5[:veri] or l5[veri] in bloco5 or l5[veri] in llista[veri]:
		         l5[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 6 and i < 9:
		      while l5[veri] in l5[:veri] or l5[veri] in bloco6 or l5[veri] in llista[veri]:
		         l5[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100:
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break	   
		
		
		bloco4 = bloco4 + l5[0:3]
		bloco5 = bloco5 + l5[3:6]
		bloco6 = bloco6 + l5[6:9]
		
		c1 = c1 + [l5[0]]
		c2 = c2 + [l5[1]]
		c3 = c3 + [l5[2]]
		c4 = c4 + [l5[3]]
		c5 = c5 + [l5[4]]
		c6 = c6 + [l5[5]]
		c7 = c7 + [l5[6]]
		c8 = c8 + [l5[7]]
		c9 = c9 + [l5[8]]
		llista = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 6
		   l6[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l6[veri] in l6[:veri] or l6[veri] in bloco4 or l6[veri] in llista[veri]:
		         l6[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 3 and i <6:
		      while l6[veri] in l6[:veri] or l6[veri] in bloco5 or l6[veri] in llista[veri]:
		         l6[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 6 and i < 9:
		      while l6[veri] in l6[:veri] or l6[veri] in bloco6 or l6[veri] in llista[veri]:
		         l6[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100:
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break
		   		
		
		bloco4 = bloco4 + l6[0:3]
		bloco5 = bloco5 + l6[3:6]
		bloco6 = bloco6 + l6[6:9]
		
		c1 = c1 + [l6[0]]
		c2 = c2 + [l6[1]]
		c3 = c3 + [l6[2]]
		c4 = c4 + [l6[3]]
		c5 = c5 + [l6[4]]
		c6 = c6 + [l6[5]]
		c7 = c7 + [l6[6]]
		c8 = c8 + [l6[7]]
		c9 = c9 + [l6[8]]
		llista = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 7
		   l7[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l7[veri] in l7[:veri] or l7[veri] in llista[veri]:
		         l7[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 3 and i <6:
		      while l7[veri] in l7[:veri] or l7[veri] in llista[veri]:
		         l7[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 6 and i < 9:
		      while l7[veri] in l7[:veri] or l7[veri] in llista[veri]:
		         l7[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100:
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break
		   		
		
		bloco7 = l7[0:3]
		bloco8 = l7[3:6]
		bloco9 = l7[6:9]
		
		
		c1 = c1 + [l7[0]]
		c2 = c2 + [l7[1]]
		c3 = c3 + [l7[2]]
		c4 = c4 + [l7[3]]
		c5 = c5 + [l7[4]]
		c6 = c6 + [l7[5]]
		c7 = c7 + [l7[6]]
		c8 = c8 + [l7[7]]
		c9 = c9 + [l7[8]]
		llista = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 8
		   l8[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l8[veri] in l8[:veri] or l8[veri] in bloco7 or l8[veri] in llista[veri]:
		         l8[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 3 and i <6:
		      while l8[veri] in l8[:veri] or l8[veri] in bloco8 or l8[veri] in llista[veri]:
		         l8[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 6 and i < 9:
		      while l8[veri] in l8[:veri] or l8[veri] in bloco9 or l8[veri] in llista[veri]:
		         l8[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100:
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break	
		   	
		
		bloco7 = bloco7 + l8[0:3]
		bloco8 = bloco8 + l8[3:6]
		bloco9 = bloco9 + l8[6:9]
		
		c1 = c1 + [l8[0]]
		c2 = c2 + [l8[1]]
		c3 = c3 + [l8[2]]
		c4 = c4 + [l8[3]]
		c5 = c5 + [l8[4]]
		c6 = c6 + [l8[5]]
		c7 = c7 + [l8[6]]
		c8 = c8 + [l8[7]]
		c9 = c9 + [l8[8]]
		llista = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
		
		
		i = 0
		loop = 0
		while i < 9: #linha 9
		   l9[i] = random.choice(n)
		   veri = i
		   
		   c = 0
		   if i < 3:
		      while l9[veri] in l9[:veri] or l9[veri] in bloco7 or l9[veri] in llista[veri]:
		         l9[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 3 and i <6:
		      while l9[veri] in l9[:veri] or l9[veri] in bloco8 or l9[veri] in llista[veri]:
		         l9[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   c = 0
		   if i >= 6 and i < 9:
		      while l9[veri] in l9[:veri] or l9[veri] in bloco9 or l9[veri] in llista[veri]:
		         l9[i] = random.choice(n)
		         c = c + 1
		         loop = loop + 1
		         if c > 100:
		            i = 0
		            break
		   i = i + 1
		   if c > 100:
		      c = c - c
		      i = 0
		   if loop > 1000:
		   	break
		   		
		
		bloco7 = bloco7 + l9[0:3]
		bloco8 = bloco8 + l9[3:6]
		bloco9 = bloco9 + l9[6:9]
		
		c1 = c1 + [l9[0]]
		c2 = c2 + [l9[1]]
		c3 = c3 + [l9[2]]
		c4 = c4 + [l9[3]]
		c5 = c5 + [l9[4]]
		c6 = c6 + [l9[5]]
		c7 = c7 + [l9[6]]
		c8 = c8 + [l9[7]]
		c9 = c9 + [l9[8]]
		
		nl = nl + 1
		if loop <= 1000:
			break
		loop = 0
		
	#sudoku completo
	sc = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

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
