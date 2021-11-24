from pygame import *
from luu_diem import *
from nut import *

yellow=(255,255,0) 
black=(0,0,0)	
blue=(0,0,102)

class cua_so():
	def __init__(self):
		init()
		self.screen = display.set_mode((600, 500))
		self.screen.fill(blue)

		draw.rect(self.screen,yellow,(10,10,70,40))
		draw.rect(self.screen,yellow,(100,10,70,40))
		draw.rect(self.screen,yellow,(190,10,70,40))
		draw.rect(self.screen,yellow,(280,10,110,40))
		draw.rect(self.screen,yellow,(450,10,100,40))

		de = font.SysFont('calibri',20).render('DỄ',True,black)
		vua = font.SysFont('calibri',20).render('VỪA',True,black)
		kho = font.SysFont('calibri',20).render('KHÓ',True,black)
		tuychon = font.SysFont('calibri',20).render('TÙY CHỌN',True,black)
		thoat = font.SysFont('calibri',20).render('THOÁT',True,black)

		self.screen.blit(de,(33,18))
		self.screen.blit(vua,(115,20))
		self.screen.blit(kho,(205,20))
		self.screen.blit(tuychon,(290,20))
		self.screen.blit(thoat,(470,20))
		display.update()


	def In_de_kho(self,Bang):
		yellow = (255,255,0) 
		black = (0,0,0)
		ten = font.SysFont('calibri',20).render('Tên người chơi',True,black)
		top = font.SysFont('calibri',20).render('Top',True,black)
		thoigian = font.SysFont('calibri',20).render('Thời gian',True,black)
		draw.rect(self.screen,yellow,(10,60,580,430))
		self.screen.blit(top,(50,70))
		self.screen.blit(thoigian,(140,70))
		self.screen.blit(ten,(250,70))
		index = 0
		y_cord = 90
		for key in Bang.keys():
			thanhtich = font.SysFont('calibri',20).render(str(index + 1),True,black)
			self.screen.blit(thanhtich,(50,y_cord))
			thanhtich = font.SysFont('calibri',20).render(str(Bang[key]),True,black)
			self.screen.blit(thanhtich,(160,y_cord))
			thanhtich = font.SysFont('calibri',20).render(key,True,black)
			self.screen.blit(thanhtich,(270,y_cord))
			y_cord += 20
			index += 1
			if index >= 10:
				break
		display.update()

	def In_tuy_chon(self,Bang):
		yellow = (255,255,0) 
		black = (0,0,0)
		top = font.SysFont('calibri',20).render('Top',True,black)
		thoigian = font.SysFont('calibri',20).render('Thời gian',True,black)
		dorongbang = font.SysFont('calibri',20).render('Độ rộng bảng',True,black)
		sof0 = font.SysFont('calibri',20).render('Số F0',True,black)
		sof0max = font.SysFont('calibri',20).render('Số F0 max',True,black)
		ten = font.SysFont('calibri',20).render('Tên người chơi',True,black)
		draw.rect(self.screen,yellow,(10,60,580,430))
		self.screen.blit(thoigian,(20,70))
		self.screen.blit(dorongbang,(120,70))
		self.screen.blit(sof0,(255,70))
		self.screen.blit(sof0max,(330,70))
		self.screen.blit(ten,(445,70))
		index = 0
		y_cord = 90
		for key in Bang.keys():
			thanhtich = font.SysFont('calibri',20).render(str(Bang[key][0]),True,black)
			self.screen.blit(thanhtich,(25,y_cord))
			thanhtich = font.SysFont('calibri',20).render(str(Bang[key][1]),True,black)
			self.screen.blit(thanhtich,(120,y_cord))
			thanhtich = font.SysFont('calibri',20).render(str(Bang[key][2]),True,black)
			self.screen.blit(thanhtich,(255,y_cord))
			thanhtich = font.SysFont('calibri',20).render(str(Bang[key][3]),True,black)
			self.screen.blit(thanhtich,(330,y_cord))
			thanhtich = font.SysFont('calibri',20).render(key,True,black)
			self.screen.blit(thanhtich,(445,y_cord))
			y_cord += 20
			index +=1
			if index >= 10:
				break
		display.update()

class Bang_xep_hang():
	def __init__(self):
		self.Bang_xep_hang_de = {}
		self.Bang_xep_hang_bthuong = {}
		self.Bang_xep_hang_kho = {}
		self.Bang_xep_hang_tuy_chon = {}

	def Lay_du_lieu(self,filename,Bang): #Lay du lieu tu file
		try:
			with open(filename,'r') as rf:
				line = rf.readline()
				line = line.replace('\n','')
				linesplit = line.split()
				while line:
					Bang[linesplit[0]] = int(linesplit[1])
					line = rf.readline()
					line = line.replace('\n','')
					linesplit = line.split()
		except FileNotFoundError:
			rf = open(filename,'w') 
			rf.close()

	def Lay_du_lieu_all(self):  #Lay du lieu cho cac bang xep hang de, binh thuong, kho
		self.Lay_du_lieu('Data/Bang_xep_hang_de.txt',self.Bang_xep_hang_de)
		self.Lay_du_lieu('Data/Bang_xep_hang_bthuong.txt',self.Bang_xep_hang_bthuong)
		self.Lay_du_lieu('Data/Bang_xep_hang_kho.txt',self.Bang_xep_hang_kho)

	def Lay_du_lieu_tuy_chon(self):  #Lay du lieu cho bang xep hang tuy chon gom thoi gian hoan thanh, do rong bang, so f0
		try:
			with open('Data/Bang_xep_hang_tuy_chon.txt','r') as rf:
				line = rf.readline()
				line = line.replace('\n','')
				linesplit = line.split()
				while line:
					Du_lieu = [int(linesplit[1]),int(linesplit[2]),int(linesplit[3]),int(linesplit[4])]
					self.Bang_xep_hang_tuy_chon[linesplit[0]] = Du_lieu
					line = rf.readline()
					line = line.replace('\n','')
					linesplit = line.split()
		except FileNotFoundError:
			rf = open('Data/Bang_xep_hang_tuy_chon.txt','w') 
			rf.close()

	#neu trung ten thi kiem tra neu thanh tich moi tot hown thi luu thanh tich moi, con khong thi giu nguyen
	def Them_du_lieu(self,Thanh_tich_moi,Do_kho):  #Thêm dữ liệu cho các bảng xh dễ, bth, khó
		ten = nhap_ten()
		if Do_kho == 1:
			if ten not in self.Bang_xep_hang_de.keys() or self.Bang_xep_hang_de[ten] > Thanh_tich_moi:
				self.Bang_xep_hang_de[ten] = Thanh_tich_moi
			temp = sorted(self.Bang_xep_hang_de.items(),key = lambda x : x[1])
			self.Bang_xep_hang_de.clear()
			for item in temp:
				self.Bang_xep_hang_de[item[0]] = item[1]

		if Do_kho == 2:
			if ten not in self.Bang_xep_hang_bthuong.keys() or self.Bang_xep_hang_bthuong[ten] > Thanh_tich_moi:
				self.Bang_xep_hang_bthuong[ten] = Thanh_tich_moi
			temp = sorted(self.Bang_xep_hang_bthuong.items(),key = lambda x : x[1])
			self.Bang_xep_hang_bthuong.clear()
			for item in temp:
				self.Bang_xep_hang_bthuong[item[0]] = item[1]

		if Do_kho == 3:
			if ten not in self.Bang_xep_hang_kho.keys() or self.Bang_xep_hang_kho[ten] > Thanh_tich_moi:
				self.Bang_xep_hang_kho[ten] = Thanh_tich_moi
			temp = sorted(self.Bang_xep_hang_kho.items(),key = lambda x : x[1])
			self.Bang_xep_hang_kho.clear()
			for item in temp:
				self.Bang_xep_hang_kho[item[0]] = item[1]

	def Them_du_lieu_tuy_chon(self,Thanh_tich_moi,Do_rong_bang,So_f0,So_f0_max):  #thêm dữ liệu cho bảng xh tùy chọn
		ten = nhap_ten()
		Thanh_tich = [Thanh_tich_moi,Do_rong_bang,So_f0,So_f0_max]
		self.Bang_xep_hang_tuy_chon[ten] = Thanh_tich
		temp = sorted(self.Bang_xep_hang_tuy_chon.items(),key = lambda x : x[1][0])
		self.Bang_xep_hang_tuy_chon.clear()
		for item in temp:
			self.Bang_xep_hang_tuy_chon[item[0]] = item[1]

	def In_bang_xep_hang(self): #in bẳng xếp hạng

		cuaso = cua_so()
		run=True
		while run:
			for e in event.get():
				if e.type==QUIT:
					quit()
					exit()

				mouse_x, mouse_y = mouse.get_pos()
				if e.type == MOUSEBUTTONDOWN: 
					if e.button == 1: 
						if (10<mouse_x<80) and (10<mouse_y<50): 
							cuaso.In_de_kho(self.Bang_xep_hang_de)
						if (100<mouse_x<170) and (10<mouse_y<50):
							cuaso.In_de_kho(self.Bang_xep_hang_bthuong)
						if (190<mouse_x<260) and (10<mouse_y<50):
							cuaso.In_de_kho(self.Bang_xep_hang_kho)
						if (280<mouse_x<390) and (10<mouse_y<50):
							cuaso.In_tuy_chon(self.Bang_xep_hang_tuy_chon)	
						if (450<mouse_x<550) and (10<mouse_y<50):
							run=False
							
	def Ghi_du_lieu(self,filename,Bang):   #ghi dữ liệu vào file
		index = 0 
		with open(filename,'w') as wf:
			for key in Bang.keys():
				wf.write(f"{key} {Bang[key]}\n")
				index += 1
				if index >= 10:
					break

	def Ghi_du_lieu_all(self):     #ghi dữ liệu cho các bảng xh dễ, bth, khó
		self.Ghi_du_lieu('Data/Bang_xep_hang_de.txt',self.Bang_xep_hang_de)
		self.Ghi_du_lieu('Data/Bang_xep_hang_bthuong.txt',self.Bang_xep_hang_bthuong)
		self.Ghi_du_lieu('Data/Bang_xep_hang_kho.txt',self.Bang_xep_hang_kho)
	
	def Ghi_du_lieu_tuy_chon(self):	    #ghi dữ liệu cho bảng tuỳ chọn
		index = 0  
		with open('Data/Bang_xep_hang_tuy_chon.txt','w') as wf:
			for key in self.Bang_xep_hang_tuy_chon.keys():
				wf.write(f"{key} {self.Bang_xep_hang_tuy_chon[key][0]} {self.Bang_xep_hang_tuy_chon[key][1]} {self.Bang_xep_hang_tuy_chon[key][2]} {self.Bang_xep_hang_tuy_chon[key][3]}\n")
				index += 1
				if index >= 10:
					break