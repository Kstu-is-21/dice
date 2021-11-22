from PIL import ImageTk,Image
import tkinter as tk
import random
import pygame

#First commit (Create Canvas)
r = tk.Tk()
r.geometry('700x700')
r.title('Игра кости')

c = tk.Canvas(r, width=700, height=700)
c.pack()

i = ''

#Second commit (roll_dice function)
def roll_dice():
    global img,i,bttn_clicks
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}')
    c.create_window(350, 250, window=ldice)
    res = d[die1]+d[die2]
    label2.configure(text="Ты получил  "+str(res))
    bttn_clicks += 1
    label1['text'] = "Кости были брошены: " + str(bttn_clicks) + " раз(а)"

#Third commit (restart function)
def restart():
    global bttn_clicks
    global i
    bttn_clicks= 0
    label1.configure(text="")
    label2.configure(text="None")
    pygame.mixer.init()
    pygame.mixer.music.stop()
    if i:
        c.delete(i)
    rollbutton.configure(state='normal')

#Fourth commit (Rendering)
ldice = tk.Label(r, text='', font=('Times', 120),fg='green')
rollbutton = tk.Button(r, text='Кинуть кости', font=('times', 20,"bold"),state="disabled",background="brown",foreground='yellow',height=1, width=20, command=roll_dice)
c.create_window(350, 120, window=rollbutton)
button1 = tk.Button(r, text='Начало/Перезапуск игры', font=('times', 20,"bold"),background="blue",foreground='white',height=1, width=20, command=restart)
c.create_window(350, 50, window=button1)
label1 = tk.Label(r, text='', font=('Times',20,'bold'),fg='brown')
c.create_window(180, 550, window=label1)
label2 = tk.Label(r, text='None', font=('Times',20,'bold'),bg='purple',fg='yellow',width=12)
c.create_window(480, 550, window=label2)



r.mainloop()