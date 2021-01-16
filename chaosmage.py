#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import random



window = tk.Tk()
window.geometry("640x360")
window.resizable(False, False)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.title("Chaos Mage")
icon_string = b'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'
window.iconphoto(False, tk.PhotoImage(data=icon_string))

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


# In[ ]:




