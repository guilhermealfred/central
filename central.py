# -*- coding: utf-8 -*-s
from bs4 import BeautifulSoup as bs
from functools import partial
from tkinter import *
from PIL import Image
from datetime import datetime
import os
import urllib.request
import sqlite3
class central:
	def __init__(self):
		self.main = Tk()
		self.main.geometry('400x400+500+200')
		self.main.resizable(False,False)
		self.main.title('Login')
		self.main['bg'] = '#4c4c4c'
		self.frame1 = Frame(self.main)
		self.frame1.pack()

		self.frame2 = Frame(self.main)
		self.frame2.pack()

		self.frame3 = Frame(self.main)
		self.frame3.pack()

		self.frame4 = Frame(self.main)
		self.frame4.pack()

		self.frame5 = Frame(self.main)
		self.frame5.pack()

		self.frame6 = Frame(self.main)
		self.frame6.pack()

		self.userimg = PhotoImage(file='user.gif')
		self.lbuser = Label(self.frame1,image=self.userimg,bg='#4c4c4c')
		self.lbuser.pack()

		self.user = Entry(self.frame2)
		self.user.pack()

		self.passwordimg = PhotoImage(file='pass.gif')
		self.lbpassword = Label(self.frame3,image=self.passwordimg,bg='#4c4c4c',pady= 10)
		self.lbpassword.pack()

		self.password = Entry(self.frame4,show='*')
		self.password.pack()
		self.botaoimg = PhotoImage(file='login.gif')
		self.botao = Button(self.frame5,image=self.botaoimg,command=self.verify,bg='#4c4c4c')
		self.botao.pack()
		self.result = Label(self.frame6,text='',bg='#4c4c4c')
		self.result.pack()

		self.main.mainloop()
	def verify(self):
		if len(self.user.get()) > 0 and len(self.password.get()) > 0:
			if self.user.get() == 'ghostalfredo' and self.password.get() == '123456':
				self.main.destroy()
				options()
			else:
				self.result.pack()
				self.result['text'] = 'Acesso negado'
				self.result['fg'] = 'red'
				self.result['font'] = font=('Ubuntu Condensed',12)
		else:
			self.result['text'] = 'Preencha todos os campos'
			self.result['fg'] = 'red'
			self.result['font'] = font=('Ubuntu Condensed',12)
class options(object):
	def __init__(self):
		self.tela = Tk()
		self.tela.resizable(False,False)
		self.tela.title('Tools')
		self.option = Label(self.tela,text='Bem vindo meu senhor. Qual ferramenta quer usar? ',font=('Ubuntu Condensed',15),fg='#4c4c4c')
		self.option.pack()
		self.frame1 = Frame(self.tela)
		self.frame1.pack()
		self.bt1 = Button(self.frame1,text='Scraping Twitter',width=50,height=3,command=self.scraping)
		self.bt1.pack()
		self.bt2 = Button(self.frame1,text='Agenda',width=50,height=3,command=self.agenda)
		self.bt2.pack()
		self.tela.mainloop()
	def scraping(self):
		self.tela.destroy()
		scraping()
	def agenda(self):
		self.tela.destroy()
		agenda()
class scraping(object):
	def __init__(self):
		self.tela = Tk()
		self.tela.title('Scraping Twitter')
		self.tela.geometry('400x400+400+200')
		self.tela.resizable(False,False)
		self.tela['bg'] = '#61f2cf'
		self.framelink = Frame(self.tela)
		self.framelink.pack()
		self.alert = Label(self.tela,fg='red',bg='#61f2cf',font=('Ubuntu Condensed',12))
		self.alert.pack()
		self.lblink = Label(self.framelink,text='Link',font=('Ubuntu Condensed',12),padx = 25)
		self.lblink.pack(side=LEFT)
		self.frameimg = Frame(self.tela,pady = 10,bg='#61f2cf')
		self.frameimg.pack()
		self.link = Entry(self.framelink,width=40)
		self.link.focus_force()
		self.link.insert(END,'https://twitter.com/')
		self.link.bind('<Return>',self.handle)
		self.link.pack(side=LEFT)
		self.tela.mainloop()
	@property
	def get_tweets(self):
		try:
			self.tweets = self.soup.find('a',class_="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav")
			return self.tweets.get('title')
		except:
			return 'Não tem nenhum tweet'
	@property
	def get_following(self):
		try:
			self.fl = self.soup.find('li',class_='ProfileNav-item ProfileNav-item--following')
			self.following = self.fl.find('a',class_="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor").get('title').split()
			return str(self.following[1].replace('s','S')) + ' ' + str(self.following[0]) + ' pessoas'
		except:
			return 'Não segue nenhum perfil'
	@property 
	def get_followers(self):
		try:
			self.flo = self.soup.find('li',class_='ProfileNav-item ProfileNav-item--followers')
			self.followers = self.flo.find('a',class_="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor").get('title')
			return self.followers
		except:
			return 'Não possui seguidores'
	@property
	def get_photos(self):
		try:
			self.ph = self.soup.find('a',class_='PhotoRail-headingWithCount js-nav')
			if self.ph.text.strip() == '0 Foto ou vídeo':
				return 'Não possui fotos/vídeos'
			return ' '* 15 + self.ph.text.lstrip()
		except:
			pass
	def handle(self,event):
		try:
			self.site = urllib.request.urlopen(self.link.get()).read()
			self.soup = bs(self.site,'lxml')
			try:
				if self.soup.find('input',value="app/pages/profile/highline_landing") != None:
					self.download()
				else:
					raise	
			except:
				raise 
		except Exception as e:
			self.alert['text'] = 'Perfil Inválido!.Formato de entrada : https://twitter.com/perfil'
			print(e)
	def download(self):
		try:
			img = self.soup.find('img',class_='ProfileAvatar-image ').get('src')
			urllib.request.urlretrieve(img,'img.png')
		except:
			urllib.request.urlretrieve('https://abs.twimg.com/a/1527200258/img/t1/highline/empty_state/owner_empty_avatar.png','img.png')
		finally:
			self.handle_image()
	def handle_image(self):
		image = Image.open('img.png')
		new_img = image.resize((150,150))
		new_img.save('perfil.gif')
		self.photo = PhotoImage(file='perfil.gif')
		self.save = self.photo
		self.organize()
	def organize(self):
		self.alert.pack_forget()
		self.lblink.pack_forget()
		self.link.pack_forget()
		self.framelink.pack_forget()
		self.tela.title(f'Perfil-@{self.soup.find("b",class_="u-linkComplex-target").text}')
		self.lb = Label(self.frameimg,image=self.photo,bg='#61f2cf')
		self.lb.pack()
		os.system('rm img.png')
		os.system('rm perfil.gif')
		self.frameinfo = Frame(self.tela,bg='#61f2cf')
		self.frameinfo.pack()

		lista = [self.get_following,self.get_followers,self.get_photos,self.get_tweets]
		for i in lista:
			self.lbi = Label(self.frameinfo,text=i,font=('Ubuntu Condensed',12),fg='#4c4c4c',bg='#61f2cf')
			self.lbi.pack()
		self.framebt = Frame(self.tela,pady=30,bg='#61f2cf')
		self.framebt.pack(side=BOTTOM)
		self.again = Button(self.framebt,text='Scrapar denovo',width=13,bg='#61f2cf',borderwidth=0,command=partial(actions,self.tela,scraping),font=('Ubuntu Condensed',12),fg='black')
		self.again.pack(side=LEFT)

		self.backtocentral = Button(self.framebt,width=13,bg='#61f2cf',text='Voltar pra central',borderwidth=0,command=partial(actions,self.tela,options),font=('Ubuntu Condensed',12),fg='black')
		self.backtocentral.pack(side=LEFT)
def actions(tela,classe):
	tela.destroy()
	classe()
class agenda:
	def __init__(self):
		self.tela = Tk()
		#self.tela.geometry('500x330+400+200')
		self.tela.resizable(False,False)
		self.tela.title('Agenda')
		self.tela['bg'] = '#4c4c4c'
		self.connect = sqlite3.connect('agenda.db')
		self.cursor = self.connect.cursor()
		self.cursor.execute('CREATE TABLE IF NOT EXISTS dados (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,data text,tipo text, materia text,desc text)')
		self.cursor.execute('SELECT * FROM dados')
		if len(self.cursor.fetchall()) < 1:
			self.tela.geometry('500x330+400+200')
			self.aviso = Label(text='Nenhuma tarefa foi registrada',bg='#4c4c4c',font=("Ubuntu Condensed",30),fg='red')
			self.aviso.pack()
			self.adicionar = Button(text='Adicionar',command=self.add,bg='#4c4c4c')
			self.adicionar.pack()
		else:
			self.frame = Frame(self.tela,bg='#4c4c4c')
			self.frame.pack()
			self.cursor.execute('SELECT * FROM dados ORDER by data')
			for e,i in enumerate(self.cursor.fetchall()):
				data = datetime.strptime('%s'%(i[1]),'%d/%m/%Y')
				if data < datetime.today():
					self.cursor.execute("DELETE FROM dados WHERE id= %d"%(i[0]))
					self.connect.commit()
				if e % 3 == 0:
					frame = Frame(self.tela)
					frame.pack()
				texto = '%s\n%s\n%s'%(i[3],i[2],i[1])
				bt = Button(frame,text=texto,font=("Ubuntu Condensed",20),width=10,command=partial(self.read_and_show,i[0]))
				bt.pack(side=LEFT)
		self.menu = Menu(self.tela,tearoff=0)
		self.tool_menu = Menu(self.menu,tearoff=0)
		self.help_menu = Menu(self.menu,tearoff=0)
		self.tool_menu.add_command(label='  Adicionar',command=self.add,font=('Ubuntu Condensed',12))
		self.tool_menu.add_command(label='  Ir pra central',command=partial(actions,self.tela,options),font=('Ubuntu Condensed',12))
		self.menu.add_cascade(label='Ações',font=('Ubuntu Condensed',12),menu=self.tool_menu)
		self.menu.add_cascade(label='Ajuda',font=('Ubuntu Condensed',12),menu=self.help_menu)
		self.help_menu.add_command(label='  Sobre...',command=self.sobre,font=('Ubuntu Condensed',12))
		self.tela.configure(menu=self.menu)
		self.tela.mainloop()
	def sobre(self):
		self.sobretela = Tk()
		self.sobretela.title('Agenda- Sobre')
		self.sobretela.resizable(False,False)
		self.sobretela.geometry('305x100+500+250')
		self.lb = Label(self.sobretela,fg='#00689d',text='Criado por : Guilherme Alfredo\n Github: https://github.com/guilhermealfred/\n Discord : Guilherme Alfredo#1690',font=('Trebuchet MS',11))
		self.lb.pack()
		self.sobretela.mainloop()
	def read_and_show(self,id):
		self.cursor.execute('SELECT * FROM dados WHERE id = %d'%id)
		self.h = Tk()
		#self.h.geometry('300x100+600+250')
		s = [(i[1],i[2],i[3],i[4]) for i in self.cursor.fetchall()]
		self.h.title(f'{s[0][1]}-{s[0][0]}-')
		hora = str(datetime.strptime(s[0][0],'%d/%m/%Y')-datetime.today()).replace('days','dias')
		lb = Label(self.h,text='%s de %s\n%s\nFaltam: %s'%(s[0][1],s[0][2],s[0][3],hora[0:hora.find('.')]))
		lb.pack()
		self.h.mainloop()
	def add(self):
		self.tela.destroy()
		self.addscreen = Tk()
		self.addscreen.resizable(False,False)
		self.addscreen.title('Agenda- Adicionar')
		self.addscreen.geometry('300x250+500+200')

		self.data = Label(text='Data: ')
		self.data.pack()

		self.dataentry = Entry(self.addscreen,width=30)
		self.dataentry.pack()

		self.tipoatv_on = False
		self.tipopes_on = False
		self.tipoatrabalho_on = False

		self.materia = Label(text='Materia: ')
		self.materia.pack()
		self.matentry = Entry(self.addscreen,width=30)
		self.matentry.pack()

		self.desclb = Label(text='Descrição: ')
		self.desc = Entry(self.addscreen,width=30)
		self.desclb.pack()
		self.desc.pack()

		self.tipoframe = Frame(self.addscreen,pady=20)
		self.tipoframe.pack()

		self.tipoatv = Checkbutton(self.tipoframe,text='Atividade',command=self.controlatv)
		self.tipopes = Checkbutton(self.tipoframe,text='Pesquisa',command=self.controles)
		self.tipotrabalho = Checkbutton(self.tipoframe,text='Trabalho',command=self.controltra)

		self.tipoatv.pack(side=LEFT)
		self.tipopes.pack(side=LEFT)
		self.tipotrabalho.pack(side=LEFT)

		self.lbaviso = Label(self.addscreen,text='',fg='red',pady=0)
		self.lbaviso.pack()

		self.backbt = Button(text='Voltar',command=lambda:self.back(),borderwidth=0,padx=60)
		self.backbt.pack(side=LEFT)

		self.sendbutton = Button(text='Salvar',command=lambda:self.handle_entrys(),borderwidth=0,fg='green',pady=2,padx=60)
		self.sendbutton.pack(side=LEFT)

		self.addscreen.mainloop()
	def back(self):
		self.addscreen.destroy()
		agenda()
	def controlatv(self):
		self.tipoatv_on = not self.tipoatv_on
		if self.tipopes_on:
			self.tipopes.deselect()
			self.tipopes_on = False
		if self.tipoatrabalho_on:
			self.tipotrabalho.deselect()
			self.tipoatrabalho_on = False
		return 'Atividade'
	def controles(self):
		self.tipopes_on = not self.tipopes_on
		if self.tipoatv_on:
			self.tipoatv.deselect()
			self.tipoatv_on = False
		if self.tipoatrabalho_on:
			self.tipotrabalho.deselect()
			self.tipoatrabalho_on = False
		return 'Pesquisa'
	def controltra(self):
		self.tipoatrabalho_on = not self.tipoatrabalho_on
		if self.tipoatv_on:
			self.tipoatv.deselect()
			self.tipoatv_on = False
		if self.tipopes_on:
			self.tipopes.deselect()
			self.tipopes_on = False
		return 'Trabalho'
		
	def handle_entrys(self):
		try:
			x = datetime.strptime(self.dataentry.get(),'%d/%m/%Y')
			if x >= datetime.today() and len(self.matentry.get()) > 0 and len(self.desc.get())>0 and self.check() != False:
				self.adiciona(x.strftime('%d/%m/%Y'),self.check(),self.matentry.get(),self.desc.get())
				print(type(self.check()),type(x.strftime('%d/%m/%Y')))
				return True
			print(type(self.check()))
			raise
		except Exception as e:
			self.lbaviso['text'] = 'Preencha os campos corretamente'
			self.lbaviso['fg'] = 'red'
			print(e)

	def check(self):
		if self.tipoatv_on:
			return 'Atividade'
		elif self.tipopes_on:
			return 'Pesquisa'
		elif self.tipoatrabalho_on:
			return 'Trabalho'
		else:
			return False
	def adiciona(self,data,tipo,materia,desc):
		sql = """
		INSERT INTO dados(data,tipo,materia,desc) VALUES(?,?,?,?)
		"""
		self.cursor.execute(sql,(data,tipo,materia,desc))
		self.connect.commit()
		self.lbaviso['text'] = 'Item adicionado!'
		self.lbaviso['fg'] = 'green'
			
if __name__=="__main__":
	central()