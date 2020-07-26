import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial
import threading
import imutils
import time


stream = cv2.VideoCapture("clip.mp4")
flag = True
    
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag

def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # 2. Wait for 1 second
    time.sleep(1.5)

    # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("github.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 second
    time.sleep(2.5)
    # 5. Display out/notout image
    if decision == 'out':
        decisionImg = "out.jpg"
    else:
        decisionImg = "not_out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not_out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

SET_WIDTH = 650
SET_HEIGHT = 364
# GUI OF Tkinter
window = tkinter.Tk()
window.title("DHONI REVIEW SYSTEM")
cv_img = cv2.cvtColor(cv2.imread("ground.jfif"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()
canvas.pack()


# Buttons to Control the PlayBack
btn = tkinter.Button(window, text="Play",width=50, bg='slate blue', command=partial(play,0))
btn.pack()
btn = tkinter.Button(window, text="<< Previous (Fast)",width=50, bg='yellow', command=partial(play, -20))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (Slow)",width=50, bg='azure', command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (Fast) >>", width=50,bg='cyan2', command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Next (Slow) >>", width=50,bg='purple3', command=partial(play, 15))
btn.pack()

btn = tkinter.Button(window, text="OUT", width=50, bg='tomato2', command=out)
btn.pack()

btn = tkinter.Button(window, text="NOT OUT", width=50,bg='green yellow', command=not_out)
btn.pack()



window.mainloop()
