import tkinter
from tkinter.constants import ANCHOR
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import time
import imutils

stream =cv2.VideoCapture("video2.mp4")
SET_WIDTH =800
SET_LENTH = 500
def play(speed):
    print(f"you clicked on play.your speed is {speed}")
    
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES ,frame1+ speed)

    grabbed, frame =stream.read()
    frame =imutils.resize(frame ,width =SET_WIDTH, height =SET_LENTH)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0,image = frame,anchor =tkinter.NW)
    canvas.create_text(128,25,fill="black",font="times 20  bold" , text ="Decision Pending")

def pending(decision):
    # display pending image
    frame =cv2.cvtColor(cv2.imread("pending.jpg"),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width =SET_WIDTH,height =SET_LENTH)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image =frame,anchor = tkinter.NW)
    time.sleep(1)
    # display sponsor image
    frame =cv2.cvtColor(cv2.imread("sponsor.jpg"),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width =SET_WIDTH,height =SET_LENTH)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image =frame,anchor = tkinter.NW)
    time.sleep(2)
    # give decision
    if decision =='out':
        dic = "out.jpg"
    else:
        dic = "not out.jpg"
    frame =cv2.cvtColor(cv2.imread(dic),cv2.COLOR_BGR2RGB)
    frame= imutils.resize(frame,width =SET_WIDTH,height =SET_LENTH)
    frame =PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image =frame
    canvas.create_image(0,0, image =frame,anchor = tkinter.NW)
    time.sleep(1)


def out():
    thread =threading.Thread(target=pending ,args=("out",))
    thread.daemon =1
    thread.start()
    print("player is out")
    
def notout():

    thread =threading.Thread(target=pending ,args=("not out",))
    thread.daemon =1
    thread.start()
    print("player is out")
    

window = tkinter.Tk()
window.title("third umpire system")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpeg"),cv2.COLOR_BGR2RGB)
canvas =tkinter.Canvas(window,width=SET_WIDTH,height =SET_LENTH)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas =canvas.create_image(0,0,anchor = tkinter.NW,image = photo)
canvas.pack()
# button to control
btn =tkinter.Button(window,text="<<previous (fast)",width=50 ,command= partial(play,-25))
btn.pack()
btn =tkinter.Button(window,text="<<previous (slow)",width=50, command=partial(play,-2))
btn.pack()
btn =tkinter.Button(window,text="next (fast)>>",width=50,command= partial(play,25))
btn.pack()
btn =tkinter.Button(window,text="next (slow)>>",width=50,command= partial(play,5))
btn.pack()
btn =tkinter.Button(window,text="give OUT",width=50, command=out)
btn.pack()
btn =tkinter.Button(window,text="give NOTOUT",width=50, command=notout)
btn.pack()


window.mainloop()

