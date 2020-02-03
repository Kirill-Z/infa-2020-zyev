from graph import*

windowSize(400, 580)
penSize(0)

#Background
penColor('grey')
brushColor('grey')
rectangle(0, 0, 600, 250)
brushColor(0, 0, 0)
rectangle(0, 249, 600, 850)

#Moon
brushColor('white')
circle(370, 60, 40)

#Very dark grey cloud
brushColor('#131313')
oval(215, 148, 440, 190)

#Home
def Home(x1, y1):
    x2 = x1 + 110
    y2 = y1 + 155
    brushColor('#231c03')
    moveTo(x1, y1)
    rectangle(x1, y1, x2, y2)
    def housePainting():
        brushColor('554343')
        #rectangle()
    def roof(x1, y1, x2, y2):
        penColor('black')
        brushColor('black')
        polygon([(x1 - 10, y1), (x1 + 20, y1 - 20),
                 (x2 - 10, y1 - 20), (x2 + 10, y1)])
    def balcony():
        brushColor('#989898')
        x2BalconyDown = x2 + 10
        x2BalconyUp = x2 + 5
        rectangle(x1 - 10, y1 + 50, x2 + 10, y1 + 75)
        rectangle(x1 + 10, y1 + 40, x2 + 10, y1 + 55)

        penColor('#131313')
        penSize(5)
        line(x1 - 2, y1 + 75, x1 - 2, y1 + 95)
        line(x2 + 8, y1 + 75, x2 + 8, y1 + 95)

        N = 5
        h = (x2 - x1)/(N + 1)
        x = x1 + h
        penSize(10)
        for i in range(N):
            line(x, y1, x, y2)
            x += h
        penSize(0)
    def windows(x1, x2, y2):
        brushColor('#270900')
        N = 3
        h = (x2 - x1)/(N + 1)
        x = x1 + h
        for i in range(N - 1):
            rectangle(x, y2 - 60, x + 30, y2 - 30)
            x += h
        else:
            brushColor('#d5ac00') #yellow
            rectangle(x, y2 - 60, x + 30, y2 - 30)
    def pipes():
        #Pipes behind the clouds
        penSize(7)
        penColor('#232323')
        line(x1 + 20, y1 - 10, x1 + 20, y1 - 25)
        line(x2 - 20, y1, x2 - 20, y1 - 20)
        #Pipes in front of cloud
        penSize(15)
        line(x1 + 35, y1 - 7, x1 + 35, y1 - 40)
        penSize(5)
        line(x2 - 40, y1 - 7, x2 - 40, y1 - 20)
        penSize(0)




#Grey cloud
brushColor('#333332')
oval(19, 80, 340, 120)

#Light grey clouds
brushColor('#4c4c4c')
oval(190, 55, 430, 97)
oval(250, 105, 470, 140)

#Ghost
brushColor('#aaaaaa')
polygon([(285, 457), (323, 453),
         (365, 507), (245, 527)])
circle(300, 455, 18)
brushColor('#C0E1ED')
circle(290, 453, 4.5)
circle(305, 451, 4.5)
brushColor('black')
circle(288, 454, 1.5)
circle(302, 452, 1.5)
brushColor('white')
oval(290, 453, 294.5, 451)
oval(304, 451, 309.5, 449)

Home(10, 280)
run()

