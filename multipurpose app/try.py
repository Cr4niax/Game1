from cv2 import *
import time
from ffpyplayer.player import MediaPlayer
import moviepy.editor as mv
useOptimized()
filename="C:\\Users\\PC\\Downloads\\AMONG US NEW PROXIMITY CHAT FUNNY HIGHLIGHTS __ PART 2.mp4"
a=VideoCapture(r'{}'.format(filename))
player=MediaPlayer(r'{}'.format(filename))
video = mv.VideoFileClip(filename)
video_duration=int(video.duration)
fps = a.get(cv2.CAP_PROP_FPS)
print(fps)
t2=time.time()
check,frame=a.read()
x,y,z=frame.shape
if x>768:
    if y>1366:
        img=resize(frame,(1366,768))
    else:
        img=resize(frame,(1366,x))
else:
    if y>1366:
        img=resize(frame,(y,768))
    else:
        img=frame
if cv2.waitKey(1)==13:
    pass
imshow('video',img)
t1=time.time()
audio_frame, val = player.get_frame()
if val != 'eof' and audio_frame is not None:
        #audio
        img, t = audio_frame
print(t1-t2)                   

a.release()
destroyAllWindows()

