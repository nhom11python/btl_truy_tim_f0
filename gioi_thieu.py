from pygame import *

init()

red = Color(255, 0, 0)
white = Color(255, 255, 255)
black= Color(0, 0, 0)

def luatchoi():
    #tao khung chuong trinh
    screen = display.set_mode((760, 550))# tao khung hien thi voi kich thuoc chieu rong va chieu dai
    display.set_caption("Truy tìm F0")# them tieu de cho cua so
    background = image.load("images/phongnen.png")# load hinh anh
    screen.blit(background, (0, 0))# hien thi hinh anh tren window
    chu = font.SysFont("calibri", 30)# tao chu chu
    boicanh=image.load("images/luatchoi.png")
    
    text1 = chu.render(" THOÁT ", True, white)
    text_rect1 = text1.get_rect(center=(380, 500))  # can giua van ban
    chay=True    
    while chay:
        #ve chu
        screen.blit(boicanh, (0, 0))
        screen.blit(text1, text_rect1)
        for e in event.get():# lay cac su kien tren window: an nut, chuot,..
            if e.type == QUIT:# neu nhan nut tat thi thoat
                sys.exit()         
            if e.type == MOUSEBUTTONDOWN and e.button==1:    #kiem tra xem co an nut chuot trai hay khong
                if text_rect1.collidepoint(e.pos):#kiem tra xem chuot nam trong khung chu, envent.pos la toa do cua chuot
                    chay=False
        display.update()# cap nhat lai window
    cua_so=display.set_mode((600,337))
def thongtin():
    screen = display.set_mode((700, 550))
    display.set_caption("Truy tìm F0")
    background = image.load("images/phongnen.png")
    screen.blit(background, (0, 0))
    chu = font.SysFont("calibri", 30)
    thanhvien=image.load("images/thanhvien.png")
    
    text1 = chu.render(" THOÁT ", True, white)
    text_rect1 = text1.get_rect(center=(350, 500))
    chay=True
    while chay:
        screen.blit(thanhvien, (0, 0))
        screen.blit(text1, text_rect1)
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                    
                if text_rect1.collidepoint(e.pos):
                    chay=False
        display.update()
    cua_so=display.set_mode((600,337))
def boicanh():
    screen = display.set_mode((700, 550))
    display.set_caption("Truy tìm F0")
    background = image.load("images/phongnen.png")
    screen.blit(background, (0, 0))
    chu = font.SysFont("calibri", 30)
    boicanh=image.load("images/boicanh.png")
    text1 = chu.render(" THOÁT ", True, white)
    text_rect1 = text1.get_rect(center=(350, 500))
    screen.blit(boicanh, (0, 0))
    screen.blit(text1, text_rect1)
    chay=True
    while chay:
        
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:        
                if text_rect1.collidepoint(e.pos):
                    chay=False
        display.update()
    cua_so=display.set_mode((600,337))
def GioiThieu():
    screen = display.set_mode((600,337)) 
    display.set_caption("Truy tìm F0")
    background = image.load("images/phongnen.png")
    chu = font.SysFont("calibri", 30)#tao chu chu
    #tao chu
    text = chu.render(" BỐI CẢNH ", True, white)
    text1 = chu.render(" LUẬT CHƠI ", True, white)
    text2 = chu.render(" THÔNG TIN NHÓM ", True, white)
    text3 = chu.render(" THOÁT ", True, white)
    #can giua van ban
    text_rect = text.get_rect(center=(300, 50))
    text_rect1 = text1.get_rect(center=(300,100))
    text_rect2 = text2.get_rect(center=(300, 150))
    text_rect3 = text3.get_rect(center=(300, 250))  
    chay=True
    while chay:
        
        screen.blit(background, (0, 0))#ve nen
        #ve chu
        screen.blit(text, text_rect)
        screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        
        for e in event.get():
            if e.type == QUIT:
                quit()
                exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1: 
                if text_rect.collidepoint(e.pos):
                    boicanh() 
                if text_rect1.collidepoint(e.pos):
                    luatchoi()
                if text_rect2.collidepoint(e.pos):
                    thongtin()
                if text_rect3.collidepoint(e.pos):
                    chay=False
        display.update()  

#chay thu
#GioiThieu()