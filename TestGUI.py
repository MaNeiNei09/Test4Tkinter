#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
# Pyhton GUI V0.1.1
# date = 2018.09.16
# author = zbh
'''
import tkinter as tk

window = tk.Tk()
window.title('我是无聊的小胖纸')
window.geometry('200x100')

var = tk.StringVar()

l = tk.Label(window,
             textvar=var,
             bg='white',
             font=('Arial',12),
             width=15,
             height=2)
l.pack()

on_hit = 0

def hit_me():
    global on_hit
    if on_hit == 0:
        on_hit = 1
        var.set('Hello,媳妇')
    elif on_hit == 1:
        on_hit = 2
        var.set('我爱你')
    else:
        var.set('你最美')


b = tk.Button(window,
              text='点点我',
              width=5,
              height=5,
              command=hit_me)
b.pack()

window.mainloop()