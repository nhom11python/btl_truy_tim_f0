from random import randint #can ham randint de khoi tao ngau nhien vi tri f0
from pygame import time #lay thoi gian

'''
che_do_de=(10,10,15,2*60)
che_do_vua=(15,25,30,3*60)
che_do_kho=(20,40,45,5*60)
'''

class bang():
	def __init__(self,kich_thuoc=10,so_f0=10,so_f0_max=15,thoi_gian=2*60):
		self.kich_thuoc=kich_thuoc#kich thuoc cua bang vuong
		self.so_f0=so_f0#so f0 ban dau
		self.so_f0_max=so_f0_max#so f0 toi da co the co
		self.so_f0_ban_dau=so_f0#dung de dat lai man choi
		self.so_dau=0#so dau da danh (khong lon hon so f0)
		self.thoi_gian=thoi_gian#thoi gian toi da cho 1 man (het thoi gian thi thua)
		self.thoi_gian_hoan_thanh=None#thoi gian choi cho den khi thang hoac thua
		self.thoi_gian_bat_dau=time.get_ticks()#thoi gian bat dau man choi
		self.thang=False
		self.thua=False
		
		self.hien_thi=[[0 for i in range(self.kich_thuoc)] for i in range(self.kich_thuoc)]
		#bang cho biet cac o: da mo (1), chua mo (0), o goi y (2), danh dau (3)
		
		self.f0=[[0 for i in range(self.kich_thuoc)] for i in range(self.kich_thuoc)]
		#bang luu gia tri f0
		#o f0 co gia tri 9
		#o khong pai f0 co gia tri bang so f0 o 8 o xong quanh no
	
	def thoi_gian_con_lai(self):
		if self.thoi_gian_hoan_thanh==None:
			return self.thoi_gian-(time.get_ticks()-self.thoi_gian_bat_dau)//1000
		return self.thoi_gian-self.thoi_gian_hoan_thanh
	
	#dat lai toan bo man choi
	def dat_lai(self):
		self.__init__(self.kich_thuoc,self.so_f0_ban_dau,self.so_f0_max,self.thoi_gian)
		self.khoi_tao_f0()
		self.tinh_toan()
		self.goi_y()
		
	#kiem tra xem toa do x,y co nam trong bang hay k??
	def nam_trong(self,x,y):
		if 0<=x and x<self.kich_thuoc and 0<=y and y<self.kich_thuoc:
			return True
		return False

	#dua vi tri x,y va cac o lan can ve trang thai chua mo
	#tru cac o bi danh dau
	def lam_moi(self,x,y):
		for i in range(x-1,x+2):
			for j in range(y-1,y+2):
				if self.nam_trong(i,j):
					if self.hien_thi[i][j]!=3:
						self.hien_thi[i][j]=0

	#so trong 1 o khong phai f0 se the hien so f0 xung quanh no
	#ham duyet tung o trong bang f0 va tinh gia tri cua no
	def tinh_toan(self):
		for x in range(self.kich_thuoc):
			for y in range(self.kich_thuoc):
				if self.f0[x][y]!=9:
				#duyet tung o trong bang khong phai f0
					self.f0[x][y]=0
					for i in range(x-1,x+2):
						for j in range(y-1,y+2):
							if self.nam_trong(i,j) and self.f0[i][j]==9:
								self.f0[x][y]+=1

	#tim ra o dau tien co gia tri 0 trong bang f0
	def goi_y(self):
		for i in range(self.kich_thuoc):
			for j in range(self.kich_thuoc):
				if self.f0[i][j]==0:
					self.hien_thi[i][j]=2
					return

	#tao ra f0 o vi tri ngau nhien va f0 tao ra phai nam o cac o chua mo
	def khoi_tao_f0(self,so_luong=None):
		if so_luong==None:
			so_luong=self.so_f0
		for i in range(so_luong):
			x=randint(0,self.kich_thuoc-1)
			y=randint(0,self.kich_thuoc-1)
			while self.f0[x][y]==9 or self.hien_thi[x][y]!=0:#dam bao f0 dc tao ra k trung vs f0 nao khac va phai nam o vi tri chua mo
				x=randint(0,self.kich_thuoc-1)
				y=randint(0,self.kich_thuoc-1)
			self.f0[x][y]=9#f0 co so la 9
			self.lam_moi(x,y)

	def bfs(self,x,y):
	#thuat toan su dung bfs
		l=[[x,y]]#danh sach de luu vi tri cac so khong da duyet - bfs
		#gia tri dau tien tring danh sach la o so 0 vua mo
		self.hien_thi[x][y]=1
		while l:#neu danh sach chua trong (con co vi tri chua duyet) thi duyet phan tu dau cua danh sach
			a,b=l[0][0],l[0][1]#lay ra phan tu dau
			del l[0]#xoa di phan tu da lay ra
			for i in range(a-1,a+2):
				for j in range(b-1,b+2):
					if self.nam_trong(i,j):
						#duyet tat ca cac o xung quanh no va ca chinh no, o do phai nam trong self.hien_thi
						if self.f0[i][j]==0 and self.hien_thi[i][j] in [0,2]:#neu o do bang 0 va chua duyet thi
							self.hien_thi[i][j]=1#mo o do trong bang hien thi
							l.append([i,j])#them o do vao danh sach
						if self.f0[i][j]>0 and self.f0[i][j]<9:#neu o do co so tu 1-8
							self.hien_thi[i][j]=1#mo o do trong bang hien thi
																	
	def do_tim(self,x,y):
		if self.hien_thi[x][y] in [0,2]:
		#chi do tim o cac vi tri chua mo hoac co goi y
			if self.f0[x][y]==0:
			#neu o dang do co so 0 thi dong thoi mo toan bo cac o co so 0 lien thong voi no
			#va mo luon cac o co so tu 1-8 nam gan cac o co so 0 da mo
				self.bfs(x,y)
			elif self.f0[x][y]<9:#neu o dang do co so tu 1-8
				self.hien_thi[x][y]=1#mo no trong bang hien thi
			else:#neu o dang do la f0 thi f0 do chay di ra mot vi tri ngau nhien khac
			#va sinh ra them 1 f0 moi o vi tri ngau nhien
			#tuy vay, trong thuat toan ta se xoa f0 do di va sinh ra them hai f0 nua o vi tri ngau nhien (y nghia tuong tu) 
			#vi tri xung quanh f0 bi xoa va hai f0 moi deu se bi lam moi (tro ve trang thai chua mo)
				#xoa f0 cu
				self.f0[x][y]=0
				self.lam_moi(x,y)
				self.khoi_tao_f0(2)#tao ra hai f0 moi
				self.so_f0+=1#tang so f0 len 1
				self.tinh_toan()
				
	def danh_dau(self,x,y):#danh dau va xoa dau da danh
		if self.hien_thi[x][y]==3:#vi tri da co dau thi xoa dau da danh va giam so dau di 1
			self.hien_thi[x][y]=0
			self.so_dau-=1
		elif self.so_dau<self.so_f0 and self.hien_thi[x][y]==0:#neu khong co dau va so dau da danh nho hon so f0 hien tai thi danh dau
			self.hien_thi[x][y]=3
			self.so_dau+=1
		
	def kiem_tra_thang(self):#neu toan bo cac o f0 bi danh dau va cac o con lai da mo thi ban thang
		for i in range(self.kich_thuoc):
			for j in range(self.kich_thuoc):
				if self.hien_thi[i][j]==0:#con o chua mo
					return
				if self.f0[i][j]==9 and self.hien_thi[i][j]!=3:
					return
		self.thoi_gian_hoan_thanh=(time.get_ticks()-self.thoi_gian_bat_dau)//1000
		self.thang=True
		
	def kiem_tra_thua(self):#neu so f0 lon hon so f0 max hoac het thoi gian thi ban thua
		if self.so_f0>self.so_f0_max or self.thoi_gian<=(time.get_ticks()-self.thoi_gian_bat_dau)//1000:
			self.thoi_gian_hoan_thanh=(time.get_ticks()-self.thoi_gian_bat_dau)//1000
			self.thua=True
			#hien thi toan bo so bom
			for x in range(self.kich_thuoc):
				for y in range(self.kich_thuoc):
					if self.f0[x][y]==9:
						self.hien_thi[x][y]=4