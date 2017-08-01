from Tkinter import *
import os 
root = Tk()


def Untrained(event):
	print "Un"
	os.system("python /home/anupam/Desktop/pygame/RL.py")
def Trained(event):
	print "Tra"
	os.system("python train-atari.py --task play --env Pong-v0 --load Pong-v0.tfmodel")
def Trained100(event):
	print "100"
	os.system("python3 -m baselines.deepq.experiments.atari.enjoy --model-dir /home/anupam/Desktop/tmp/models/model-atari-pong-1 --env Pong")
	
def Coaster(event):
	print "Coas"
	os.system("python train-atari.py --task play --env SpaceInvaders-v0 --load SpaceInvaders-v0.tfmodel")

def Pong(event):
	print "Coas"
	os.system("python train-atari.py --task play --env Pong-v0 --load Pong-v0.tfmodel")




frame = Frame(root)
frame.grid()
Label1 = Label(root, text = "Game of Pong")
Label1.grid(row = 0, column = 2)
#Label1.pack(side = LEFT)

photo1 = PhotoImage(file = 'pong.png')
label2 = Label(root, image = photo1)
label2.grid(row = 1, column = 2) 

button1 = Button(root, text = "Untrained", fg = "red",)
button1.grid(row = 2, column = 0,)
button1.bind("<Button-1>", Untrained)
#button1.pack(side = BOTTOM)
button2 = Button(root, text = "Trained", fg = "blue")
button2.grid(row = 2, column = 2, ipadx = 9)
button2.bind("<Button-1>", Trained)

button3 = Button(root, text = "100% Trained", fg = "green")
button3.grid(row = 2, column = 5)
button3.bind("<Button-1>", Trained100)

Label3 = Label(root, text = "Game of Space invader")
Label3.grid(row = 10, column = 2)

photo2 = PhotoImage(file = 'coas.png')
label4 = Label(root, image = photo2)
label4.grid(row = 11, column = 2) 

button4 = Button(root, text = "PLAY SPACE INVADER", fg = "green")
button4.grid(row = 12, column = 2)
button4.bind("<Button-1>", Coaster)

'''button4 = Button(root, text = "PLAY PONG", fg = "green")
button4.grid(row = 12, column = 4)
button4.bind("<Button-1>", Pong)
'''
#frame.pack()
root.minsize(320,300)
root.mainloop()
