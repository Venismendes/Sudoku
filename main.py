from Sudoku import sudoku, sudoku_i, verificar_sudoku
from c_int import cint
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import json

#Variáveis globais, que serão usadas em várias classes e funções diferentes
dificuldade = nome = ''
lista_completa = su = []
s = m = h = 0
tempo = '00:00:00'

#Gerenciador das telas
class Ukivy(ScreenManager):
	pass
		
#Menu principal	
class Menu(Screen):
	pass

#Tela para escolher a dificuldade do jogo
class Dificuldade(Screen):
	def __init__(self, **kwargs):
		super(Screen, self).__init__(**kwargs)
		pass
		self.novojogo = Novo_jogo()
	pass

#Tela onde o jogo será exibido	
class Novo_jogo(Screen):
	def __init__(self, **kwargs):
		super(Screen, self).__init__(**kwargs)
		self.cronometro = 0
		pass
		self.recorde = Recordes()
	
	
	def facil(self, *args):
			global dificuldade
			dificuldade  = 'facil'
	
	
	def medio(self, *args):
			global dificuldade
			dificuldade  = 'medio'
			
			
	def dificil(self, *args):
			global dificuldade
			dificuldade  = 'dificil'
	
	#Preencher os botões
	def on_pre_enter(self, *args):
		global dificuldade, lista_completa, su
		
		su = sudoku()
		sui = sudoku_i(su, dificuldade)
		
		l11 = self.ids.l11
		l12 = self.ids.l12
		l13 = self.ids.l13
		l14 = self.ids.l14
		l15 = self.ids.l15
		l16 = self.ids.l16
		l17 = self.ids.l17
		l18 = self.ids.l18
		l19 = self.ids.l19
		
		l21 = self.ids.l21
		l22 = self.ids.l22
		l23 = self.ids.l23
		l24 = self.ids.l24
		l25 = self.ids.l25
		l26 = self.ids.l26
		l27 = self.ids.l27
		l28 = self.ids.l28
		l29 = self.ids.l29
		
		l31 = self.ids.l31
		l32 = self.ids.l32
		l33 = self.ids.l33
		l34 = self.ids.l34
		l35 = self.ids.l35
		l36 = self.ids.l36
		l37 = self.ids.l37
		l38 = self.ids.l38
		l39 = self.ids.l39
		
		l41 = self.ids.l41
		l42 = self.ids.l42
		l43 = self.ids.l43
		l44 = self.ids.l44
		l45 = self.ids.l45
		l46 = self.ids.l46
		l47 = self.ids.l47
		l48 = self.ids.l48
		l49 = self.ids.l49
		
		l51 = self.ids.l51
		l52 = self.ids.l52
		l53 = self.ids.l53
		l54 = self.ids.l54
		l55 = self.ids.l55
		l56 = self.ids.l56
		l57 = self.ids.l57
		l58 = self.ids.l58
		l59 = self.ids.l59
		
		l61 = self.ids.l61
		l62 = self.ids.l62
		l63 = self.ids.l63
		l64 = self.ids.l64
		l65 = self.ids.l65
		l66 = self.ids.l66
		l67 = self.ids.l67
		l68 = self.ids.l68
		l69 = self.ids.l69
		
		l71 = self.ids.l71
		l72 = self.ids.l72
		l73 = self.ids.l73
		l74 = self.ids.l74
		l75 = self.ids.l75
		l76 = self.ids.l76
		l77 = self.ids.l77
		l78 = self.ids.l78
		l79 = self.ids.l79
		
		l81 = self.ids.l81
		l82 = self.ids.l82
		l83 = self.ids.l83
		l84 = self.ids.l84
		l85 = self.ids.l85
		l86 = self.ids.l86
		l87 = self.ids.l87
		l88 = self.ids.l88
		l89 = self.ids.l89
		
		l91 = self.ids.l91
		l92 = self.ids.l92
		l93 = self.ids.l93
		l94 = self.ids.l94
		l95 = self.ids.l95
		l96 = self.ids.l96
		l97 = self.ids.l97
		l98 = self.ids.l98
		l99 = self.ids.l99
		
		lista_completa = [
		l11, l12, l13, l14, l15, l16, l17, l18, l19, 
		l21, l22, l23, l24, l25, l26, l27, l28, l29, 
		l31, l32, l33, l34, l35, l36, l37, l38, l39, 
		l41, l42, l43, l44, l45, l46, l47, l48, l49, 
		l51, l52, l53, l54, l55, l56, l57, l58, l59, 
		l61, l62, l63, l64, l65, l66, l67, l68, l69, 
		l71, l72, l73, l74, l75, l76, l77, l78, l79, 
		l81, l82, l83, l84, l85, l86, l87, l88, l89, 
		l91, l92, l93, l94, l95, l96, l97, l98, l99
		]

		n1 = 0
		n2 = 0
		#Separando os botões do jogo
		for i in lista_completa:
			i.text = str(sui[n1][n2])
			numero = cint(sui[n1][n2])
			if numero == 0:
				#Botões vazios
				i.group = 'sudo'
			else:
				#Botões já preenchidos
				i.group = 'imutavel'
			
			n2 += 1
			if n2 > 8:
				n1 += 1
				n2 = 0
				
		#Iniciar o tempo
		global s, m, h
		s = m = h = 0
		self.cronometro = Clock.schedule_interval(self.contador, 1)
	

	def on_leave(self, *args):
		#Parar o tempo ao sair
		self.cronometro.cancel()
		self.ids.tempo.text = '00:00:00'
	
	#Cronômetro do jogo
	def contador(self, *args):
		global s, m, h, tempo
		s += 1
		if s >= 59:
			s = 0
			m += 1
			if m >= 59:
				h += 1
				
		if s < 10:
			segundos = '0' + str(s)
		else:
			segundos = str(s)
		if m < 10:
			minutos = '0' + str(m)
		else:
			minutos = str(m)
		if h < 10:
			horas = '0' + str(h)
		else:
			horas = str(h)
		
		tempo = (f'{horas}:{minutos}:{segundos}')
		self.ids.tempo.text = str(tempo)
	
	#Para mudar os números manual
	def mude_n(self, text, *args):
		global lista_completa
		
		for i in lista_completa:
			if i.state == 'down' and i.group == 'sudo':
				i.text=text
				i.color = 0, 0, 0, 1
				
	#Para não ir para o inicio de vez
	def pop_inicio(self, *args):
		box_i = BoxLayout()
		
		i = Popup(
		title='Ir para o início?', 
		content=box_i, 
		size_hint=(None, None), 
		size=('240sp', '95sp'))
		
		def voltar_inicio(self, *args):
			App.get_running_app().root.transition.direction = 'right'
			App.get_running_app().root.current='menu'
			i.dismiss()

		i_sim = Button(
		text='sim', 
		on_release=voltar_inicio)
		
		i_nao = Button(
		text='não', 
		on_release=i.dismiss)
		
		box_i.add_widget(i_sim)
		box_i.add_widget(i_nao)
		
		i.open()
	
	#Para não iniciar um novo jogo de vez
	def pop_novojogo(self, *args):
		boxnj = BoxLayout()
		
		nj = Popup(
		title='Iniciar novo jogo?', 
		content=boxnj, 
		size_hint=(None, None), 
		size=('240sp', '95sp'))

		def novojogo(self, *args):
			App.get_running_app().root.transition.direction = 'right'
			App.get_running_app().root.current='dificuldade'
			nj.dismiss()
		
		nj_sim = Button(
		text='sim', 
		on_release=novojogo)
		
		nj_nao = Button(
		text='não', 
		on_release=nj.dismiss)
		
		boxnj.add_widget(nj_sim)
		boxnj.add_widget(nj_nao)

		nj.open()
		
	#Verificação ao final do jogo
	def verificar(self, *args):
		global su, tempo, nome
		
		l11 = cint(self.ids.l11.text)
		l12 = cint(self.ids.l12.text)
		l13 = cint(self.ids.l13.text)
		l14 = cint(self.ids.l14.text)
		l15 = cint(self.ids.l15.text)
		l16 = cint(self.ids.l16.text)
		l17 = cint(self.ids.l17.text)
		l18 = cint(self.ids.l18.text)	
		l19 = cint(self.ids.l19.text)
			
		l21 = cint(self.ids.l21.text)
		l22 = cint(self.ids.l22.text)
		l23 = cint(self.ids.l23.text)
		l24 = cint(self.ids.l24.text)
		l25 = cint(self.ids.l25.text)
		l26 = cint(self.ids.l26.text)
		l27 = cint(self.ids.l27.text)
		l28 = cint(self.ids.l28.text)
		l29 = cint(self.ids.l29.text)
			
		l31 = cint(self.ids.l31.text)
		l32 = cint(self.ids.l32.text)
		l33 = cint(self.ids.l33.text)
		l34 = cint(self.ids.l34.text)
		l35 = cint(self.ids.l35.text)
		l36 = cint(self.ids.l36.text)
		l37 = cint(self.ids.l37.text)
		l38 = cint(self.ids.l38.text)
		l39 = cint(self.ids.l39.text)
			
		l41 = cint(self.ids.l41.text)
		l42 = cint(self.ids.l42.text)
		l43 = cint(self.ids.l43.text)
		l44 = cint(self.ids.l44.text)
		l45 = cint(self.ids.l45.text)
		l46 = cint(self.ids.l46.text)
		l47 = cint(self.ids.l47.text)
		l48 = cint(self.ids.l48.text)
		l49 = cint(self.ids.l49.text)
			
		l51 = cint(self.ids.l51.text)
		l52 = cint(self.ids.l52.text)
		l53 = cint(self.ids.l53.text)
		l54 = cint(self.ids.l54.text)
		l55 = cint(self.ids.l55.text)
		l56 = cint(self.ids.l56.text)
		l57 = cint(self.ids.l57.text)
		l58 = cint(self.ids.l58.text)
		l59 = cint(self.ids.l59.text)
			
		l61 = cint(self.ids.l61.text)
		l62 = cint(self.ids.l62.text)
		l63 = cint(self.ids.l63.text)
		l64 = cint(self.ids.l64.text)
		l65 = cint(self.ids.l65.text)
		l66 = cint(self.ids.l66.text)
		l67 = cint(self.ids.l67.text)
		l68 = cint(self.ids.l68.text)
		l69 = cint(self.ids.l69.text)
			
		l71 = cint(self.ids.l71.text)
		l72 = cint(self.ids.l72.text)
		l73 = cint(self.ids.l73.text)
		l74 = cint(self.ids.l74.text)
		l75 = cint(self.ids.l75.text)
		l76 = cint(self.ids.l76.text)
		l77 = cint(self.ids.l77.text)
		l78 = cint(self.ids.l78.text)
		l79 = cint(self.ids.l79.text)
			
		l81 = cint(self.ids.l81.text)
		l82 = cint(self.ids.l82.text)
		l83 = cint(self.ids.l83.text)
		l84 = cint(self.ids.l84.text)
		l85 = cint(self.ids.l85.text)
		l86 = cint(self.ids.l86.text)
		l87 = cint(self.ids.l87.text)
		l88 = cint(self.ids.l88.text)
		l89 = cint(self.ids.l89.text)
			
		l91 = cint(self.ids.l91.text)
		l92 = cint(self.ids.l92.text)
		l93 = cint(self.ids.l93.text)
		l94 = cint(self.ids.l94.text)
		l95 = cint(self.ids.l95.text)
		l96 = cint(self.ids.l96.text)
		l97 = cint(self.ids.l97.text)
		l98 = cint(self.ids.l98.text)
		l99 = cint(self.ids.l99.text)
			
		lista_completa = [
		[l11, l12, l13, l14, l15, l16, l17, l18, l19], 
		[l21, l22, l23, l24, l25, l26, l27, l28, l29], 
		[l31, l32, l33, l34, l35, l36, l37, l38, l39], 
		[l41, l42, l43, l44, l45, l46, l47, l48, l49], 
		[l51, l52, l53, l54, l55, l56, l57, l58, l59], 
		[l61, l62, l63, l64, l65, l66, l67, l68, l69], 
		[l71, l72, l73, l74, l75, l76, l77, l78, l79], 
		[l81, l82, l83, l84, l85, l86, l87, l88, l89], 
		[l91, l92, l93, l94, l95, l96, l97, l98, l99]
		]
		
		verificar = verificar_sudoku(lista_completa)
		
		if verificar == True:
			boxvv = BoxLayout(
			orientation='vertical')
		
			vv = Popup(
			title='', 
			content=boxvv, 
			size_hint=(None, None), 
			size=('250sp', '120sp'))
		
			voce_venceu = Label(
			text='VOCÊ VENCEU!!!',
			font_size=30)
			
			tempo_final = Label(
			text=str(tempo))
			
			nome = TextInput(
			text='Seu Nome', 
			size_hint=(3, 1))
			
			bnome = Button(
			text='Enviar', 
			on_release=self.recorde.finalizado,
			on_press=vv.dismiss)
			
			boxnome = BoxLayout()
			
			boxnome.add_widget(nome)
			boxnome.add_widget(bnome)
			boxvv.add_widget(voce_venceu)
			boxvv.add_widget(tempo_final)
			boxvv.add_widget(boxnome)
			
			self.cronometro.cancel()
			vv.open()
		else:
			boxin = BoxLayout(
			orientation='vertical')
			
			vp = Popup(
			title='', 
			content=boxin, 
			size_hint=(None, None), 
			size=('250sp', '120sp'))
			
			incom = Label(
			text='Sudoku Incompleto')
			
			ok = Button(
			text='Ok, continuar', 
			on_release=vp.dismiss)
			
			boxin.add_widget(incom)
			boxin.add_widget(ok)		
			vp.open()
				
#Tela dos recordes incompleta ainda
class Recordes(Screen):
	def __init__(self, **kwargs):
		super(Screen, self).__init__(**kwargs)
		self.lista_jogadores = []
		self.salvos = []
		pass
	
	#Mudando pra tela dos recordes
	def finalizado(self, *args):
			self.inserir_nr()
			App.get_running_app().root.transition.direction = 'left'
			App.get_running_app().root.current='recordes'
	
	#Para inserir um novo recorde
	def inserir_nr(self, *args):
		global tempo, nome
		
		if nome.text == '':
			#Nome padrão
			nome.text = 'Sem Nome'
		
		try:
			#Carregando o Arquivo salvo
			with open('dados.json', 'r') as dados:
				salvos = json.load(dados)
			lista_rank = salvos[0]
			lista_nome = salvos[1]
			lista_tempo = salvos[2]
		except:
			#Valores padrões caso não exusta o arquivo json
			lista_rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
			lista_nome = ['Venis', '', '', '', '', '', '', '', '', '']
			lista_tempo = ['00:04:47', '', '', '', '', '', '', '', '', '']
		
		c = 0 #Comparando o resultado com os recordes
		for i in lista_tempo:
			if i == '':
				ti = 0
			else:
				ti = (int(i[0:2]) * 60 + int(i[3:5])) * 60 + int(i[6:])
				
			t = (int(tempo[0:2]) * 60 + int(tempo[3:5])) * 60 + int(tempo[6:])
				
			if ti == 0:
				lista_nome.insert(c, nome.text)
				lista_tempo.insert(c, tempo)
				if len(lista_tempo) > 10:
					lista_nome.pop()
					lista_tempo.pop()
				break
			elif t < ti:
				lista_nome.insert(c, nome.text)
				lista_tempo.insert(c, tempo)
				if len(lista_tempo) > 10:
					lista_nome.pop()
					lista_tempo.pop()
				break
			c += 1
		
		#Lista de dados dos recordes	
		salvos = [
		lista_rank,
		lista_nome,
		lista_tempo
		]
		self.salvar_dados(salvos)
	
	#Salvando os dados em json
	def salvar_dados(self, salvos, *args):	
		with open('dados.json', 'w') as dados:
			json.dump(salvos, dados)
			
		
	#Carregando os dados nos recordes
	def carregar_dados(self, *args):
		try:
			with open('dados.json', 'r') as dados:
				salvos = json.load(dados)
		except FileNotFoundError:
			lista_rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
			lista_nome = ['Venis', '', '', '', '', '', '', '', '', '']
			lista_tempo = ['00:04:47', '', '', '', '', '', '', '', '', '', '']
			
			salvos = [
			lista_rank,
			lista_nome,
			lista_tempo
			]
			
		#Laço pra criar os box e adicionar os valores
		c = 0
		for jogador in salvos[0]:
			novo_jogador = Bl(
			size_hint=(1, 1))
				
			nova_posicao = Label(
			text=salvos[0][c], 
			font_size=30, 
			size_hint=(0.8, 1),
			color=(0, 0, 0, 1))
				
			nome_jogador = Label(
			text=salvos[1][c], 
			font_size=30, 
			size_hint=(2.2, 1),
			color=(0, 0, 0, 1))
				
			tempo_jogador = Label(
			text=salvos[2][c], 
			font_size=30, 
			size_hint=(1, 1),
			color=(0, 0, 0, 1))
			
			novo_jogador.add_widget(nova_posicao)
			novo_jogador.add_widget(nome_jogador)
			novo_jogador.add_widget(tempo_jogador)
				
			self.ids.rank.add_widget(novo_jogador)
			c += 1			

	#Carregar os recordes na página
	def on_pre_enter(self, *args):
		self.carregar_dados()
		
	#Ao sair da página salvar os recordes
	def  on_leave(self, *args):
		try:
			with open('dados.json', 'r') as dados:
				salvos = json.load(dados)
			self.salvar_dados(salvos)
		except:
			pass
		self.ids.rank.clear_widgets()
		
#BoxLayout com um canvas cinza
class Bl(BoxLayout):
	def __init__(self, **kwargs):
		super(Bl, self).__init__(**kwargs)
		self.atualizar()
	
	#Ao mudar de posição
	def on_pos(self, *args):
		self.atualizar()
		
	#Ao mudar de tamanho	
	def on_size(self, *args):
		self.atualizar()
	
	#Atualizar o canvas na tela
	def atualizar(self, *args):
		self.canvas.before.clear()
		with self.canvas.before:
			Color(rgba=(0.5, 0.5, 0.5, 1))
			
			Rectangle(
			size=(self.width, self.height), 
			pos=(self.x, self.y))
		
				
class Jogo(App):
	def build(self):
		return Ukivy()
		
Jogo().run()
