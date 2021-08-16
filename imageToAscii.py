from PIL import Image
import math



lets = {
    'a':Image.open('a.png').load(),
    'b':Image.open('b.png').load(),
    'c':Image.open('c.png').load(),
    'd':Image.open('d.png').load(),
    'e':Image.open('e.png').load(),
    'f':Image.open('f.png').load(),
    'g':Image.open('g.png').load(),
    'h':Image.open('h.png').load(),
    'i':Image.open('i.png').load(),
    'j':Image.open('j.png').load(),
    'k':Image.open('k.png').load(),
    'l':Image.open('l.png').load(),
    'm':Image.open('m.png').load(),
    'n':Image.open('n.png').load(),
    'o':Image.open('o.png').load(),
    'p':Image.open('p.png').load(),
    'q':Image.open('q.png').load(),
    'r':Image.open('r.png').load(),
    's':Image.open('s.png').load(),
    't':Image.open('t.png').load(),
    'u':Image.open('u.png').load(),
    'v':Image.open('v.png').load(),
    'w':Image.open('w.png').load(),
    'x':Image.open('x.png').load(),
    'y':Image.open('y.png').load(),
    'z':Image.open('z.png').load(),
    'A':Image.open('a1.png').load(),
    'B':Image.open('b1.png').load(),
    'C':Image.open('c1.png').load(),
    'D':Image.open('d1.png').load(),
    'E':Image.open('e1.png').load(),
    'F':Image.open('f1.png').load(),
    'G':Image.open('g1.png').load(),
    'H':Image.open('h1.png').load(),
    'I':Image.open('i1.png').load(),
    'J':Image.open('j1.png').load(),
    'K':Image.open('k1.png').load(),
    'L':Image.open('l1.png').load(),
    'M':Image.open('m1.png').load(),
    'N':Image.open('n1.png').load(),
    'O':Image.open('o1.png').load(),
    'P':Image.open('p1.png').load(),
    'Q':Image.open('q1.png').load(),
    'R':Image.open('r1.png').load(),
    'S':Image.open('s1.png').load(),
    'T':Image.open('t1.png').load(),
    'U':Image.open('u1.png').load(),
    'V':Image.open('v1.png').load(),
    'W':Image.open('w1.png').load(),
    'X':Image.open('x1.png').load(),
    'Y':Image.open('y1.png').load(),
    'Z':Image.open('z1.png').load(),
    '0':Image.open('0.png').load(),
    '1':Image.open('1.png').load(),
    '2':Image.open('2.png').load(),
    '3':Image.open('3.png').load(),
    '4':Image.open('4.png').load(),
    '5':Image.open('5.png').load(),
    '6':Image.open('6.png').load(),
    '7':Image.open('7.png').load(),
    '8':Image.open('8.png').load(),
    '9':Image.open('9.png').load(),
    '`':Image.open('`.png').load(),
    '~':Image.open('~.png').load(),
    '!':Image.open('!.png').load(),
    '@':Image.open('@.png').load(),
    '#':Image.open('#.png').load(),
    '.':Image.open('dot.png').load(),
    ':':Image.open('colon.png').load(),
    '_':Image.open('_.png').load(),
    '-':Image.open('-.png').load(),
    '$':Image.open('$.png').load(),
    '%':Image.open('%.png').load(),
    '^':Image.open('^.png').load(),
    '&':Image.open('&.png').load(),
    '*':Image.open('*.png').load(),
    '(':Image.open('(.png').load(),
    ')':Image.open(').png').load(),
    '+':Image.open('+.png').load(),
    '=':Image.open('=.png').load(),
    '{':Image.open('{.png').load(),
    '}':Image.open('}.png').load(),
    '[':Image.open('[.png').load(),
    ']':Image.open('].png').load(),
    '\\':Image.open('\.png').load(),
    '|':Image.open('|.png').load(),
    ';':Image.open(';.png').load(),
    "'":Image.open("'.png").load(),
    '"':Image.open('".png').load(),
    '<':Image.open('<.png').load(),
    '>':Image.open('>.png').load(),
    ',':Image.open(',.png').load(),
    '/':Image.open('slash.png').load(),
    '?':Image.open('?.png').load()
    
    
    
    }

#give 10 by ten pixels and it will return closest matching letter
def findLet(pix, tolerance, shift,dark):
    proximity ={" ":0}
    for key in lets:
        proximity[key]=0
    for x in range(10):
        for y in range(10):
            pAvg = (pix[x+shift[0],y+shift[1]][0]+pix[x+shift[0],y+shift[1]][1]+pix[x+shift[0],y+shift[1]][2])/3
            pAvg+=dark
            for let in lets:
                lAvg = (lets[let][x,y][0]+lets[let][x,y][1]+lets[let][x,y][2])/3
                if abs((pAvg)-lAvg)<tolerance:
                    proximity[let]+=1
            if pAvg>=255:
                proximity[" "]+=1
    #print(proximity)
    greatest = ('',0)
    for key in proximity:
        if proximity[key]>greatest[1]:
            greatest = (key, proximity[key])
    return greatest[0]

def getAvg(pix, shift, dark):
    tAvg = 0
    for x in range(10):
        for y in range(10):
            pAvg = (pix[x+shift[0],y+shift[1]][0]+pix[x+shift[0],y+shift[1]][1]+pix[x+shift[0],y+shift[1]][2])/3
            pAvg+=dark
            tAvg+=pAvg
    return tAvg
    

def findLet2(pix, shift, dark):
    pAvg = getAvg(pix, shift, dark)
    closest = (' ',abs(255*100-pAvg))
    for key in lets:
        lAvg = getAvg(lets[key],(0,0),0)
        dif = abs(lAvg-pAvg)
        if dif<closest[1]:
            closest = (key, dif)
    return closest[0]
    
def convertPic2(im, dark):
    pixels  = im.load()
    x,y = im.size
    for yShift in range(y//10):
        for xShift in range(x//10):
            print(findLet2(pixels,(xShift*10,yShift*10),dark),end="")
        print()


def convertPic(im, tol, dark):
    tolerance = tol
    pixels  = im.load()
    x,y = im.size
    for yShift in range(y//10):
        for xShift in range(x//10):
            print(findLet(pixels, tolerance,(xShift*10,yShift*10),dark),end="")
        print()

def monaLisa():
    im = Image.open('monaLisa.jpg')
    convertPic(im, 40, 130)

monaLisa()
