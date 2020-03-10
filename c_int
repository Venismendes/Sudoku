def cint(n):
	""" A função cint, recebe um valor (n) que pode ser uma número inteiro, real, string ou uma lista e converte o valor para número inteiro
	No caso de (n) ser uma lista irá converter cada um dos valores contidos na lista para inteiros e continuará sendo uma lista
	No caso de ser uma string vazia ou letra, receberá o valor padrão de 0
	"""
	try:
		n = int(n)
	except ValueError:
		n = 0
	except TypeError:
		c = 0
		for i in range(0, len(n)):
			try:
				n[i] = int(n[i])		
			except ValueError:
				n[i] = 0
			except TypeError:
				n[i] = 0
	return n
