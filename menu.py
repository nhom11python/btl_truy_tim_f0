from pygame import *
from chon_do_kho import *
from gioi_thieu import *
from man_choi_do_hoa_va_tuong_tac import *
from nut import *
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
# b3=font.render('Options',True,BLACK)
b4=font.render('ĐIỂM CAO',True,BLACK)
b5=font.render('THOÁT',True,BLACK)


clock = time.Clock() 
bg = image.load('images/anh_game.png') 

running = True 
while running: 
	clock.tick(60) 
	screen.blit(bg,(0,0)) 
	mouse_x, mouse_y = mouse.get_pos() 

	#Ve cac hinh chu nhat 
	draw.rect(screen,YELLOW,(420,140,130,40))
	draw.rect(screen,YELLOW,(420,190,130,40))
	# draw.rect(screen,YELLOW,(495,150,92,40))
	draw.rect(screen,YELLOW,(420,240,130,40))
	draw.rect(screen,YELLOW,(420,290,130,40))

	#Ve chu
	screen.blit(b1,(442,148))
	screen.blit(b2,(430,200))
	# screen.blit(b3,(512,158))
	screen.blit(b4,(437,245))
	screen.blit(b5,(453,300))


	for e in event.get():
		if e.type == QUIT: 
			running=False 
		if e.type == MOUSEBUTTONDOWN:
			if e.button == 1: 
				if (420<mouse_x<550) and (140<mouse_y<180): 
					#print('start') #run ra -> start
					chon()
					screen = display.set_mode((600,337))
				if (420<mouse_x<550) and (190<mouse_y<230):
					#print('information')
					GioiThieu()
					screen = display.set_mode((600,337)) 
				if (420<mouse_x<550) and (240<mouse_y<280):
					#print('score')
					xep_hang = Bang_xep_hang()
					xep_hang.Lay_du_lieu_all()    
					xep_hang.Lay_du_lieu_tuy_chon()
					xep_hang.In_bang_xep_hang()
					screen = display.set_mode((600,337)) 
					
				if (420<mouse_x<550) and (290<mouse_y<330):
					quit()
					# exit()


		display.flip() 
quit() 