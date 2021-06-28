#!/usr/bin/python3

# if using Ubuntu
# sudo apt install python3-tk

#=============
# imports and instances
#=============
import tkinter as tk
from tkinter import ttk # adds labels, stands for "themed tk"
from tkinter import scrolledtext # scrolling text box
from tkinter import Menu # allows menus to be created
from tkinter import messagebox as msg # pop-up message boxes
from tkinter import Spinbox # spinning list of options

#=============
# create the window
#=============
win = tk.Tk()

#=============
# general settings
#=============
win.title("Python GUI 01")
# X, Y
win.resizable(True,True)

#=============
# content
#=============

#=============
# labels, label frames, and grid layout
#=============
# use frames within frames to manage the overall grid layout
#helloWorld = ttk.Label(win, text="Hello World")
#helloWorld.grid(column=0, row=0)
# create a frame with a mini grid of its own inside
top_frame = ttk.LabelFrame(win, text="  Label in a Frame  ")
top_frame.grid(column=0, row=0)
labelOne = ttk.Label(top_frame, text="Label One")
labelOne.grid(column=0, row=0, sticky=tk.W) # sticky aligns to grid west (left-align)

#=============
# text box
#=============
ttk.Label(win, text="enter your name").grid(column=0, row=1)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=20, textvariable=name)
name_entered.grid(column=0, row=2)

#=============
# dropdown menu with default values
#=============
ttk.Label(win, text="select your age").grid(column=1, row=1)
numbo = tk.StringVar()
numbo_chosen = ttk.Combobox(win, width=5, textvariable=numbo, state='readonly') # adding state restricts users to only listed options
#numbo_chosen['values'] = ("18-19",29,49,70)
numbo_chosen['values'] = [i for i in range(1,121)]
numbo_chosen.grid(column=1, row=2)
numbo_chosen.current(0)

#=============
# button
#=============
# click-action (put before the button itself)
def click_me():
	btn.configure(text="Click Me Again!")
	labelOne.configure(foreground="red")
	labelOne.configure(text="Name: " + name.get() + ", Age: " + numbo_chosen.get())
	msg.showwarning('Popup Title','Checkbox Status:\n'+str(str(cbox1Var.get()) + str(cbox2Var.get()) + str(cbox3Var.get())))
#	action.configure(state='disabled') # disable the button

# button actual (put after the function it uses)
btn = ttk.Button(win, text="Click Me!", command=click_me)
btn.grid(column=2, row=2)

#=============
# checkboxes in column 0, rows 3-5 (fourth through sixth)
#=============
# first is disabled and checked by default
cbox1Var = tk.IntVar()
cbox1 = tk.Checkbutton(win, text="Disabled", variable=cbox1Var, state="disabled")
cbox1.select()
cbox1.grid(column=0, row=3, sticky=tk.W)
# second is enabled and not checked by default
cbox2Var = tk.IntVar()
cbox2 = tk.Checkbutton(win, text="Unchecked", variable=cbox2Var)
cbox2.deselect() # not deselect vs select
cbox2.grid(column=0, row=4, sticky=tk.W)
# third is enabled and checked by default
cbox3Var = tk.IntVar()
cbox3 = tk.Checkbutton(win, text="Checked", variable=cbox3Var)
cbox3.select()
cbox3.grid(column=0, row=5, sticky=tk.W)

#=============
# radio buttons in column 1, rows 3-5 (fourth through sixth) sharing one variable to call a function, and using globals
#=============
radCol1 = "blue"
radCol2 = "gold"
radCol3 = "red"
def radColor():
	x = radVar.get()
	if x == 1: win.configure(background=radCol1)
	elif x == 2: win.configure(background=radCol2)
	elif x == 3: win.configure(background=radCol3)
# var to call radColor
radVar = tk.IntVar()
# first is blue
rad1 = tk.Radiobutton(win, text=radCol1, variable=radVar, value=1, command=radColor)
rad1.grid(column=1, row=3, sticky=tk.W)
# second is gold
rad2 = tk.Radiobutton(win, text=radCol2, variable=radVar, value=2, command=radColor)
rad2.grid(column=1, row=4, sticky=tk.W)
# third is red
rad3 = tk.Radiobutton(win, text=radCol3, variable=radVar, value=3, command=radColor)
rad3.grid(column=1, row=5, sticky=tk.W)
# use a loop to create the radio buttons more efficiently
#colz = ["black","orange","green"]
#for col in range(6,9):
#	xrad = tk.Radiobutton(win, text=colz[col], variable=radVar, value=col, command=XXXX)
#	xrad.grid(column=1, row=col, sticky=tk.W)

#=============
# spinbox
#=============
spin = Spinbox(win, from_=0, to=10, width=5, bd=5, relief=tk.RIDGE) # SUNKEN (def) RAISED FLAT GROOVE RIDGE, bd is borderwidth
spin.grid(column=2, row=3)

#=============
# scrolled text box
#=============
scrol_w = 50 # characters wide
scrol_h = 3 # lines high
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD) # default wrap is tk.CHAR, wraps characters regardless if in the middle of a word
scr.grid(column=0, row=9, columnspan=3) # columnspan keeps the box from stretching out column 0

#=============
# loop over items in an element to affect them (type less)
#=============
for child in win.winfo_children():
	child.grid_configure(padx=4, pady=4)

#=============
# menu bar
# not very Pythonic
#=============
# create function for the exit button in file menu
def _quity():
	msg.showerror('bye bye','hit ok to exit')
	win.quit()
	win.destroy()
	exit()
# create function for the "new" button in file menu
def _newy():
	if answer == True:
		v = 999
	elif answer == False:
		v = 999
# create menu bar
menu_bar = Menu(win)
#menu_bar = Menu(top_frame) # test
win.config(menu=menu_bar)
# create menu and add items
file_menu = Menu(menu_bar, tearoff=0) # create File menu item, remove dashed line at top
#
#
# create function for "new" to call popup
def _newpop():
	msg.askyesnocancel("Yes/No/Cancel Popup","Do a thing?")
file_menu.add_command(label="New", command=_newpop) # add item
file_menu.add_command(label="Configure") # add item
file_menu.add_separator() # adds a horizontal line
file_menu.add_command(label="Exit", command=_quity) # add item and function call
menu_bar.add_cascade(label="File", menu=file_menu) # add file menu to menu bar and give it a label
# create about menu to the menu_bar and popup function
def _abouty():
	msg.showinfo('About','This is Python using the tkinter library')
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_abouty)
menu_bar.add_cascade(label="Help", menu=help_menu)

#=============
# tabbed frames
# note using tabs inside label frames
#=============
bottom_frame = ttk.LabelFrame(win, text="  Tabs  ")
bottom_frame.grid(column=0, columnspan=3, row=20)
tabControl = ttk.Notebook(bottom_frame) # create tab control
# tab 1
tab1 = ttk.Frame(tabControl) # create a new tab
tabControl.add(tab1, text="Tab 1") # add the tab
# tab 2
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
# make the tabs visible, after adding tabs
tabControl.pack(expand=1, fill="both")
# add content to tabs
tab1stuff = ttk.Label(tab1, text="Stuff in Tab 1").grid(column=0, row=0, padx=10, pady=10)
tab2stuff = ttk.Label(tab2, text="Stuff in Tab 2").grid(column=0, row=0, padx=10, pady=10)


#=============
# give focus to field when opened
#=============
name_entered.focus()

#=============
# start GUI
#=============
win.mainloop()
