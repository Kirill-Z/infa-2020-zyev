
from graph import*

windowSize(400, 580)
penSize(0)
N = 5

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
brushColor('#231c03')
rectangle(20, 150, 235, 450)

#House painting
brushColor('#554343')
rectangle(35, 150, 58, 246)
rectangle(78, 150, 101, 248)
rectangle(133, 150, 156, 247)
rectangle(188, 150, 211, 248)

#Roof
penColor('black')
brushColor('black')
polygon([(0, 150), (30, 130),
         (225, 130), (255, 150)])

#Pipes behind the clouds
penSize(7)
penColor('#232323')
line(50, 140, 50, 110)
line(155, 130, 155, 110)
penSize(0)

#Grey cloud
brushColor('#333333')
oval(20, 80, 340, 120)

#Balcony
brushColor('#131313')
rectangle(0, 249, 265, 280)
rectangle(10, 210, 250, 225)

penColor('#131313')
penSize(5)
line(8, 225, 8, 249)
line(252, 225, 252, 249)


x1 = 10; y1 = 225
x2 = 250; y2 = 250
h = (x2 - x1)/(N + 1)
x = x1 + h
penSize(10)
for i in range(N):
    line(x, y1, x, y2)
    x += h
penSize(0)

#Windows
brushColor('#270900')
rectangle(45, 355, 85, 410)
rectangle(110, 355, 150, 410)
brushColor('#d5ac00') #yellow
rectangle(170, 355, 215, 410)

#Light grey clouds
brushColor('#4c4c4c')
oval(190, 55, 430, 97)
oval(250, 105, 470, 140)

#Pipes in front of cloud
penColor('#131313')
penSize(15)
line(65, 143, 65, 78)
penSize(5)
line(215, 143, 215, 90)
penSize(0)

#Ghost
brushColor('#aaaaaa')
circle(300, 455, 18)
brushColor('#C0E1ED')
circle(292, 453, 4)
circle(305, 451, 4)
brushColor('black')
circle(290, 453, 1.5)
circle(304, 451, 1.5)

run()
