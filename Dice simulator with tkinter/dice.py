import tkinter as tk
import winsound
import random


def simulator():
    def two():
        def roll():
            winsound.PlaySound('DICE.wav', winsound.SND_ASYNC)
            lt = []
            for i in range(2):
                t = random.randint(1, 6)
                lt.append(t)
            label.configure(text='{} Roll Again!!'.format(lt))

        ro1 = tk.Toplevel()
        ro1.resizable(False, False)
        ro1.title('diceRoller')
        canvas = tk.Canvas(ro1, height=300, width=200)
        canvas.pack()
        label1 = tk.Label(ro1)
        label1.place(x=0, y=0, relheight=0.5, relwidth=1)
        button1 = tk.Button(ro1, text='roll', font=(
            'Comic Sans MS', 8, 'bold'), bg='orange', command=roll)
        button1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.58)
        label = tk.Label(ro1, font=('Comic Sans MS', 10, 'normal'))
        label.place(relx=0.3, rely=0.8)

        def image(i):
            frame = frames[i]
            i += 1
            if i == 12:
                i = 0
            label1.configure(image=frame)
            ro1.after(100, image, i)
        ro1.after(0, image, 0)

        ro1.mainloop()

    def one():
        def roll():
            winsound.PlaySound('DICE.wav', winsound.SND_ASYNC)
            t = random.randint(1, 6)
            label.configure(text='{} Roll Again!!'.format(t))

        ro1 = tk.Toplevel()
        ro1.title('diceRoller')
        ro1.resizable(False, False)
        canvas = tk.Canvas(ro1, height=300, width=200)
        canvas.pack()
        label1 = tk.Label(ro1)
        label1.place(x=0, y=0, relheight=0.5, relwidth=1)
        button1 = tk.Button(ro1, text='roll', font=(
            'Comic Sans MS', 8, 'bold'), bg='orange', command=roll)
        button1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.58)
        label = tk.Label(ro1, font=('Comic Sans MS', 10, 'normal'))
        label.place(relx=0.3, rely=0.8)

        def image(i):
            frame = frames1[i]
            i += 1
            if i == 12:
                i = 0
            label1.configure(image=frame)
            ro1.after(100, image, i)
        ro1.after(0, image, 0)

        ro1.mainloop()

    def choice():

        ro1 = tk.Toplevel()
        ro1.resizable(False, False)
        canvas = tk.Canvas(ro1, height=300, width=200)
        canvas.pack()
        label1 = tk.Label(ro1, text='set probability',
                          font=('Comic Sans MS', 8, 'bold'))
        label1.place(relx=0, rely=0.04, relheight=0.14, relwidth=1)
        label2 = tk.Label(ro1, text='1', font=('Comic Sans MS', 8, 'bold'))
        label2.place(relx=0.01, rely=0.2, relheight=0.14, relwidth=0.14)
        label3 = tk.Label(ro1, text='2', font=('Comic Sans MS', 8, 'bold'))
        label3.place(relx=0.01, rely=0.3, relheight=0.14, relwidth=0.14)
        label4 = tk.Label(ro1, text='3', font=('Comic Sans MS', 8, 'bold'))
        label4.place(relx=0.01, rely=0.4, relheight=0.14, relwidth=0.14)
        label5 = tk.Label(ro1, text='4', font=('Comic Sans MS', 8, 'bold'))
        label5.place(relx=0.01, rely=0.5, relheight=0.14, relwidth=0.14)
        label6 = tk.Label(ro1, text='5', font=('Comic Sans MS', 8, 'bold'))
        label6.place(relx=0.01, rely=0.6, relheight=0.14, relwidth=0.14)
        label7 = tk.Label(ro1, text='6', font=('Comic Sans MS', 8, 'bold'))
        label7.place(relx=0.01, rely=0.7, relheight=0.14, relwidth=0.14)

        entr1 = tk.Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
        entr1.place(relx=0.2, rely=0.25, relheight=0.04, relwidth=0.5)
        entr2 = tk.Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
        entr2.place(relx=0.2, rely=0.35, relheight=0.04, relwidth=0.5)
        entr3 = tk.Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
        entr3.place(relx=0.2, rely=0.45, relheight=0.04, relwidth=0.5)
        entr4 = tk.Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
        entr4.place(relx=0.2, rely=0.55, relheight=0.04, relwidth=0.5)
        entr5 = tk.Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
        entr5.place(relx=0.2, rely=0.65, relheight=0.04, relwidth=0.5)
        entr6 = tk.Entry(ro1, font=('Comic Sans MS', 8, 'bold'))
        entr6.place(relx=0.2, rely=0.75, relheight=0.04, relwidth=0.5)

        def roll(a, b, c, d, e, f):
            lt = []
            for i in (a, b, c, d, e, f):
                lt.append(float(i))

            def roll1():
                winsound.PlaySound('DICE.wav', winsound.SND_ASYNC)
                t = random.choices(list(range(1, 7)), weights=lt)
                label.configure(text='{} Roll Again!!'.format(t[0]))

            ro1 = tk.Toplevel()

            ro1.title('diceRoller')
            ro1.resizable(False, False)
            canvas = tk.Canvas(ro1, height=300, width=200)
            canvas.pack()
            label1 = tk.Label(ro1)
            label1.place(x=0, y=0, relheight=0.5, relwidth=1)
            button1 = tk.Button(ro1, text='roll', font=(
                'Comic Sans MS', 8, 'bold'), bg='orange', command=roll1)
            button1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.58)
            label = tk.Label(ro1, font=('Comic Sans MS', 10, 'normal'))
            label.place(relx=0.3, rely=0.8)

            def image(i):
                frame = frames1[i]
                i += 1
                if i == 12:
                    i = 0
                label1.configure(image=frame)
                ro1.after(100, image, i)
            ro1.after(0, image, 0)
            ro1.mainloop()
        button1 = tk.Button(ro1, text='set', font=('Comic Sans MS', 8, 'bold'), bg='orange', command=lambda: roll(
            entr1.get(), entr2.get(), entr3.get(), entr4.get(), entr5.get(), entr6.get()))
        button1.place(relheight=0.05, relwidth=0.1, relx=0.46, rely=0.85)

    ro = tk.Tk()

    ro.title('diceRoller')
    ro.resizable(False, False)
    canvas = tk.Canvas(ro, height=400, width=300)
    canvas.pack()
    bg = tk.PhotoImage(file='Whatsapp-Wallpaper-102.png')
    label = tk.Label(ro, image=bg)
    label.place(x=0, y=0, relheight=1, relwidth=1)
    frame = tk.Frame(ro, bg='DarkSlateGray1', bd=5)
    frame.place(relx=0.04, rely=0.15, relheight=0.8, relwidth=0.92)
    frame1 = tk.Frame(ro, bg='white')
    frame1.place(relx=0.04, rely=0.01, relheight=0.1, relwidth=0.92)
    label1 = tk.Label(frame1, text='Dice Simulator',
                      font=('Comic Sans MS', 20, 'bold'))
    label1.place(relheight=1, relwidth=1)
    frames = [tk.PhotoImage(file='animated-dice-image-0015.gif',
                            format='gif -index {}'.format(i)) for i in range(12)]
    frames1 = [tk.PhotoImage(file='animated-dice-image-0012.gif',
                             format='gif -index {}'.format(i)) for i in range(12)]
    button1 = tk.Button(frame, text='roll two dice', font=(
        'Comic Sans MS', 8, 'bold'), bg='orange', command=two)
    button1.place(relheight=0.5, relwidth=0.5, relx=0, rely=0)

    def image(i):
        frame = frames[i]
        i += 1
        if i == 12:
            i = 0
        button1.configure(image=frame)
        ro.after(100, image, i)
    ro.after(0, image, 0)
    button2 = tk.Button(frame, text='roll one dice', font=(
        'Comic Sans MS', 8, 'bold'), bg='yellow', command=one)
    button2.place(relheight=0.5, relwidth=0.5, relx=0.5, rely=0)

    def image1(i):
        frame = frames1[i]
        i += 1
        if i == 12:
            i = 0
        button2.configure(image=frame)
        ro.after(100, image1, i)
    ro.after(0, image1, 0)
    text = '''roll dice on the basis of your
probability of occuring'''
    button3 = tk.Butto
