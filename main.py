import tkinter
import cv2
import PIL.Image
import PIL.ImageTk
from functools import partial


def play(speed):
    print(f"You Clicked on play and speed is {speed}")


def out():
    print("Out")


def not_out():
    print("Not Out")


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
