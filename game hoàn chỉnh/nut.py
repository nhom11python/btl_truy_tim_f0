from pygame import *

trang=(230,230,200)
xanh_duong=(50,0,200)
xanh_duong_nhat=(0,0,100)
xanh_la=(0,200,0)
xanh_la_nhat=(0,100,0)
do=(200,0,0)
den=(0,0,0)
xam=(100,100,100)
cam=(200,100,10)
cam_nhat=(200,50,0)
vang=(200,200,0)
vang_nhat=(100,100,0)

chuot_trai=0
chuot_giua=1
chuot_phai=2

#cac doi tuong can tuong tac bang chuot
class nut():
	def __init__(self,cua_so,hinh_anh,toa_do=(0,0)):
		self.cua_so=cua_so#cua so de ve doi tuong
		self.hinh_anh=hinh_anh#hinh anh cua nut
		self.toa_do=toa_do#toa do nut
		
	def ve(self):
		self.cua_so.blit(self.hinh_anh,self.toa_do)
		#ve nut
		
	def nhap_chuot(self,chuot):
		#lay toa do chuot va toa do anh, kiem tra xem chuot co dang nam trong anh hay k
		#dong thoi kiem tra chuot co dang duoc nhan
		if self.toa_do[0]<=mouse.get_pos()[0] and self.toa_do[0]+self.hinh_anh.get_width()>=mouse.get_pos()[0] and self.toa_do[1]<=mouse.get_pos()[1] and self.toa_do[1]+self.hinh_anh.get_height()>=mouse.get_pos()[1] and mouse.get_pressed()[chuot]:
			return True
		return False
		
#tao hop de dien du lieu
class hop():
	def __init__(self, cua_so, mau1, mau2, toa_do=(0,0), co_chu = 30, kieu_chu = None, mau_chu = trang):
		self.cua_so = cua_so
		self.mau1 = mau1
		self.mau2 = mau2
		self.toa_do = toa_do
		self.co_chu = co_chu
		self.kieu_chu = kieu_chu
		self.mau_chu = mau_chu
		self.dau_nhap = False
		self.text = ''
	
	def ve(self):
		chu = font.SysFont(self.kieu_chu, self.co_chu).render(self.text, True, xam, self.mau_chu)
		if self.dau_nhap:
			self.cua_so.blit(self.mau2, self.toa_do)
		else:
			self.cua_so.blit(self.mau1, self.toa_do)

		self.cua_so.blit(chu, self.toa_do)

	def click_chuot(self):
		if mouse.get_pressed()[chuot_trai]:
			if self.toa_do[0]<=mouse.get_pos()[0] and self.toa_do[0]+self.mau1.get_width()>=mouse.get_pos()[0] and self.toa_do[1]<=mouse.get_pos()[1]  and self.toa_do[1]+self.mau1.get_height()>=mouse.get_pos()[1]:
				self.dau_nhap = True
				#print('nhap')
			else:
				self.dau_nhap = False
		
	def nhap_du_lieu(self,key,chuoi_cho_phep):
		if self.dau_nhap:
			if key == K_BACKSPACE:
				self.text = self.text[:-1]
			elif key in range(0x110000) and chr(key) in chuoi_cho_phep:
				self.text += chr(key)
