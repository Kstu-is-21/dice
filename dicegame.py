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