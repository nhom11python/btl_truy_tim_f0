from pygame import *
from chon_do_kho import *
from gioi_thieu import *
from man_choi_xu_ly_du_lieu import *
from man_choi_do_hoa_va_tuong_tac import *
from nut import *
from luu_diem import *
from bang_xep_hang import *


init() 
screen = display.set_mode((600,337)) 
display.set_caption("Truy Tìm F0")

YELLOW = (255,255,0) 
BLACK = (0,0,0) 
#Tạo font
font=font.SysFont('calibri',24) 
#Tạo chữ
b1=font.render('BẮT ĐẦU',True,BLACK)
b2=font.render('THÔNG TIN',True,BLACK)
b4=font.render('ĐIỂM CAO',True,BLACK)
b5=font.render('THOÁT',True,BLACK)


clock = time.Clock() 
bg = image.load('images/anh_game.png') 

#chèn âm thanh
nhac_chon_do_kho=mixer.Sound('sound/chon_do_kho.mp3')
nhac_gioi_thieu=mixer.Sound('sound/gioi_thieu.mp3')
nhac_menu=mixer.Sound('sound/menu.mp3')
nhac_xem_diem_cao=mixer.Sound('sound/xem_diem_cao.mp3')

mixer.Sound.play(nhac_menu,loops=-1)

running = True 
while running: 
	clock.tick(60)
	screen.blit(bg,(0,0))

	#Ve cac hinh chu nhat 
	draw.rect(screen,YELLOW,(420,140,130,40))
	draw.rect(screen,YELLOW,(420,190,130,40))
	draw.rect(screen,YELLOW,(420,240,130,40))
	draw.rect(screen,YELLOW,(420,290,130,40))

	#Ve chu
	screen.blit(b1,(442,148))
	screen.blit(b2,(430,200))
	screen.blit(b4,(437,245))
	screen.blit(b5,(453,300))


	for e in event.get():
		if e.type == QUIT: 
			quit()
			exit()
		if e.type == MOUSEBUTTONDOWN:
			mouse_x, mouse_y = mouse.get_pos()
			if e.button == 1: 
				if (420<mouse_x<550) and (140<mouse_y<180): 
					mixer.stop()
					mixer.Sound.play(nhac_chon_do_kho,loops=-1)
					chon()
					screen = display.set_mode((600,337))
					mixer.stop()
					mixer.Sound.play(nhac_menu,loops=-1)
					
				if (420<mouse_x<550) and (190<mouse_y<230):
					mixer.stop()
					mixer.Sound.play(nhac_gioi_thieu,loops=-1)
					GioiThieu()
					screen = display.set_mode((600,337)) 
					mixer.stop()
					mixer.Sound.play(nhac_menu,loops=-1)
					
				if (420<mouse_x<550) and (240<mouse_y<280):
					mixer.stop()
					mixer.Sound.play(nhac_xem_diem_cao,loops=-1)
					xep_hang = Bang_xep_hang()
					xep_hang.Lay_du_lieu_all()    
					xep_hang.Lay_du_lieu_tuy_chon()
					xep_hang.In_bang_xep_hang()
					screen = display.set_mode((600,337)) 
					mixer.stop()
					mixer.Sound.play(nhac_menu,loops=-1)
					
				if (420<mouse_x<550) and (290<mouse_y<330):
					quit()
					exit()

		display.flip()