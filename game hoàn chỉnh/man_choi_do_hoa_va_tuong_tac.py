from pygame import *
from random import *
from nut import *
from man_choi_xu_ly_du_lieu import *
from luu_diem import *
from bang_xep_hang import *

init()

#nhac man choi
nhac_man_choi=mixer.Sound('sound/man_choi.mp3')
nhac_thang=mixer.Sound('sound/man_choi_thang.wav')#nhac khi thang
nhac_thua=mixer.Sound('sound/man_choi_thua.mp3')#nhac khi thua
nhac_danh_dau=mixer.Sound('sound/man_choi_danh_dau.wav')#nhac khi danh dau hoac bo danh dau
nhac_mo_o_moi=mixer.Sound('sound/man_choi_mo_o_moi.wav')#nhac khi mo dc mot o moi
nhac_mo_f0=mixer.Sound('sound/man_choi_mo_f0.wav')#nhac khi mo trung o co f0

#chinh lai am luong nhac cho phu hop :)))
mixer.Sound.set_volume(nhac_thang,0.4)
mixer.Sound.set_volume(nhac_thua,0.4)
mixer.Sound.set_volume(nhac_mo_f0,0.6)
mixer.Sound.set_volume(nhac_mo_o_moi,0.6)
mixer.Sound.set_volume(nhac_danh_dau,0.6)

#khoi tao cac doi tuong duoc ve tren cua so
#lua chon choi lai se lam moi man choi
anh_choi_lai=font.SysFont('calibri',20).render(' CHƠI LẠI ',True,trang,xanh_duong_nhat)

#thoat ra khoi man choi, ve laij man hinh chinh
anh_thoat=font.SysFont('calibri',20).render(' THOÁT ',True,trang,xanh_duong_nhat)

#hien thi khi thang
anh_thang=font.SysFont('calibri',20).render(' BẠN ĐÃ THẮNG ',True,trang,xanh_duong_nhat)

#hien thi khi thua
anh_thua=font.SysFont('calibri',20).render(' BẠN ĐÃ THUA ',True,trang,xanh_duong_nhat)

#lưu diem cao
anh_luu=font.SysFont('calibri',20).render(' LƯU ĐIỂM ',True,trang,xanh_duong_nhat)

#bang va cac o trong bang

kich_thuoc_o=20

#o chua mo 
anh_o_chua_mo=Surface((kich_thuoc_o,kich_thuoc_o))
anh_o_chua_mo.fill(vang)

#o goi y
anh_o_goi_y=Surface((kich_thuoc_o,kich_thuoc_o))
anh_o_goi_y.fill(cam)

#o da mo
anh_o_da_mo=[None]*9
for i in range(9):
	anh_o_da_mo[i]=Surface((kich_thuoc_o,kich_thuoc_o))
	anh_o_da_mo[i].fill(xam)
	text=font.SysFont('calibri',18).render(f'{i}',True,xanh_duong,xam)
	anh_o_da_mo[i].blit(text,(5,0))

#o danh dau
anh_o_danh_dau=Surface((kich_thuoc_o,kich_thuoc_o))
anh_o_danh_dau.fill(xanh_duong)
text=font.SysFont('calibri',18).render('V',True,trang,xanh_duong)
anh_o_danh_dau.blit(text,(4,0))

#o f0
anh_o_f0=Surface((kich_thuoc_o,kich_thuoc_o))
anh_o_f0.fill(xanh_duong)
text=font.SysFont('calibri',18).render('f0',True,trang,xanh_duong)
anh_o_f0.blit(text,(3,1))

def anh_o(i,j,bang_man_choi):
	if bang_man_choi.hien_thi[i][j]==0:
		return anh_o_chua_mo
	elif bang_man_choi.hien_thi[i][j]==1:
		return anh_o_da_mo[bang_man_choi.f0[i][j]]
	elif bang_man_choi.hien_thi[i][j]==2:
		return anh_o_goi_y
	elif bang_man_choi.hien_thi[i][j]==3:
		return anh_o_danh_dau
	return anh_o_f0
		
def man_choi(che_do,thong_so=None):	
	#khoi tao bang chua f0
	if che_do==0: bang_man_choi=bang(10,10,15,2*60)		
	if che_do==1: bang_man_choi=bang(15,25,30,3*60)		
	if che_do==2: bang_man_choi=bang(20,40,45,5*60)		
	if che_do==3: bang_man_choi=bang(thong_so[0],thong_so[1],thong_so[2],thong_so[3])		
	bang_man_choi.khoi_tao_f0()
	bang_man_choi.tinh_toan()
	bang_man_choi.goi_y()

	#khoi tao moi truong pygame
	init()
	cua_so=display.set_mode((500,600))#cua so de ve moi thu man choi
	cua_so.fill(vang_nhat)
	display.set_caption('Truy tìm F0')#ten game

	#khung bang
	anh_khung=Surface((20+(kich_thuoc_o+2)*bang_man_choi.kich_thuoc,20+(kich_thuoc_o+2)*bang_man_choi.kich_thuoc))
	anh_khung.fill(cam_nhat)
	
	#tao cac nut
	nut_luu=nut(cua_so,anh_luu,(200,100+(kich_thuoc_o+2)*bang_man_choi.kich_thuoc+30))
	nut_choi_lai=nut(cua_so,anh_choi_lai,(20,15))
	nut_thoat=nut(cua_so,anh_thoat,(140,15))
	nut_o=[[None for i in range(bang_man_choi.kich_thuoc)] for i in range(bang_man_choi.kich_thuoc)]
	for i in range(bang_man_choi.kich_thuoc):
		for j in range(bang_man_choi.kich_thuoc):
			nut_o[i][j]=nut(cua_so,anh_o(i,j,bang_man_choi),(30+(kich_thuoc_o+2)*i,100+(kich_thuoc_o+2)*j))
	
	#nhac
	mixer.stop()
	mixer.Sound.play(nhac_man_choi,loops=-1)

	man_choi_chay=True
	while man_choi_chay:
		#ve cac doi tuong
		nut_choi_lai.ve()
		nut_thoat.ve()
		cua_so.blit(anh_khung,(20,90))
		#hien thi thoi gian con lai
		anh_thoi_gian=font.SysFont('calibri',20).render(f' THỜI GIAN: {bang_man_choi.thoi_gian_con_lai()}  ',True,trang,xanh_duong_nhat)
		cua_so.blit(anh_thoi_gian,(290,50))

		#hien thi so ca da cach ly
		anh_cach_ly=font.SysFont('calibri',20).render(f' SỐ CA ĐÃ CÁCH LY: {bang_man_choi.so_dau}  ',True,trang,xanh_duong_nhat)
		cua_so.blit(anh_cach_ly,(240,15))

		#hien thi so f0 hien tai so voi so f0 max
		anh_muc_do=font.SysFont('calibri',20).render(f' MỨC ĐỘ LÂY LAN: {bang_man_choi.so_f0}/{bang_man_choi.so_f0_max}  ',True,trang,xanh_duong_nhat)
		cua_so.blit(anh_muc_do,(20,50))
		
		#hien thi bang
		for i in range(bang_man_choi.kich_thuoc):
			for j in range(bang_man_choi.kich_thuoc):
				nut_o[i][j].hinh_anh=anh_o(i,j,bang_man_choi)
				nut_o[i][j].ve()
				
		if not(bang_man_choi.thang or bang_man_choi.thua):
			#khi nguoi choi thang
			if not bang_man_choi.thang:
				bang_man_choi.kiem_tra_thang()
				if bang_man_choi.thang:
					cua_so.blit(anh_thang,(20,100+(kich_thuoc_o+2)*bang_man_choi.kich_thuoc+30))	
					nut_luu.ve()
					mixer.stop()
					mixer.Sound.play(nhac_thang)
			#khi nguoi choi thua
			if not bang_man_choi.thua:
				bang_man_choi.kiem_tra_thua()
				if bang_man_choi.thua:
					cua_so.blit(anh_thua,(20,100+(kich_thuoc_o+2)*bang_man_choi.kich_thuoc+30))
					mixer.stop()
					mixer.Sound.play(nhac_thua)
					
		for e in event.get():
			if e.type==QUIT:
				quit()
				exit()
			if e.type==MOUSEBUTTONDOWN:
				#thoat khoi man choi
				if nut_thoat.nhap_chuot(chuot_trai):
					man_choi_chay=False
					
				#bat dau mot man choi moi
				if nut_choi_lai.nhap_chuot(chuot_trai):
					bang_man_choi.dat_lai()
					cua_so.fill(vang_nhat)
					nut_choi_lai.ve()
					nut_thoat.ve()
					cua_so.blit(anh_khung,(20,90))
					mixer.stop()
					mixer.Sound.play(nhac_man_choi)
					
				#luu ten nguoi choi khi thang
				if nut_luu.nhap_chuot(chuot_trai) and bang_man_choi.thang:
					mixer.stop()
					mixer.Sound.play(nhac_man_choi)
					xep_hang = Bang_xep_hang()
					xep_hang.Lay_du_lieu_all()  
					xep_hang.Lay_du_lieu_tuy_chon()
					if che_do in [0,1,2]:
						xep_hang.Them_du_lieu(bang_man_choi.thoi_gian_hoan_thanh,che_do+1)
					else: 
						xep_hang.Them_du_lieu_tuy_chon(bang_man_choi.thoi_gian_hoan_thanh,bang_man_choi.kich_thuoc,bang_man_choi.so_f0,bang_man_choi.so_f0_max)
					xep_hang.Ghi_du_lieu_all()
					xep_hang.Ghi_du_lieu_tuy_chon()
					man_choi_chay=False
					
				#tuong tac voi cac o trong bang
				if not(bang_man_choi.thang or bang_man_choi.thua):
					for i in range(bang_man_choi.kich_thuoc):
						for j in range(bang_man_choi.kich_thuoc):
							if nut_o[i][j].nhap_chuot(chuot_trai):
								if bang_man_choi.hien_thi[i][j] in [0,2]:
									if bang_man_choi.f0[i][j]!=9:
										mixer.Sound.play(nhac_mo_o_moi)
									else:
										mixer.Sound.play(nhac_mo_f0)
								bang_man_choi.do_tim(i,j)
							if nut_o[i][j].nhap_chuot(chuot_phai):
								if bang_man_choi.hien_thi[i][j] in [0,3] and bang_man_choi.so_dau<bang_man_choi.so_f0:
									mixer.Sound.play(nhac_danh_dau)
								bang_man_choi.danh_dau(i,j)
		display.update()
	
#chay thu
#man_choi(che_do_de)