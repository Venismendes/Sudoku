from Sudoku import sudoku, sudoku_i, verificar_sudoku
from c_int import cint
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

# Variáveis globais, que serão usadas em várias classes e funções diferentes
dificuldade = nome = ''
lista_completa = su = []
s = m = h = 0
tempo = '00:00:00'


# =========================================== Gerenciador das telas ===============================================
class Ukivy(ScreenManager):
    pass


# =============================================== Menu principal ==================================================
class Menu(Screen):
    pass


# ============================================ Dificuldade do jogo ================================================
class Dificuldade(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        pass
        self.novojogo = Novo_jogo()

    pass


# ================================================ Tela do Jogo ===================================================
class Novo_jogo(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.cronometro = 0
        pass
        self.recorde = Recordes()

    def facil(self, *args):
        global dificuldade
        dificuldade = 'facil'

    def medio(self, *args):
        global dificuldade
        dificuldade = 'medio'

    def dificil(self, *args):
        global dificuldade
        dificuldade = 'dificil'

    # Preencher os botões
    def on_pre_enter(self, *args):
        global dificuldade, lista_completa, su

        su = sudoku()
        sui = sudoku_i(su, dificuldade)

        lista_ids = self.ids.keys()
        lista_completa = []
        for i in lista_ids:
            if i[0] == 'l':
                lista_completa.append(i)

        n1 = 0
        n2 = 0
        # Separando os botões do jogo
        for i in lista_completa:
            self.ids[i].text = str(sui[n1][n2])
            numero = cint(sui[n1][n2])

            if numero == 0:
                # Botões vazios
                self.ids[i].group = 'sudo'
                self.ids[i].state = 'normal'
                self.ids[i].disabled = False
                self.ids[i].background_normal = 'images/toggle_normal.png'
                self.ids[i].background_down = 'images/toggle_down.png'
                self.ids[i].color = 0.913, 0.945, 0.968, 1
            else:
                # Botões já preenchidos
                self.ids[i].group = 'imutavel'
                self.ids[i].state = 'normal'
                self.ids[i].disabled = True
                self.ids[i].background_disabled_normal = 'images/toggle_normal.png'
                self.ids[i].color = 0.513, 0.545, 0.568, 1

            n2 += 1
            if n2 > 8:
                n1 += 1
                n2 = 0

        # Iniciar o tempo
        global s, m, h
        s = m = h = 0
        self.cronometro = Clock.schedule_interval(self.contador, 1)

    def on_leave(self, *args):
        # Parar o tempo ao sair
        self.cronometro.cancel()
        self.ids.tempo.text = '00:00:00'

    # Cronômetro do jogo
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

    # Para mudar os números manual
    def mude_n(self, text, *args):
        global lista_completa

        for i in lista_completa:
            if self.ids[i].state == 'down' and self.ids[i].group == 'sudo':
                self.ids[i].color = 0.913, 0.945, 0.968, 1
                self.ids[i].text = text

    # Para não ir para o inicio de vez
    def pop_inicio(self, *args):
        box_i = BoxLayout()

        i = Popup(
            title='Ir para o início?',
            background_color=(0.133, 0.454, 0.647, 1),
            content=box_i,
            size_hint=(None, None),
            size=('240sp', '95sp'))

        def voltar_inicio(self, *args):
            App.get_running_app().root.transition.direction = 'right'
            App.get_running_app().root.current = 'menu'
            i.dismiss()

        i_sim = Button(
            text='sim',
            color=(0.913, 0.945, 0.968, 1),
            background_color=(0.133, 0.454, 0.647, 1),
            on_release=voltar_inicio)

        i_nao = Button(
            text='não',
            color=(0.913, 0.945, 0.968, 1),
            background_color=(0.133, 0.454, 0.647, 1),
            on_release=i.dismiss)

        box_i.add_widget(i_sim)
        box_i.add_widget(i_nao)

        i.open()

    # Para não iniciar um novo jogo de vez
    def pop_novojogo(self, *args):
        boxnj = BoxLayout()

        nj = Popup(
            title='Iniciar novo jogo?',
            background_color=(0.133, 0.454, 0.647, 1),
            content=boxnj,
            size_hint=(None, None),
            size=('240sp', '95sp'))

        def novojogo(self, *args):
            App.get_running_app().root.transition.direction = 'right'
            App.get_running_app().root.current = 'dificuldade'
            nj.dismiss()

        nj_sim = Button(
            text='sim',
            color=(0.913, 0.945, 0.968, 1),
            background_color=(0.133, 0.454, 0.647, 1),
            on_release=novojogo)

        nj_nao = Button(
            text='não',
            color=(0.913, 0.945, 0.968, 1),
            background_color=(0.133, 0.454, 0.647, 1),
            on_release=nj.dismiss)

        boxnj.add_widget(nj_sim)
        boxnj.add_widget(nj_nao)

        nj.open()

    # verificar tamanho do nome
    def verificar_nome(self, *args):
        if len(nome.text) <= 11:
            self.recorde.finalizado()
            self.vv.dismiss()

    # Verificação ao final do jogo
    def verificar(self, *args):
        global su, tempo, nome

        # Lista de ids dos ToggleButtons
        lista_ids = self.ids.keys()
        lista_ids2 = []
        for i in lista_ids:
            if i[0] == 'l':
                tg = cint(self.ids[i].text)
                lista_ids2.append(tg)

        # Armazenando para verificar
        lista_completa = [
            lista_ids2[0:9],
            lista_ids2[9:18],
            lista_ids2[18:27],
            lista_ids2[27:36],
            lista_ids2[36:45],
            lista_ids2[45:54],
            lista_ids2[54:63],
            lista_ids2[63:72],
            lista_ids2[72:81]]

        verificar = verificar_sudoku(lista_completa)

        if verificar == True:
            boxvv = BoxLayout(
                orientation='vertical')

            self.vv = Popup(
                title='',
                background_color=(0.133, 0.454, 0.647, 1),
                content=boxvv,
                size_hint=(None, None),
                size=('250sp', '120sp'))

            voce_venceu = Label(
                text='VOCÊ VENCEU!!!',
                color=(0.913, 0.945, 0.968, 1),
                font_size=25)

            tempo_final = Label(
                color=(0.913, 0.945, 0.968, 1),
                text=str(tempo))

            nome = TextInput(
                text='Seu Nome',
                size_hint=(3, 1.2),
                multiline=False)

            bnome = Button(
                text='Enviar',
                color=(0.913, 0.945, 0.968, 1),
                background_color=(0.133, 0.454, 0.647, 1),
                on_release=self.verificar_nome)

            boxnome = BoxLayout()

            boxnome.add_widget(nome)
            boxnome.add_widget(bnome)
            boxvv.add_widget(voce_venceu)
            boxvv.add_widget(tempo_final)
            boxvv.add_widget(boxnome)

            self.cronometro.cancel()
            self.vv.open()
        else:
            boxin = BoxLayout(
                orientation='vertical')

            vp = Popup(
                title='',
                background_color=(0.133, 0.454, 0.647, 1),
                content=boxin,
                size_hint=(None, None),
                size=('250sp', '120sp'))

            incom = Label(
                text='Sudoku Incompleto',
                color=(0.913, 0.945, 0.968, 1))

            ok = Button(
                text='Ok, continuar',
                color=(0.913, 0.945, 0.968, 1),
                background_color=(0.133, 0.454, 0.647, 1),
                on_release=vp.dismiss)

            boxin.add_widget(incom)
            boxin.add_widget(ok)
            vp.open()


# ================================================== Recordes =====================================================
class Recordes(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.lista_jogadores = []
        self.salvos = []
        pass

    # Mudando pra tela dos recordes
    def finalizado(self, *args):
        global dificuldade
        self.inserir_nr()
        App.get_running_app().root.transition.direction = 'left'

        if dificuldade == 'facil':
            App.get_running_app().root.current = 'recordes_facil'
        elif dificuldade == 'medio':
            App.get_running_app().root.current = 'recordes_medio'
        elif dificuldade == 'dificil':
            App.get_running_app().root.current = 'recordes_dificil'

    # Para inserir um novo recorde
    def inserir_nr(self, *args):
        global tempo, nome, dificuldade

        if nome.text == '':
            # Nome padrão
            nome.text = 'Sem Nome'

        try:
            if dificuldade == 'facil':
                # Carregando recordes facil
                with open('dados.json', 'r') as dados:
                    salvos = json.load(dados)
            elif dificuldade == 'medio':
                # Carregando recordes medio
                with open('dados2.json', 'r') as dados:
                    salvos = json.load(dados)
            elif dificuldade == 'dificil':
                # Carregando recordes dificil
                with open('dados3.json', 'r') as dados:
                    salvos = json.load(dados)

            lista_rank = salvos[0]
            lista_nome = salvos[1]
            lista_tempo = salvos[2]
        except:
            # Valores padrões caso não exista o arquivo json
            if dificuldade == 'facil':
                lista_rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                lista_nome = ['Venis', '', '', '', '', '', '', '', '', '']
                lista_tempo = ['00:04:47', '', '', '', '', '', '', '', '', '']
            elif dificuldade == 'medio':
                lista_rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                lista_nome = ['Venis', '', '', '', '', '', '', '', '', '']
                lista_tempo = ['00:08:54', '', '', '', '', '', '', '', '', '']
            elif dificuldade == 'dificil':
                lista_rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                lista_nome = ['Venis', '', '', '', '', '', '', '', '', '']
                lista_tempo = ['00:13:23', '', '', '', '', '', '', '', '', '']

        c = 0  # Comparando o resultado com os recordes
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

        # Lista de dados dos recordes
        salvos = [
            lista_rank,
            lista_nome,
            lista_tempo
        ]
        self.salvar_dados(salvos)

    # Salvando os dados em json
    def salvar_dados(self, salvos, *args):
        if dificuldade == 'facil':
            with open('dados.json', 'w') as dados:
                json.dump(salvos, dados)
        elif dificuldade == 'medio':
            with open('dados2.json', 'w') as dados:
                json.dump(salvos, dados)
        elif dificuldade == 'dificil':
            with open('dados3.json', 'w') as dados:
                json.dump(salvos, dados)

    # Carregando os dados nos recordes
    pass


# =================================================================================================================
class Recordes_facil(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        pass
        self.cr = Recordes()

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
        # Laço pra criar os box e adicionar os valores
        c = 0
        for jogador in salvos[0]:
            novo_jogador = Bl(
                size_hint=(1, 1))

            nova_posicao = Label(
                text=salvos[0][c],
                font_size=25,
                size_hint=(0.8, 1),
                color=(0.913, 0.945, 0.968, 1))

            nome_jogador = Label(
                text=salvos[1][c],
                font_size=25,
                size_hint=(1.8, 1),
                color=(0.913, 0.945, 0.968, 1))

            tempo_jogador = Label(
                text=salvos[2][c],
                font_size=25,
                size_hint=(1.2, 1),
                color=(0.913, 0.945, 0.968, 1))

            novo_jogador.add_widget(nova_posicao)
            novo_jogador.add_widget(nome_jogador)
            novo_jogador.add_widget(tempo_jogador)

            self.ids.rank.add_widget(novo_jogador)
            c += 1

    # Carregar os recordes na página
    def on_pre_enter(self, *args):
        global dificuldade
        dificuldade = 'facil'
        self.carregar_dados()

    # Ao sair da página salvar os recordes
    def on_leave(self, *args):
        try:
            with open('dados.json', 'r') as dados:
                salvos = json.load(dados)
            self.cr.salvar_dados(salvos)
        except:
            pass
        self.ids.rank.clear_widgets()

    pass


# =================================================================================================================
class Recordes_medio(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        pass
        self.cr = Recordes()

    def carregar_dados(self, *args):
        global dificuldade
        try:
            with open('dados2.json', 'r') as dados:
                salvos = json.load(dados)
        except FileNotFoundError:
            lista_rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            lista_nome = ['Venis', '', '', '', '', '', '', '', '', '']
            lista_tempo = ['00:08:54', '', '', '', '', '', '', '', '', '', '']

            salvos = [
                lista_rank,
                lista_nome,
                lista_tempo
            ]

        # Laço pra criar os box e adicionar os valores
        c = 0
        for jogador in salvos[0]:
            novo_jogador = Bl(
                size_hint=(1, 1))

            nova_posicao = Label(
                text=salvos[0][c],
                font_size=25,
                size_hint=(0.8, 1),
                color=(0.913, 0.945, 0.968, 1))

            nome_jogador = Label(
                text=salvos[1][c],
                font_size=25,
                size_hint=(1.8, 1),
                color=(0.913, 0.945, 0.968, 1))

            tempo_jogador = Label(
                text=salvos[2][c],
                font_size=25,
                size_hint=(1.2, 1),
                color=(0.913, 0.945, 0.968, 1))

            novo_jogador.add_widget(nova_posicao)
            novo_jogador.add_widget(nome_jogador)
            novo_jogador.add_widget(tempo_jogador)

            self.ids.rank.add_widget(novo_jogador)
            c += 1

    # Carregar os recordes na página
    def on_pre_enter(self, *args):
        global dificuldade
        dificuldade = 'medio'
        self.carregar_dados()

    # Ao sair da página salvar os recordes
    def on_leave(self, *args):
        try:
            with open('dados2.json', 'r') as dados:
                salvos = json.load(dados)
            self.cr.salvar_dados(salvos)
        except:
            pass
        self.ids.rank.clear_widgets()

    pass


# =================================================================================================================
class Recordes_dificil(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        pass
        self.cr = Recordes()

    def carregar_dados(self, *args):
        global dificuldade

        try:
            with open('dados3.json', 'r') as dados:
                salvos = json.load(dados)
        except FileNotFoundError:
            lista_rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            lista_nome = ['Venis', '', '', '', '', '', '', '', '', '']
            lista_tempo = ['00:13:23', '', '', '', '', '', '', '', '', '', '']

            salvos = [
                lista_rank,
                lista_nome,
                lista_tempo
            ]

        # Laço pra criar os box e adicionar os valores
        c = 0
        for jogador in salvos[0]:
            novo_jogador = Bl(
                size_hint=(1, 1))

            nova_posicao = Label(
                text=salvos[0][c],
                font_size=25,
                size_hint=(0.8, 1),
                color=(0.913, 0.945, 0.968, 1))

            nome_jogador = Label(
                text=salvos[1][c],
                font_size=25,
                size_hint=(1.8, 1),
                color=(0.913, 0.945, 0.968, 1))

            tempo_jogador = Label(
                text=salvos[2][c],
                font_size=25,
                size_hint=(1.2, 1),
                color=(0.913, 0.945, 0.968, 1))

            novo_jogador.add_widget(nova_posicao)
            novo_jogador.add_widget(nome_jogador)
            novo_jogador.add_widget(tempo_jogador)

            self.ids.rank.add_widget(novo_jogador)
            c += 1

    # Carregar os recordes na página
    def on_pre_enter(self, *args):
        global dificuldade
        dificuldade = 'dificil'
        self.carregar_dados()

    # Ao sair da página salvar os recordes
    def on_leave(self, *args):
        try:
            with open('dados3.json', 'r') as dados:
                salvos = json.load(dados)
            self.cr.salvar_dados(salvos)
        except:
            pass
        self.ids.rank.clear_widgets()

    pass


# ========================================= BoxLayout com canvas cinza ============================================
class Bl(BoxLayout):
    def __init__(self, **kwargs):
        super(Bl, self).__init__(**kwargs)
        self.atualizar()

    # Ao mudar de posição
    def on_pos(self, *args):
        self.atualizar()

    # Ao mudar de tamanho
    def on_size(self, *args):
        self.atualizar()

    # Atualizar o canvas na tela
    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(0.133, 0.454, 0.647, 1))

            Rectangle(
                size=(self.width, self.height),
                pos=(self.x, self.y))


# ============================================= Classe principal ==================================================
class Jogo(App):
    def build(self):
        self.icon = 'images/sudoku.png'
        return Ukivy()


Jogo().run()
