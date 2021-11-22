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
