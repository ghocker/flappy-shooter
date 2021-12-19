from math import *
from os import stat
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#import os
import random as rd
poin = 0
kor_x_pesawat = 0
kor_y_pesawat = 100
kor_x_manuk = 0
kor_y_manuk = -40
kor_x_peluru = 0
kor_y_peluru = -32
move = 1
shoot = False
nyawa = 5
state = False

def init() :
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-80.0, 80.0, -80.0, 80.0)
def menu ():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(66, 245, 242)
    glVertex2f(500,500)
    glVertex2f(500,-500)
    glVertex2f(-500,-500)
    glVertex2f(-500,500)
    glEnd()
    glColor3ub(74, 232, 16)
    glTranslated(0,5,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-1,3)
    glVertex2f(0,5)
    glVertex2f(1,3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-4,-4)
    glVertex2f(-4,-3)
    glVertex2f(-3,-3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(4,-4)
    glVertex2f(4,-3)
    glVertex2f(3,-3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-6,-4)
    glVertex2f(-4,-4)
    glVertex2f(-4,-2)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(6,-4)
    glVertex2f(4,-4)
    glVertex2f(4,-2)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-1,-3)
    glVertex2f(1,-3)
    glVertex2f(1,-5)
    glVertex2f(-1,-5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2,0)
    glVertex2f(-1,1)
    glVertex2f(1,1)
    glVertex2f(2,0)
    glVertex2f(2,-2)
    glVertex2f(1,-3)
    glVertex2f(-1,-3)
    glVertex2f(-2,-2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2,-6)
    glVertex2f(-1,-5)
    glVertex2f(1,-5)
    glVertex2f(2,-6)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-4,-2)
    glVertex2f(-2,0)
    glVertex2f(-2,-2)
    glVertex2f(-3,-3)
    glVertex2f(-4,-3)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(2,0)
    glVertex2f(4,-2)
    glVertex2f(4,-3)
    glVertex2f(3,-3)
    glVertex2f(2,-2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-4,-8)
    glVertex2f(-2,-6)
    glVertex2f(0,-6)
    glVertex2f(-4,-10)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(4,-8)
    glVertex2f(2,-6)
    glVertex2f(0,-6)
    glVertex2f(4,-10)
    glEnd()
    glBegin(GL_POLYGON)
    for i in range(100): 
        cosine= 1.6 * cos(i*2*pi/100) + 0  
        sine  = 1.6 * sin(i*2*pi/100) + 2   
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()
    glColor3ub(0,0,0)
    glRasterPos(-27,20 )
    for p in str('FLAPPY SHOOTER') :
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(p) )
    glRasterPos(-29,-20 )
    for p in str('PRESS F1 TO START') :
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(p) )

def bg() :
    glPushMatrix()
    glColor3ub(66, 245, 242)
    glBegin(GL_POLYGON)
    glVertex2f(500,500)
    glVertex2f(500,-500)
    glVertex2f(-500,-500)
    glVertex2f(-500,500)
    glEnd()
    glPopMatrix()

def pesawat() :
    global kor_x_pesawat,kor_y_pesawat,move,poin,nyawa,kor_x_manuk
    glPushMatrix()
    glColor3ub(232, 16, 16)
    kor_y_pesawat -= move
    if kor_y_pesawat < -100 :
        kor_y_pesawat = 105
        kor_x_pesawat = rd.randrange(-70,70)
    if kor_x_pesawat in range(kor_x_peluru-15,kor_x_peluru) and kor_y_pesawat in range(kor_y_peluru-6,kor_y_peluru+3) :
        kor_y_pesawat = 80
        kor_x_pesawat = rd.randrange(-70,70)
        poin += 1
    if kor_x_pesawat in range(kor_x_manuk-20,kor_x_manuk) and kor_y_pesawat in range (kor_y_manuk-8,kor_y_manuk+5) :
        nyawa -= 1
        kor_x_manuk -= 15
    glTranslated(kor_x_pesawat,kor_y_pesawat,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(10,5)
    glVertex2f(9,6)
    glVertex2f(11,6)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(9,12)
    glVertex2f(11,12)
    glVertex2f(11,6)
    glVertex2f(9,6)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(8,10)
    glVertex2f(9,10)
    glVertex2f(9,8)
    glVertex2f(8,8)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(11,10)
    glVertex2f(12,10)
    glVertex2f(12,8)
    glVertex2f(11,8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(8,13)
    glVertex2f(12,13)
    glVertex2f(11,12)
    glVertex2f(9,12)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(7,11)
    glVertex2f(8,10)
    glVertex2f(8,8)
    glVertex2f(7,9)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(6,11)
    glVertex2f(7,11)
    glVertex2f(7,9)
    glVertex2f(6,10)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(12,10)
    glVertex2f(13,11)
    glVertex2f(13,9)
    glVertex2f(12,8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(13,11)
    glVertex2f(14,11)
    glVertex2f(14,10)
    glVertex2f(13,9)
    glEnd()
    glPopMatrix()

def pesawat2() :
    global kor_x_pesawat,kor_y_pesawat,move,poin,nyawa,kor_x_manuk
    glPushMatrix()
    glColor3ub(232, 16, 16)
    kor_y_pesawat -= move
    if kor_y_pesawat < -100 :
        kor_y_pesawat = 85
        kor_x_pesawat = rd.randrange(-35,105)
    if kor_x_pesawat in range(kor_x_peluru+35,kor_x_peluru+60) and kor_y_pesawat in range(kor_y_peluru-6,kor_y_peluru+3) :
        kor_y_pesawat = 80
        kor_x_pesawat = rd.randrange(-50,90)
        poin += 1
    if kor_x_pesawat in range(kor_x_manuk+40,kor_x_manuk+60) and kor_y_pesawat in range (kor_y_manuk-8,kor_y_manuk+5) :
        nyawa -= 1
        kor_x_manuk -= 15
    glTranslated(kor_x_pesawat-60,kor_y_pesawat,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(10,5)
    glVertex2f(9,6)
    glVertex2f(11,6)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(9,12)
    glVertex2f(11,12)
    glVertex2f(11,6)
    glVertex2f(9,6)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(8,10)
    glVertex2f(9,10)
    glVertex2f(9,8)
    glVertex2f(8,8)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(11,10)
    glVertex2f(12,10)
    glVertex2f(12,8)
    glVertex2f(11,8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(8,13)
    glVertex2f(12,13)
    glVertex2f(11,12)
    glVertex2f(9,12)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(7,11)
    glVertex2f(8,10)
    glVertex2f(8,8)
    glVertex2f(7,9)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(6,11)
    glVertex2f(7,11)
    glVertex2f(7,9)
    glVertex2f(6,10)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(12,10)
    glVertex2f(13,11)
    glVertex2f(13,9)
    glVertex2f(12,8)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(13,11)
    glVertex2f(14,11)
    glVertex2f(14,10)
    glVertex2f(13,9)
    glEnd()
    glPopMatrix()


def manuk() :
    global kor_x_manuk,kor_y_manuk, nyawa
    glPushMatrix()
    glColor3ub(74, 232, 16)
    if kor_x_manuk <= -75:
        kor_x_manuk = -75
    if kor_x_manuk >= 75:
        kor_x_manuk = 75
    if kor_y_manuk <= -70:
        kor_y_manuk = -70
    if kor_y_manuk >= 0:
        kor_y_manuk = 0
    
    glTranslated(kor_x_manuk,kor_y_manuk,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-1,3)
    glVertex2f(0,5)
    glVertex2f(1,3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-4,-4)
    glVertex2f(-4,-3)
    glVertex2f(-3,-3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(4,-4)
    glVertex2f(4,-3)
    glVertex2f(3,-3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-6,-4)
    glVertex2f(-4,-4)
    glVertex2f(-4,-2)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(6,-4)
    glVertex2f(4,-4)
    glVertex2f(4,-2)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-1,-3)
    glVertex2f(1,-3)
    glVertex2f(1,-5)
    glVertex2f(-1,-5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2,0)
    glVertex2f(-1,1)
    glVertex2f(1,1)
    glVertex2f(2,0)
    glVertex2f(2,-2)
    glVertex2f(1,-3)
    glVertex2f(-1,-3)
    glVertex2f(-2,-2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2,-6)
    glVertex2f(-1,-5)
    glVertex2f(1,-5)
    glVertex2f(2,-6)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-4,-2)
    glVertex2f(-2,0)
    glVertex2f(-2,-2)
    glVertex2f(-3,-3)
    glVertex2f(-4,-3)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(2,0)
    glVertex2f(4,-2)
    glVertex2f(4,-3)
    glVertex2f(3,-3)
    glVertex2f(2,-2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-4,-8)
    glVertex2f(-2,-6)
    glVertex2f(0,-6)
    glVertex2f(-4,-10)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(4,-8)
    glVertex2f(2,-6)
    glVertex2f(0,-6)
    glVertex2f(4,-10)
    glEnd()
    glBegin(GL_POLYGON)
    for i in range(100): 
        cosine= 1.6 * cos(i*2*pi/100) + 0  
        sine  = 1.6 * sin(i*2*pi/100) + 2   
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()

def peluru() :
    global kor_x_peluru, kor_y_peluru,kor_x_manuk,kor_y_manuk,shoot
    glPushMatrix()
    glColor3ub(0,0,0)
    if shoot == True :
        kor_y_peluru += 1
    if shoot == False :
        kor_y_peluru = kor_y_manuk
        kor_x_peluru = kor_x_manuk
    if kor_y_peluru > 70 :
        shoot = False
    glTranslated(kor_x_peluru,kor_y_peluru,0)
    glBegin(GL_QUADS)
    glVertex2f(1,1)
    glVertex2f(1,-1)
    glVertex2f(-1,-1)
    glVertex2f(-1,1)
    glEnd()
    glPopMatrix()

def darah() :
    global nyawa
    glColor3ub( 0, 0, 0 )   #-> kalo mau diubah warna nya bisa
    glRasterPos(-72,-73 )
    for a in str(nyawa):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(a) )
    glPushMatrix()
    glTranslated(-80,-75,0)
    glColor3ub(250, 105, 163)
    glBegin(GL_POLYGON)
    glVertex2f(2,5)
    glVertex2f(3,6)
    glVertex2f(4,5)
    glVertex2f(5,6)
    glVertex2f(6,5)
    glVertex2f(4,3)
    glEnd()
    glPopMatrix()

def skor() :
    global poin
    glColor3ub( 0, 0, 0 )   #-> kalo mau diubah warna nya bisa
    glRasterPos(-75,70 )

    for p in 'score : '+str(poin):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(p) )
def over() :
    global state
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(66, 245, 242)
    glVertex2f(500,500)
    glVertex2f(500,-500)
    glVertex2f(-500,-500)
    glVertex2f(-500,500)
    glEnd()
    glColor3ub(74, 232, 16)
    glTranslated(-20,5,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-1,3)
    glVertex2f(0,5)
    glVertex2f(1,3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-4,-4)
    glVertex2f(-4,-3)
    glVertex2f(-3,-3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(4,-4)
    glVertex2f(4,-3)
    glVertex2f(3,-3)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-6,-4)
    glVertex2f(-4,-4)
    glVertex2f(-4,-2)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(6,-4)
    glVertex2f(4,-4)
    glVertex2f(4,-2)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-1,-3)
    glVertex2f(1,-3)
    glVertex2f(1,-5)
    glVertex2f(-1,-5)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2,0)
    glVertex2f(-1,1)
    glVertex2f(1,1)
    glVertex2f(2,0)
    glVertex2f(2,-2)
    glVertex2f(1,-3)
    glVertex2f(-1,-3)
    glVertex2f(-2,-2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2,-6)
    glVertex2f(-1,-5)
    glVertex2f(1,-5)
    glVertex2f(2,-6)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-4,-2)
    glVertex2f(-2,0)
    glVertex2f(-2,-2)
    glVertex2f(-3,-3)
    glVertex2f(-4,-3)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(2,0)
    glVertex2f(4,-2)
    glVertex2f(4,-3)
    glVertex2f(3,-3)
    glVertex2f(2,-2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-4,-8)
    glVertex2f(-2,-6)
    glVertex2f(0,-6)
    glVertex2f(-4,-10)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(4,-8)
    glVertex2f(2,-6)
    glVertex2f(0,-6)
    glVertex2f(4,-10)
    glEnd()
    glBegin(GL_POLYGON)
    for i in range(100): 
        cosine= 1.6 * cos(i*2*pi/100) + 0  
        sine  = 1.6 * sin(i*2*pi/100) + 2   
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()
    glColor3ub( 0, 0, 0 )   
    glRasterPos(0,-15 )
    for p in str(poin):
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(p) )   
    glRasterPos(0,15 )
    for p in 'GAME OVER' :
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(p) ) 
    glRasterPos(0,0 )
    for p in 'YOUR SCORE :' :
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(p) )
    glRasterPos(-45,-35)
    for p in 'PRESS F10 TO RETURN MENU' :
        glutBitmapCharacter( GLUT_BITMAP_TIMES_ROMAN_24, ord(p) )
def display():
    global state,nyawa,poin
    glClear(GL_COLOR_BUFFER_BIT)
    if state == False :
        menu()
        glFlush()
    if state == True and nyawa > -1:
        bg()
        pesawat()
        peluru()
        manuk()
        skor()
        darah()
        glFlush()
        if poin >= 5 :
            bg()
            pesawat()
            pesawat2()
            peluru()
            manuk()
            skor()
            darah()
            glFlush()
    if state == True and nyawa <= -1 :
        over()
        glFlush()

def input_keyboard(key,x,y):
    global kor_x_manuk,kor_y_manuk,shoot,state,nyawa,poin
    if key == GLUT_KEY_UP:
        kor_y_manuk += 2
    if key == GLUT_KEY_DOWN:
        kor_y_manuk -= 2
    if key == GLUT_KEY_LEFT:
        kor_x_manuk -= 2
    if key == GLUT_KEY_RIGHT:
        kor_x_manuk += 2
    if key == GLUT_KEY_F5 :
        shoot = True
    if key == GLUT_KEY_F1 :
        state = True
        nyawa = 5
        poin = 0
    if key == GLUT_KEY_F10 :
        state = False
        

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("FLAPPY SHOOTER")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    init()
    glutMainLoop()

main()