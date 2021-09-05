from tkinter import *
from tkinter import filedialog
from cv2 import *
import moviepy.editor as mv
import time
from ffpyplayer.player import MediaPlayer
import numpy as np
useOptimized()
class GUI:
    def __init__(self,master,h,w,img):
        self.master=master
        self.canvas=Canvas(master,height=h,width=w)
        self.canvas.pack()
        self.image=PhotoImage(file=img)
        self.label=Label(self.canvas,image=self.image)
        self.label.place(x=0,y=0,relwidth=1,relheight=1)
#-------------------------------------------------------------------------------------------------------------------------IMAGE FUNCTION
def showimage(path):
    a=imread(r'{}'.format(path),1)
    x,y,z=a.shape
    if x>768:
        if y>1366:
            img=resize(a,(1366,768))
        else:
            img=resize(a,(1366,x))
    else:
        if y>1366:
            img=resize(a,(y,768))
        else:
            img=a
    imshow('image',img)
    
def winsearch():
    ro=Toplevel()
    ro.transient(root)
    a=GUI(ro,400,600,'but1.png')
    ro.resizable(False,False)
    frame=Frame(ro,bg='sienna1',bd=5)
    frame.place(relx=0.35,rely=0,relheight=0.06,relwidth=0.3)
    label1=Label(frame,bg='Antiquewhite1',text='Open Image',fg='sienna1',font=('Comic Sans MS', 10, 'bold'))
    label1.place(relheight=1,relwidth=1)
    entr1=Entry(ro,font=('Comic Sans MS',10,'normal'),text='Enter image address')
    entr1.focus()
    entr1.place(rely=0.35,relx=0.2,relwidth=0.6,relheight=0.06)
    frame1=Frame(ro,bg='DarkGoldenrod1',bd=3)
    frame1.place(relx=0.3,rely=0.44,relheight=0.06,relwidth=0.4)
    def openfile():
        try:
            filename=filedialog.askopenfilename(initialdir='/',title='Select a file')
            showimage(filename)
        except:
            label1=Label(ro,bg='Antiquewhite1',text='mentioned image is not retrievable',fg='sienna1',font=('Comic Sans MS', 15, 'bold'))
            label1.place(rely=0.55,relx=0.2,relheight=0.06,relwidth=0.6)
        finally:
            entr1.delete(0,'end')

            
    def search():
        filename=entr1.get()
        try:
            showimage(filename)
        except:
            label1=Label(ro,bg='Antiquewhite1',text='mentioned address is not retrievable',fg='sienna1',font=('Comic Sans MS', 15, 'bold'))
            label1.place(rely=0.55,relx=0.2,relheight=0.06,relwidth=0.6)
        finally:
            entr1.delete(0,'end')
            
        
        
    button=Button(frame1,text='Browse',fg='sienna2',bg='Antiquewhite2',font=('Comic Sans MS', 10, 'bold'),command=openfile)
    button.place(relheight=1,relwidth=0.5)
    button1=Button(frame1,text='search',fg='sienna2',bg='Antiquewhite2',font=('Comic Sans MS', 10, 'bold'),command=search)
    button1.place(relx=0.5,relheight=1,relwidth=0.5)
    
    
    
    ro.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------VIDEO FUNCTION
def playvideo(path):
    a=VideoCapture(r'{}'.format(path))
    video = mv.VideoFileClip(path)
    video_duration=int(video.duration)
    fps = a.get(cv2.CAP_PROP_FPS)
    time1=(1-0.0064*fps)/fps
    player=MediaPlayer(r'{}'.format(path))
    while True:
        check,frame=a.read()
        if check==False:
            break
        if cv2.waitKey(1)==13:
            break
        imshow('video',frame)
        audio_frame, val = player.get_frame()
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
        time.sleep(time1)   
    a.release()
    destroyAllWindows()
    
def openvid():
    ro=Toplevel()
    ro.transient(root)
    a=GUI(ro,400,600,'but2.png')
    ro.resizable(False,False)
    frame=Frame(ro,bg='sienna1',bd=5)
    frame.place(relx=0.35,rely=0,relheight=0.06,relwidth=0.3)
    label1=Label(frame,bg='Antiquewhite1',text='Open Video',fg='sienna1',font=('Comic Sans MS', 10, 'bold'))
    label1.place(relheight=1,relwidth=1)
    entr1=Entry(ro,font=('Comic Sans MS',10,'normal'),text='Enter image address')
    entr1.focus()
    entr1.place(rely=0.35,relx=0.2,relwidth=0.6,relheight=0.06)
    frame1=Frame(ro,bg='DarkGoldenrod1',bd=3)
    frame1.place(relx=0.3,rely=0.44,relheight=0.06,relwidth=0.4)
    def openfile():
        try:
            filename=filedialog.askopenfilename(initialdir='/',title='Select a file')

            playvideo(filename)
        except:
            label1=Label(ro,bg='Antiquewhite1',text='mentioned image is not retrievable',fg='sienna1',font=('Comic Sans MS', 15, 'bold'))
            label1.place(rely=0.55,relx=0.2,relheight=0.06,relwidth=0.6)

            
    def search():
        b=entr1.get()
        try:
            playvideo(b)
        except:
            label1=Label(ro,bg='Antiquewhite1',text='mentioned address is not retrievable',fg='sienna1',font=('Comic Sans MS', 15, 'bold'))
            label1.place(rely=0.55,relx=0.2,relheight=0.06,relwidth=0.6)
            
        
        
    button=Button(frame1,text='Browse',fg='sienna2',bg='Antiquewhite2',font=('Comic Sans MS', 10, 'bold'),command=openfile)
    button.place(relheight=1,relwidth=0.5)
    button1=Button(frame1,text='search',fg='sienna2',bg='Antiquewhite2',font=('Comic Sans MS', 10, 'bold'),command=search)
    button1.place(relx=0.5,relheight=1,relwidth=0.5)
    ro.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------draw plane

def drawing():
    global ix,iy,drawing,mode
    def nothing(x):
        pass
    namedWindow('img')
    draw='draw'
    bgcolor='ChngBG'
    createTrackbar(draw,'img',0,1,nothing)
    createTrackbar(bgcolor,'img',0,1,nothing)
    createTrackbar('Paint:Red','img',0,255,nothing),createTrackbar('Paint:Blue','img',0,255,nothing),createTrackbar('Paint:Gr','img',0,255,nothing)
    createTrackbar('BG:Red','img',0,255,nothing),createTrackbar('BG:Blue','img',0,255,nothing),createTrackbar('BG:Gr','img',0,255,nothing)
    drawing=False
    ix=iy=0,0
    def mousefunc(event,x,y,flag,param):
        r=getTrackbarPos('Paint:Red','img')
        g=getTrackbarPos('Paint:Gr','img')
        b=getTrackbarPos('Paint:Blue','img')
        global ix,iy,drawing,mode
        if event==EVENT_LBUTTONDOWN:
            drawing=True
            ix,iy=x,y
        elif event==EVENT_MOUSEMOVE:
            if drawing==True:
                circle(img,(x,y),5,(b,g,r),-1)
        elif event==EVENT_LBUTTONUP:
            drawing = False
            circle(img,(x,y),5,(b,g,r),-1)
    img=np.zeros((700,1200,3),np.uint8)
    img[:]=255
    namedWindow('image')
    setMouseCallback('image',mousefunc)
    resizeWindow('img',300,100)
    while True:
        imshow('image',img)
        if cv2.waitKey(1)==13:
            break
        s=getTrackbarPos(draw,'img')
        bg=getTrackbarPos(bgcolor,'img')
        r1=getTrackbarPos('BG:Red','img')
        g1=getTrackbarPos('BG:Gr','img')
        b1=getTrackbarPos('BG:Blue','img')
        if s==0:
            img[:]=255
        if bg==1:
            img[:]=[b1,g1,r1]
        if cv2.waitKey(1)==19:
            files = [('Text Document', '*.png')] 
            file = asksaveasfile(filetypes = files, defaultextension = files)
            
    destroyAllWindows()
    
            
    
#main-------------------------------------------------------------------------------------------------------------------------------------------------------        
root=Tk()
a=GUI(root,768,1366,'bg1.png')
frame=Frame(root,bg='sienna1',bd=5)
frame.place(relx=0,rely=0,relheight=0.06,relwidth=0.3)
label1=Label(frame,bg='Antiquewhite1',text='M U L T I P U R P O S E   A P P',fg='sienna1',font=('Comic Sans MS', 15, 'bold'))
label1.place(relheight=1,relwidth=1)
img1=PhotoImage(file='but1.png')
frame1=Frame(root,bg='DarkGoldenrod1',bd=3)
frame1.place(relx=0.05,rely=0.15,relheight=0.09,relwidth=0.2)
openimg=Button(frame1,text='O P E N  I M A G E',fg='sienna2',bg='Antiquewhite2',font=('Comic Sans MS', 10, 'bold'), command=winsearch)
openimg.place(relheight=1,relwidth=1)
frame1=Frame(root,bg='pale turquoise',bd=3)
frame1.place(relx=0.08,rely=0.3,relheight=0.09,relwidth=0.2)
openvid=Button(frame1,text='O P E N  V I D E O',fg='SlateBlue1',bg='thistle1',font=('Comic Sans MS', 10, 'bold'), command=openvid)
openvid.place(relheight=1,relwidth=1)
frame1=Frame(root,bg='coral1',bd=3)
frame1.place(relx=0.11,rely=0.45,relheight=0.09,relwidth=0.2)
draw_plane=Button(frame1,text='D R A W',fg='salmon3',bg='khaki1',font=('Comic Sans MS', 10, 'bold'), command=drawing)
draw_plane.place(relheight=1,relwidth=1)



root.mainloop()
