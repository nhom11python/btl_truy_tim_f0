from pygame import *
from man_choi_xu_ly_du_lieu import *
from man_choi_do_hoa_va_tuong_tac import *
from nut import *

white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)
orange=(255,100,10)
yellow=(255,255,0)
gray = (100,100,100)

"""Cửa sổ nhập dữ liệu tùy chọn"""
def nhap():
	init()
	screen = display.set_mode((600,350))
	display.set_caption("Truy tìm F0")
	bg = image.load ("images/covidbg2.png")

	ghi_chu1 = font.SysFont('calibri', 20).render('KÍCH THƯỚC:', True, white)
	ghi_chu2 = font.SysFont('calibri', 20).render('SỐ F0:', True, white)
	ghi_chu3 = font.SysFont('calibri', 20).render('SỐ F0 MAX:', True, white)
	ghi_chu4 = font.SysFont('calibri', 20).render('THỜI GIAN:', True, white)
	text1 = font.SysFont('calibri', 20).render(' CHƠI ', True, white)
	text = font.SysFont('calibri', 20).render(' THOÁT ', True, white)

	
	#tạo các hộp:
	mau1 = Surface((350, 30))
	mau1.fill(gray)  # lúc chưa click vào hộp thì hộp màu xám
	mau2 = Surface((350,30))
	mau2.fill(white) # khi click vào thì hộp màu trắng

	hop_kich_thuoc= hop(screen, mau1, mau2, (170, 130))
	hop_so_f0 = hop(screen, mau1, mau2, (170, 170))
	hop_so_f0_max = hop(screen, mau1, mau2, (170, 210))
	hop_thoi_gian =hop(screen, mau1, mau2, (170, 250))

	nut_choi = nut(screen, text1, (420,302))
	nut_thoat = nut(screen, text, (480,300))

	#KÍCH THƯỚC NHỎ HƠN HOẶC BẰNG 20, SỐ F0 TỐI ĐA PHẢI
	#NHỎ HƠN SỐ Ô TRÊN BẢN ĐỒ, SỐ F0 BAN ĐẦU NHỌ HƠN SỐ F0 TỐI ĐA
	running = True
	while running:		
		
		screen.blit(bg, (0,0))
		screen.blit(ghi_chu1, (55, 130))
		screen.blit(ghi_chu2, (55, 170))
		screen.blit(ghi_chu3, (55, 210))
		screen.blit(ghi_chu4, (55, 250))

		hop_kich_thuoc.ve()
		hop_so_f0.ve()
		hop_so_f0_max.ve()
		hop_thoi_gian.ve()
		
		nut_choi.ve()
		nut_thoat.ve()
		
		for e in event.get():
			if e.type == QUIT:
				quit()
				exit()
			if e.type == MOUSEBUTTONDOWN:
				hop_kich_thuoc.click_chuot()
				hop_so_f0.click_chuot()
				hop_so_f0_max.click_chuot()
				hop_thoi_gian.click_chuot()

				# nhấn nút chơi thì đưa đến màn chơi có thông số đã nhập
				if nut_choi.nhap_chuot(chuot_trai):
					#print('Choi thoi')
					if hop_kich_thuoc.text!='' and hop_so_f0.text!='' and hop_so_f0_max.text!='' and hop_thoi_gian.text!='': 
						kt=int(hop_kich_thuoc.text)
						f0=int(hop_so_f0.text)
						f0_max=int(hop_so_f0_max.text)
						tg=int(hop_thoi_gian.text)
						if 0<kt and kt<=20 and 0<f0 and f0<f0_max and 0<f0_max and f0_max<kt**2 and 0<tg and tg<10000000000:
							man_choi(3,[kt,f0,f0_max,tg])
							running = False
				# nhấn nút thoát thì quay lại cửa sổ lựa chọn mức độ
				if nut_thoat.nhap_chuot(chuot_trai):
					running = False

			if e.type == KEYDOWN:
				hop_kich_thuoc.nhap_du_lieu(e.key,'1234567890')
				hop_so_f0.nhap_du_lieu(e.key,'1234567890')
				hop_so_f0_max.nhap_du_lieu(e.key,'1234567890')
				hop_thoi_gian.nhap_du_lieu(e.key,'1234567890')
		display.update()
		

"""Cửa sổ lựa chọn mức độ hoặc tùy chọn"""
def chon():
	screen = display.set_mode((600,350))
	display.set_caption("Truy tìm F0")
	bg = image.load("images/covidbg.png")

	text1 = font.SysFont('calibri', 50).render("LỰA CHỌN", True, white)
	text2 = font.SysFont('calibri', 20).render('          DỄ         ', True, red, white)
	text3 = font.SysFont('calibri', 20).render('        VỪA        ', True, red, white) 
	text4 = font.SysFont('calibri', 20).render('        KHÓ        ', True, red, white)
	text5 = font.SysFont('calibri', 20).render('   TÙY CHỌN   ', True, red, white)

	nut_de = nut(screen, text2, (400, 130))
	nut_vua = nut(screen, text3, (400, 170))
	nut_kho = nut(screen, text4, (400, 210))
	nut_tuy_chon = nut(screen, text5, (400, 250))

	run=True
	while run:
		screen.blit(bg, (0,0))
		screen.blit(text1, (340,50))
		
		nut_de.ve()
		nut_vua.ve()
		nut_kho.ve()
		nut_tuy_chon.ve()
		
		for e in event.get():
			if e.type == QUIT:
				quit()
				sys.exit()
			if e.type == MOUSEBUTTONDOWN:
				if nut_de.nhap_chuot(chuot_trai):
					#print("chon muc do de")
					man_choi(0)
					run=False
					continue
				if nut_vua.nhap_chuot(chuot_trai):
					#print("chon muc do vua")
					man_choi(1)
					run=False
					continue
				if nut_kho.nhap_chuot(chuot_trai):
					#print("chon muc do kho")
					man_choi(2)
					run=False
					continue
				if nut_tuy_chon.nhap_chuot(chuot_trai):
					nhap()
					run=False
					continue
		display.update()


#chay thu
#chon()