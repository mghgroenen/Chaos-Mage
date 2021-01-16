#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
import random


window = tk.Tk()
window.geometry("640x360")
window.resizable(False, False)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.title("Chaos Mage")

font = "Cambria"
button_relief=tk.RAISED

#----------Functions---------------------------
def reset():
    global spell_list
    spell_list = [1,2,3,4,5,6]

    button_attack1.config(bg="red", fg="white", relief=tk.RAISED)
    button_attack2.config(bg="red", fg="white", relief=tk.RAISED)
    button_defense1.config(bg="blue", fg="white", relief=tk.RAISED)
    button_defense2.config(bg="blue", fg="white", relief=tk.RAISED)
    button_iconic1.config(bg="purple", fg="white", relief=tk.RAISED)
    button_iconic2.config(bg="purple", fg="white", relief=tk.RAISED)
    
    create_upcoming()
    label_arrow.grid_forget()

def next_spell():
    global upcoming
    if len(spell_list) > 0:
        upcoming = spell_list.pop(random.randint(0,len(spell_list)-1))
    else:
        upcoming = 0
        label_arrow.grid(row=0, column=0, padx=(0,10), sticky="e")
    label_upcoming.destroy()
    create_upcoming(upcoming)

#------------Display frames--------------
display = tk.Frame(master=window, bg="#404040", relief=tk.RIDGE, borderwidth=7)
display.pack(expand=True, fill=tk.BOTH)
display.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

display2 = tk.Frame(master=window, bg="#404040", relief=tk.RIDGE, borderwidth=7)
display2.pack(expand=True, fill=tk.BOTH)
display2.grid_columnconfigure((1), weight=1)

display3 = tk.Frame(master=display2, bg="#404040")
display3.grid(column=0, row=0)

display4 = tk.Frame(master=display2, bg="#404040")
display4.grid(column=1, row=0)

display5 = tk.Frame(master=display4, bg="#404040")
display5.grid(column=1, row=1, sticky="e")

#------------Spel labels----------------------
def create_stones():
    global button_attack1
    global button_attack2
    global button_defense1
    global button_defense2
    global button_iconic1
    global button_iconic2
    
    button_attack1 = tk.Label(master=display, 
                              text="A",
                              font=(font, 45),
                              bg="red",
                              fg="white",
                              relief=button_relief,
                              borderwidth=5)
    button_attack1.config(height=1,width=2)
    button_attack1.grid(row=0, column=0, padx=(10, 5), pady=(10,0))

    button_attack2 = tk.Label(master=display, 
                              text="A", 
                              font=(font, 45), 
                              bg="red", 
                              fg="white",
                              relief=button_relief,
                              borderwidth=5)
    button_attack2.config(height=1,width=2)
    button_attack2.grid(row=0, column=1, padx=(5, 5), pady=(10,0))

    button_defense1 = tk.Label(master=display,
                               text="D",
                               font=(font, 45),
                               bg="blue",
                               fg="white",
                               relief=button_relief,
                               borderwidth=5)
    button_defense1.config(height=1,width=2)
    button_defense1.grid(row=0, column=2, padx=(5, 5), pady=(10,0))

    button_defense2 = tk.Label(master=display,
                                text="D",
                                font=(font, 45),
                                bg="blue", 
                                fg="white", 
                                relief=button_relief,
                                borderwidth=5)
    button_defense2.config(height=1,width=2)
    button_defense2.grid(row=0, column=3, padx=(5, 5), pady=(10,0))

    button_iconic1 = tk.Label(master=display,
                              text="I",
                              font=(font, 45),
                              bg="purple",
                              fg="white",
                              relief=button_relief,
                              borderwidth=5)
    button_iconic1.config(height=1,width=2)
    button_iconic1.grid(row=0, column=4, padx=(5, 5), pady=(10,0))

    button_iconic2 = tk.Label(master=display,
                              text="I",
                              font=(font, 45),
                              bg="purple",
                              fg="white",
                              relief=button_relief,
                              borderwidth=5)
    button_iconic2.config(height=1,width=2)
    button_iconic2.grid(row=0, column=5, padx=(5, 10), pady=(10,0))

#------------Upcoming Spell-------------------
def create_upcoming(number=0):
    global label_upcoming
    list_text = ["?", "A", "A", "D", "D", "I", "I"]
    text = list_text[number]
    
    list_background = ["grey", "red", "red", "blue", "blue", "purple", "purple"]
    background = list_background[number] 
    
    list_foreground = ["#404040", "white", "white", "white", "white", "white", "white"]
    foreground = list_foreground[number] 
    
    list_relief= ["sunken", "raised", "raised", "raised", "raised", "raised", "raised"]
    relief = list_relief[number]
    
    if number != 0:
        stone = list_stones[number-1]
        stone.config(bg="grey", fg="#404040", relief=tk.SUNKEN)
    
    label_upcoming = tk.Label(master=display3,
                              text=text,
                              font=(font, 100),
                              bg=background, 
                              fg=foreground, 
                              relief=relief, 
                              borderwidth=7)
    label_upcoming.config(height=1, width=2)
    label_upcoming.grid(row=0, column=0, padx=20, pady=20)
    
#------------Control buttons---------------------
button_next = tk.Button(master=display4, 
                        text= "Roll for next spell", 
                        font=(font, 30), 
                        bg="green", 
                        fg="white", 
                        relief=tk.RAISED, 
                        borderwidth=5, 
                        command=next_spell)
button_next.grid(row=0, column=1, sticky="e", pady=(0,10))

button_reset = tk.Button(master=display5, 
                         text= "Reset", 
                         font=(font, 20),
                         bg="maroon",
                         fg="white", 
                         relief=tk.RAISED, 
                         borderwidth=5,
                         command=reset)
button_reset.grid(row=0, column=1, sticky="e")

label_arrow = tk.Label(master=display5,
                              text="→",
                              font=(font, 35, "bold"),
                              bg="#404040",
                              fg="white", 
                              relief=button_relief, 
                              borderwidth=0)
label_arrow.grid(row=0, column=0, padx=(0,10), sticky="e")

#----------Main loop----------------------------
label_arrow.grid_forget()
spell_list = [1,2,3,4,5,6]
create_stones()
list_stones = [button_attack1, button_attack2, 
               button_defense1, button_defense2, 
               button_iconic1, button_iconic2]
create_upcoming()
window.mainloop()
