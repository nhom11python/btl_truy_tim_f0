from pygame import *
from nut import *

def nhap_ten():
	init()
	screen = display.set_mode((600,400))
	display.set_caption("Truy tìm F0")

	ghi_chu1 = font.SysFont('calibri', 20).render('TÊN NGƯỜI CHƠI:', True, trang)
	text1 = font.SysFont('calibri', 20).render(' LƯU ', True, trang)

	
	#tạo các hộp:
	mau1 = Surface((300, 30))
	mau1.fill(xam)  # lúc chưa click vào hộp thì hộp màu xám
	mau2 = Surface((300,30))
	mau2.fill(trang) # khi click vào thì hộp màu trắng

	hop_ten= hop(screen, mau1, mau2, (230, 130))
	nut_luu = nut(screen, text1, (420,200))

	running = True
	while running:		
		
		screen.fill(xanh_duong_nhat)
		screen.blit(ghi_chu1, (55, 130))

		hop_ten.ve()
		nut_luu.ve()
		
		for e in event.get():
			if e.type == QUIT:
				quit()
				exit()
			if e.type == MOUSEBUTTONDOWN:
				hop_ten.click_chuot()

				if nut_luu.nhap_chuot(chuot_trai) and hop_ten.text!='':
					return hop_ten.text
					running = False
					#running = False

			if e.type == KEYDOWN:
				hop_ten.nhap_du_lieu(e.key,'qwertyuiopasdfghjklzxcvbnm1234567890')
				
		display.update()

#chay thu
#print(nhap_ten())