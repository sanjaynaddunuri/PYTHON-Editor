from tkinter import *
root = Tk()

root.geometry("1200x480")
root.minsize(height=560, width=560)
root.title("About Pybook")

#creating frame for canvas
frame =Frame( root,width=500, height=400)
frame.pack(expand=True, fill=BOTH)

#Create a canvas object and setting scrollbar
canvas    = Canvas(frame,width=1000, height=750, scrollregion=(0, 0, 5000, 5000))
scrollbar = Scrollbar (frame,orient=VERTICAL)
scrollbar. pack(side=RIGHT, fill= Y)
scrollbar. config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)

scrollbar1 = Scrollbar (frame,orient='horizontal')
scrollbar1. pack(side=BOTTOM, fill= X)
scrollbar1. config(command=canvas.xview)
canvas.config(xscrollcommand=scrollbar1.set)

#Add a text in Canvas canvas.

canvas.create_text(80,   50,  text="Pybook:" ,fill="black", font=('Helvetica 25 bold'))
canvas.create_text(80,  100,  text="Source code: ", fill="black", font=('arial 16 bold'))
canvas.create_text(340, 100,  text="  www.google.com, www.git hub.com etc........",fill="black", font=('arial 15')) 
canvas.create_text(320, 150,  text="Notepy is Python's Integrated Development and Learning Environment.",fill="black", font=('arial 15'))
canvas.create_text(175, 200,  text="Notepy has the following features:", fill="black", font=('arial 15 bold'))
canvas.create_text(320, 250,  text="=⫸ It is coded in 100% pure Python, using the tkinter GUI toolkit. " ,fill='black', font=('arial 15'))
canvas.create_text(170, 300,  text="=⫸ It works on only Windows.", fill='black', font=('arial 15'))
canvas.create_text(520, 350,  text="=⫸ We are connected this notepy to command prompt. so errors are identified by this command prompt only. ",fill="black", font=('arial 15'))
canvas.create_text(470, 400,  text="=⫸ Multi-window text editor with Python colorizing, easy access of every items and other features.",fill='black', font=('arial 15'))
canvas.create_text(455, 450,  text="=⫸ Search within any window. replace within editor windows, and search through multiple files.",fill="black", font=('arial 15'))
canvas.create_text(250, 500,  text="=⫸ Configuration. browsers, and other dialogs.",fill="black", font=('arial 15'))

canvas.create_text(70,  570,  text="Menus", fill='black', font=('arial 25 bold'))
canvas.create_text(300, 630,  text="=⫸ Notepy has only one main window that is Editor window.", fill="black", font=("arial 15"))
canvas.create_text(315, 680,  text="=⫸ It is possible to have multiple editor windows simultaneously.", fill="black", font=('arial 15'))
canvas.create_text(400, 730,  text="=⫸ Each menu documented below indicates which window type it is associated with." ,fill="black", font=('arial 15 '))
canvas.create_text(670, 780,  text="=⫸ Output window that is command prompt. such as used for execute the code directly in the command prompt with out any file path of the code.", fill="black",font=('arial 15'))

canvas.create_text(80,  840,  text="File Menu", fill="black", font=('arial 25 bold'))
canvas.create_text(300, 840,  text="(Editor Window )", fill="black", font=('arial 25 bold'))
canvas.create_text(100, 900,  text="New File..",fill="black", font=('arial 20 bold'))
canvas.create_text(250, 940,  text="Creates a new file editing window.", fill="black", font=('arial 15 bold'))
canvas.create_text(100, 990,  text="Open File..", fill='black', font=('arial 20 bold'))
canvas.create_text(400, 1040, text="Open an existing file with an Open dialog box using filedialog box. ", fill="black", font=('arial 15 bold'))
canvas.create_text(100, 1090, text="Save File..", fill="black", font=('arial 20 bold'))
canvas.create_text(425, 1140, text="if there is one, it will Save the current window to the associated file" ,fill="black", font=('arial 15 bold'))
canvas.create_text(100, 1190, text="Save As..", fill='black', font=('arial 20 bold'))
canvas.create_text(620, 1240, text="Save the current window with a Save As dialog. The file saved becomes the new associated file for the window. ",fill='black', font=('arial 15 bold'))
canvas.create_text(80,  1290, text="Quit..",fill='black',font =('arial 20 bold'))
canvas.create_text(250, 1340, text="Close all windows and quit Pybook. ", fill='black', font=('arial 15 bold'))

canvas.create_text(80,  1400, text="Edit Menu", fill='black', font=('arial 25 bold'))
canvas.create_text(300, 1400, text="(Editor Window )", fill='black', font=('arial 25 bold'))
canvas.create_text(80,  1460, text="Cut..", fill="black", font=('arial 20 bold'))
canvas.create_text(420, 1500, text="Copy selection into the system-wide clipboard, then delete the selection." ,fill="black", font=('aria1 15 bold'))
canvas.create_text(80,  1550, text="Copy..", fill="black", font=('arial 20 bold'))
canvas.create_text(300, 1600, text="Copy selection into the system-wide clipboard.", fill='black', font=('arial 15 bold'))



canvas.create_text(80,  1650, text="Paste..", fill="black", font= ('arial 20 bold'))
canvas.create_text(420, 1700, text="Inserts the contents ofthe system-wide clipboard into the current window.", fill="black", font=('arial 15 bold'))
canvas.create_text(100, 1750, text="Select all..", fill="black", font=('arial 20 bold'))
canvas.create_text(300, 1800, text="Selects the entire contents of the current window.", fill="black",font=('arial 15 bold'))
canvas.create_text(80,  1850, text="Find..", fill="black", font=('arial 20 bold'))


canvas.create_text(420, 1900, text="Opens a search dialogbox with many two options (find and repalace). " ,fill='black', font=('arial 15 bold'))
canvas.create_text(100, 1950, text="Repalce..", fill='black',font=('arial 20 bold'))
canvas.create_text(370, 2000, text="Opens a search-and-replace dialogbox. We can replace words.", fill='black', font=('arial 15 bold'))
canvas.create_text(90,  2070, text="View Menu", fill='black', font=('arial 25 bold'))
canvas.create_text(320, 2070, text="( Editor Window )", fill='black', font=('aria1 25 bold'))
canvas.create_text(100, 2135, text="Toolbar..", fill='black', font= ('arial 20 bold'))



canvas.create_text(500, 2170, text="It is a checkbutton to hide the tool bar or show the tool bar with the shortcut keys. " ,fill='black', font=('arial 15 bold'))
canvas.create_text(150, 2220, text="Fonts (Toolbar )", fill='black', font=('arial 20 bold'))
canvas.create_text(400, 2270, text="It opens the Fonts combobox to choose the fonts oftheir Own.", fill='black', font=('arial 15 bold'))
canvas.create_text(180, 2320, text="Font Size (Toolbar )", fill='black', font=('arial 20 bold'))
canvas.create_text(530, 2370, text="It opens the Size combobox to choose the font size of their Own(increment or decrement).",fill='black',font=('arial 15 bold'))
canvas.create_text(150, 2420, text="Bold (Toolbar )", fill="black", font=('arial 20 bold'))
canvas.create_text(400, 2470, text="This is the bold button to appear the Text more visible to the user. " ,fill="black",font=('arial 15 bold'))
canvas.create_text(150, 2520, text="Italic (Toolbar )", fill="black", font=('arial 20 bold'))
canvas.create_text(380, 2570, text="This is the Italic button to visible the Text in Italic Format.", fill="black", font=('arial 15 bold'))
canvas.create_text(180, 2620, text="Underline (Toolbar )",fill="black", font=('arial 20 bold'))
canvas.create_text(400, 2670, text="This is the Underline button to visible the Text in underline Format", fill="black", font=('arial 15 bold'))



canvas.create_text(115, 2720, text="Statusbar..", fill='black', font=('arial 20 bold'))
canvas.create_text(500, 2770, text="It is a checkbutton to hide the statusbar or show the statusbar with the shortcut keys." ,fill='black',font=('arial 15 bold'))
canvas.create_text(230, 2830, text="Run Menu (Editor Window )", fill='black', font=('aria1 25 bold'))
canvas.create_text(115, 2890, text="Run Code", fill='black', font=('arial 20 bold'))
canvas.create_text(700, 2940, text="It will check the code. If no error, then execute the current code in command prompt.Output is displayed in the command prompt.", fill='black', font=('arial 15 bold')) 
canvas.create_text(55,  2940, text="=⫸" ,fill="black", font=('arial 20'))
canvas.create_text(300, 2990, text="Note that output requires use of print or write.", fill='black', font=('arial 15 bold'))
canvas.create_text(55,  2990, text="=⫸", fill="black", font=('arial 20'))
canvas.create_text(430, 3040, text="When execution is complete. you want to execute every time in the editor.", fill='black', font=('arial 15 bold'))
canvas.create_text(55,  3040, text="=⫸", fill="black", font=('arial 20'))





canvas.create_text(250, 3100, text="Colors Menu (Editor Window)", fill="black", font=('arial 25 bold'))
canvas.create_text(200, 3170, text="Background Color", fill='black', font=('arial 20 bold'))
canvas.create_text(700, 3220, text="Opens the color chooser dialog box to choose the color of their own. This will change the background color of the editor.", fill='black', font=('arial 15 bold'))
canvas.create_text(200, 3270, text="Foreground Color" ,fill='black', font=('arial 20 bold'))
canvas.create_text(650, 3320, text="opens the color chooser dialog box to choose the color of their own. this will change the Text color of the Text." ,fill='black', font=('arial 15 bold'))

canvas.create_text(250, 3400, text="Clear Menu (Editor Window)", fill="black", font=('arial 25 bold'))
canvas.create_text(100, 3470, text="Clear..", fill="black", font=('arial 20 bold'))
canvas.create_text(250, 3520, text="It Clears the whole Text in Editor.", fill="black", font=('arial 15 bold'))
canvas.create_text(250, 3600, text="Help Menu (Editor Window)", fill='black', font=('arial 25 bold'))
                                                                                    

canvas.create_text(130, 3670, text="Google..", fill="black" ,font=('arial 20 bold'))
canvas.create_text(750, 3720, text="opens the google website(On Network), so you can so you can access the google with the Oneclick. it saves time for your own doubts. ", fill='black', font=('arial 15 bold'))
canvas.create_text(150, 3770, text="Python.org",fill="black", font=('arial 20 bold' ))
canvas.create_text(750, 3820, text="opens the python. org website(On Network). start a web browser and open docs. python. org showing the latest Python documentation",fill='black', font=( 'arial 15 bold'))


p1 = PhotoImage(file=r"C:\Users\sanjay\Desktop\project\icon.png")
root.iconphoto(False, p1)

canvas.pack(expand=True, side=LEFT, fill=BOTH)
root.mainloop()
























                                                                     


