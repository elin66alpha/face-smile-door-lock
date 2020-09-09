import tkinter as tk
import cv2
import smile
import numpy as np
import sys

font1 = cv2.FONT_HERSHEY_SIMPLEX
HEIGHT = 480
WIDTH = 640
n=0

def read(entry):
    if not entry == "":
        label1['text'] = "you're {}!".format(entry)
        names = entry
        f = open("./names.txt","a")
        f.write("{}\n".format(names))
        cheese()
        return entry
    else:
        label1['text'] = "tell me your name!"
        return 0

def cheese():
    cap = cv2.VideoCapture(0)
    name = entry.get()
    while (name != 0):
        ret, frame = cap.read()       
        cv2.imshow("press enter to take picture", frame)
        if cv2.waitKey(1) & 0xFF == ord('\r'):
            cv2.imwrite("./image/"+name+".jpg", frame)
            entry.delete(0, tk.END)
            break
        label2['text'] = "tell me another name!"
    cap.release()
    cv2.destroyAllWindows()

def smileface():
    with open('names.txt','r') as f:
        nameslist = [line.strip() for line in f]
    if len(nameslist)== 0:
        label2['text'] = "put you name first!"
    else:
        smile.main()
        label2['text'] = "running"


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1fa', bd=5)
frame.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')

entry = tk.Entry(frame, font=160)
entry.place(relx=0,rely=0,relwidth=0.5, relheight=0.5)


button1 = tk.Button(frame, text="record your name", font=160,command=lambda:read(entry.get()))
button1.place(relx=0.6, rely=0,relheight=0.3, relwidth=0.4)

button3 = tk.Button(frame,text="face and smile recgonition", font=160,command=lambda:smileface())
button3.place(relx=0.6, rely=0.6,relheight=0.3, relwidth=0.4)

label1 = tk.Label(frame, font=160)
label1.place(relx=0, rely=0.5,relwidth=0.5, relheight=0.25)
label2 = tk.Label(frame, font=160)
label2.place(relx=0, rely=0.75,relwidth=0.5, relheight=0.25)
label3 = tk.Label(frame, font=160)
label3.place(relx=0.6, rely=0.3,relwidth=0.4, relheight=0.3)
label3['text'] = "english name only\nprogram for fun and learning\nprogrammer：elin"
root.mainloop()
