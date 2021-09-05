import random
import turtle
import math
import winsound
import pymongo as py
from tkinter import *
myclient = py.MongoClient('mongodb://localhost:27017')
mydb = myclient['data']
mycol = mydb['account']


class GUI:
    def __init__(self, master, height, width, image):
        self.canvas = Canvas(master, height=height, width=width)
        self.canvas.pack()
        self.image = PhotoImage(file=image)
        self.label = Label(master, image=self.image)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

    def login(self, func, func1):
        self.frame = Frame(self.label, bg='white', bd=5)
        self.frame.place(relx=0.15, rely=0.05, relheight=0.1, relwidth=0.7)
        self.label1 = Label(self.frame, bg='yellow', text='LOGIN OR REGISTER', font=(
            'Comic Sans MS', 10, 'bold'))
        self.label1.place(relheight=1, relwidth=1, x=0, y=0)
        self.but = Button(self.label, text='LOGIN', font=(
            'Comic Sans MS', 10, 'bold'), command=func)
        self.but.place(relheight=0.4, relwidth=0.25, relx=0.2, rely=0.3)
        self.but1 = Button(self.label, text='REGISTER', font=(
            'Comic Sans MS', 10, 'bold'), command=func1)
        self.but1.place(relheight=0.4, relwidth=0.25, relx=0.5, rely=0.3)


class char(turtle.Turtle):
    def __init__(self, color, setx, sety, x=1, y=1, shape='triangle'):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.color(color)
        self.shape(shape)
        self.penup()
        self.shapesize(x, y)
        self.setposition(setx, sety)
        self.speed(0)
        self.lt(90)

    def moveright(self):
        x = self.xcor()
        x += 20
        if x > 180:
            x = 180
        self.setx(x)

    def moveleft(self):
        x = self.xcor()
        x -= 20
        if x < -180:
            x = -180
        self.setx(x)


class write(turtle.Turtle):
    def __init__(self, color, setx, sety, text):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.color(color)
        self.penup()
        self.setposition(setx, sety)
        self.write(text, False, align='left',
                   font=('Comic Sans MS', 20, 'bold'))
        self.hideturtle()


def iscollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) +
                         math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 23:
        return True
    else:
        return False


def btnclick1(t2):
    y = t2.ycor()
    if y < -270:
        return True
    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------------------
ro = Tk()


def login():
    def check():
        a = entr1.get()
        b = entr2.get()
        c = mycol.find_one({'name': a, 'pass': b})
        if c == None:
            label2 = Label(ro1, text='ACCOUNT NOT FOUND',
                           font=('Comic Sans MS', 8, 'bold'))
            label2.place(relx=0.1, rely=0.7, relheight=0.05, relwidth=0.8)
        else:
            ro.destroy()

            def game():
                wn = turtle.Screen()
                wn.title('Dodge')
                wn.setup(1366, 768)
                wn.bgcolor('orange')
                wn.bgpic('menubkg.png')

                def func(x, y):
                    if x >= -34 and x <= 61 and y >= -108 and y <= -89:
                        winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                        wn.clear()
                        dodge()

                    if x >= 292 and x <= 380 and y >= 5 and y <= 24:
                        winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                        c = mycol.find({}, {'name': 1, 'score': 1})
                        wn.clear()
                        sc = turtle.Screen()
                        sc.screensize(1366, 768)
                        sc.title('Dodge')
                        sc.bgcolor('orange')
                        line = char('yellow', -300, 300)
                        line.hideturtle()
                        line.pensize(3)
                        line.pendown()
                        line.rt(90)
                        line.fd(600)
                        line.penup()
                        c = mycol.find({}, {'_id': 0, 'name': 1, 'score': 1})
                        x, y = -200, 250
                        for i in c:
                            line.setposition(x, y)
                            line.write(str(i), False, align='left',
                                       font=('Comic Sans MS', 20, 'bold'))
                            y -= 30
                    if x >= -290 and x <= -220 and y >= 5 and y <= 24:
                        winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                        turtle.exitonclick()
                turtle.onscreenclick(func, '1')
                start = write('red', -33, -119, 'START')
                start = write('red', 290, -4, 'SCORE')
                start = write('red', -290, -6, 'EXIT')

                def dodge():
                    sc = turtle.Screen()
                    sc.title('Dodge')
                    sc.setup(1366, 768)
                    sc.bgcolor('orange')
                    sc.bgpic('menu.png')
                    sc.tracer(0)
                    sc.update()
                    self = turtle.Turtle()
                    self.color('black')
                    self.speed(0)
                    self.penup()
                    self.setposition(205, -300)
                    self.pendown()
                    for i in range(2):
                        self.lt(90)
                        self.fd(600)
                        self.lt(90)
                        self.fd(410)
                    self.hideturtle()
                    self.penup()
                    self.setposition(205, 300)
                    self.pendown()
                    for i in range(2):
                        self.lt(90)
                        self.fd(40)
                        self.lt(90)
                        self.fd(410)
                    player = char('white', 0, -270, 1, 1)
                    turtle.register_shape('basket.gif')
                    turtle.register_shape('bomb.gif')
                    turtle.register_shape('egg.gif')
                    player.shape('basket.gif')
                    turtle.onkey(player.moveright, 'd')
                    turtle.onkey(player.moveleft, 'a')
                    turtle.listen()
                    egg_no = 3
                    eggs = []
                    for i in range(egg_no):
                        eggs.append(char('white', random.randrange(-180, 180, 40),
                                         random.randrange(180, 280, 20), 1, 1, 'egg.gif'))
                    bomb_no = 3
                    bombs = []
                    for i in range(bomb_no):
                        bombs.append(char('white', random.randrange(-180, 180, 30),
                                          random.randrange(180, 280, 20), 1, 1, 'bomb.gif'))
                    score = write('black', -200, 307, 'Score:0')
                    core = 0
                    ask = True
                    while ask:
                        sc.update()
                        for egg in eggs:
                            y = egg.ycor()
                            y -= 0.1
                            egg.sety(y)
                            if btnclick1(egg):
                                egg.setposition(
                                    random.randrange(-180, 180, 40), random.randrange(180, 280, 20))
                            if iscollision(player, egg):
                                winsound.PlaySound(
                                    'egg.wav', winsound.SND_ASYNC)
                                egg.setposition(
                                    random.randrange(-180, 180, 40), random.randrange(180, 280, 20))
                                core += 1
                                score.clear()
                                score.write('Score:{}'.format(core), False, align='left', font=(
                                    'Comic Sans MS', 20, 'bold'))
                        for bomb in bombs:
                            y = bomb.ycor()
                            y -= 0.16
                            bomb.sety(y)
                            if btnclick1(bomb):
                                bomb.setposition(
                                    random.randrange(-180, 180, 40), random.randrange(180, 280, 20))
                            if iscollision(player, bomb):
                                winsound.PlaySound(
                                    'bomb.wav', winsound.SND_ASYNC)
                                bomb.setposition(
                                    random.randrange(-180, 180, 40), random.randrange(180, 280, 20))
                                ask = False
                    sc.clear()
                    sc.title('Dodge')
                    sc.setup(1366, 768)
                    sc.bgcolor('orange')
                    sc.bgpic('1306995.png')
                    final = write('white', -50, 300,
                                  'Your Score:{}'.format(core))
                    if c['score'] <= core:
                        mycol.update_one({'name': a, 'pass': b}, {
                                         '$set': {'score': core}})

                    def func(x, y):
                        if x >= -130 and x <= -66 and y >= -254 and y <= -231:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            sc.clear()
                            dodge()

                        if x >= 86 and x <= 129 and y >= -256 and y <= -231:
                            winsound.PlaySound('btcl.wav', winsound.SND_ASYNC)
                            turtle.exitonclick()
                    turtle.onscreenclick(func, '1')
                turtle.listen()
                turtle.done()
            game()
    ro1 = Toplevel()
    ro1.resizable(False, False)
    ro1.title('login')
    login1 = GUI(ro1, 400, 400, 'bkg.png')
    label2 = Label(ro1, text='NAME', font=('Comic Sans MS', 8, 'bold'))
    label2.place(relx=0.1, rely=0.25, relheight=0.05, relwidth=0.1)
    label3 = Label(ro1, text='PASS', font=('Comic Sans MS', 8, 'bold'))
    label3.place(relx=0.1, rely=0.3, relheight=0.05, relwidth=0.1)
    entr1 = Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
    entr1.place(relx=0.4, rely=0.25, relheight=0.04, relwidth=0.5)
    entr2 = Entry(ro1, show='*', font=('Comic Sans MS', 8, 'bold'))
    entr2.place(relx=0.4, rely=0.3, relheight=0.04, relwidth=0.5)
    button1 = Button(ro1, text='login', font=(
        'Comic Sans MS', 8, 'bold'), bg='orange', command=check)
    button1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.58)
    ro1.mainloop()


def register():

    def check():
        a = entr1.get()
        b = entr2.get()
        c = mycol.find_one({'name': a})
        if c == None:
            x = mycol.insert_one({'name': a, 'pass': b, 'score': 0})
            ro1.destroy()

        else:
            label2 = Label(ro1, text='Your Account Name already exists', font=(
                'Comic Sans MS', 8, 'bold'))
            label2.place(relx=0.1, rely=0.7, relheight=0.05, relwidth=0.8)

    ro1 = Toplevel()
    ro1.resizable(False, False)
    ro1.title('login')
    login1 = GUI(ro1, 400, 400, 'bkg.png')
    label2 = Label(ro1, text='NAME', font=('Comic Sans MS', 8, 'bold'))
    label2.place(relx=0.1, rely=0.25, relheight=0.05, relwidth=0.1)
    label3 = Label(ro1, text='PASS', font=('Comic Sans MS', 8, 'bold'))
    label3.place(relx=0.1, rely=0.3, relheight=0.05, relwidth=0.1)
    entr1 = Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
    entr1.place(relx=0.4, rely=0.25, relheight=0.04, relwidth=0.5)
    entr2 = Entry(ro1, show='*', font=('Comic Sans MS', 8, 'bold'))
    entr2.place(relx=0.4, rely=0.3, relheight=0.04, relwidth=0.5)
    button1 = Button(ro1, text='login', font=(
        'Comic Sans MS', 8, 'bold'), bg='orange', command=check)
    button1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.58)
    ro1.mainloop()


ro.resizable(False, False)
ro.title('login or register')
app = GUI(ro, 400, 400, 'bkg.png')
app.login(login, register)
ro.mainloop()
