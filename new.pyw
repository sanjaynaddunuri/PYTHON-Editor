import tkinter as tk  # to use 'tk' as a acronym for 'tkinter' in widgets
from tkinter import *  # tkinter is a module used to design a GUI, * -> every class inside it
from tkinter import ttk, font, filedialog, messagebox, colorchooser  # filedialog is used to open file
import os  # to connect the output to cmd
import webbrowser  # to open google and python.org web-services
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re

path = ''
root = Tk()  # object creation for Tk() class for output window
root.geometry('1270x650+0+0')  # initializing Window size
root.title('PyBook')  # Title for the window
global selected

myMenu      = Menu()                       # creating object for Menu class for creating menus
file_menu   = Menu(myMenu, tearoff=False)  # creating  File-menu
view_menu   = Menu(myMenu, tearoff=False)  # creating  view-menu
edit_menu   = Menu(myMenu, tearoff=False)  # creating  Edit-menu
run_menu    = Menu(myMenu, tearoff=False)  # creating  Run-menu
color_menu  = Menu(myMenu, tearoff=False)  # creating  Color-menu
help_menu   = Menu(myMenu, tearoff=False)  # creating  Help-menu
clear_menu  = Menu(myMenu, tearoff=False)  # creating  Clear-menu

myMenu.add_cascade(label='File',   menu = file_menu)    # adding 'File'  to menu-bar
myMenu.add_cascade(label='Edit',   menu = edit_menu)    # adding 'Edit'  to menu-bar
myMenu.add_cascade(label='View',   menu = view_menu)    # adding 'View'  to menu-bar
myMenu.add_cascade(label='Color',  menu = color_menu)   # adding 'Color' to menu-bar
myMenu.add_cascade(label='Run',    menu = run_menu)     # adding 'Run'   to menu-bar
myMenu.add_cascade(label='Help',   menu = help_menu)    # adding 'Help'  to menu-bar
myMenu.add_cascade(label='Clear',  menu = clear_menu)   # adding 'Clear' to menu-bar

# adding tool_bar for placing fonts into it
tool_bar_label = ttk.Label(root)
tool_bar_label.pack(side=tk.TOP, fill=tk.X)

# creating font_box
font_tuple = font.families()
font_family = StringVar()                                                                     # font family is initializing that is string variable
font_box = ttk.Combobox(tool_bar_label, width=30, textvariable=font_family,state='readonly')  # creating the font family combobox for toolbar
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))                                                   # initializing the default font
font_box.grid(row=0, column=0, padx=5, pady=5)                                                # placing the comobobox in the toolbar

# size_box
size_var = IntVar()                                                                           # font size is initializing that is integer variable
font_size = ttk.Combobox(tool_bar_label, width=14, textvariable=size_var,state='readonly')    # creating the font size combobox for toolbar
font_size['values'] = tuple(range(8, 80, 2))                                                  # initializing the range
font_size.current(4)                                                                          # initializing the default font size
font_size.grid(row=0, column=1, padx=5)                                                       # placing the combobox in the toolbar

# bold button
bold_icon = tk.PhotoImage(file=r"C:\Users\naddu\Desktop\project\bold.png")                   # creating a Bold Icon for the Bold Button
bold_btn = ttk.Button(tool_bar_label, image=bold_icon)                                        # creating Bold button for the toolbar
bold_btn.grid(row=0, column=2, padx=5)                                                        # placing the button in the toolbar

# italic button
italic_icon = tk.PhotoImage(file=r"C:\Users\naddu\Desktop\project\italic.png")               # creating a Italic Icon for the Italic Button
italic_btn = ttk.Button(tool_bar_label, image=italic_icon)                                    # creating Italic button for the toolbar 
italic_btn.grid(row=0, column=3, padx=5)                                                      # placing the button in the toolbar

# underline button
underline_icon = tk.PhotoImage(file=r"C:\Users\naddu\Desktop\project\underline.png")         # creating a Underline Icon for the Underline Button
underline_btn = ttk.Button(tool_bar_label, image=underline_icon)                              # creating Underline button for the toolbar
underline_btn.grid(row=0, column=4, padx=5)                                                   # placing the button in the toolbar

# default font_style and font_size
font_now = 'Arial'
font_size_now = 12

# creating Frame for writing text in it
editFrame = Frame(root, bg='white')
editFrame.place(x=0, y=0, height=800, relwidth=1)  # dimensions for Frame
# creating scrollbar to editFrame
# creating textarea to write text
scrollbar = Scrollbar(editFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)         # scrollbar will set to right size of the window
scrollbar1 = Scrollbar(editFrame, orient='horizontal')
scrollbar1.pack(side=BOTTOM, fill=X)       # scrollbar will set to bottom of the window
textarea = Text(editFrame, font=('Arial', font_size_now, 'bold'),yscrollcommand=scrollbar.set, wrap="none", xscrollcommand=scrollbar1.set)
textarea.pack(fill=BOTH, expand=True)      # dimensions for textarea
scrollbar.config(command=textarea.yview)   # connecting scrollbar to textarea
scrollbar1.config(command=textarea.xview)  # connecting scrollbar to textarea
try:
    cdg = ic.ColorDelegator()
    cdg.prog = re.compile(r"\b(?P<MYGROUP>tkinter)\b|" + ic.make_pat(), re.S)
    cdg.idprog = re.compile(r'\s+(\w+)', re.S)
except TypeError:
    pass

cdg.tagdefs['GROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}
# These five lines are optional. If omitted, default colours are used.
cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#FFA500', 'background': '#FFFFFF'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#8F00FF', 'background': '#FFFFFF'}
cdg.tagdefs['STRING'] = {'foreground': '#00FF00', 'background': '#FFFFFF'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}
ip.Percolator(textarea).insertfilter(cdg)


# function to change font_style
def change_font(main_application):
    global font_now  # initializing the font
    font_now = font_family.get()  # changing the font
    textarea.configure(font=(font_now, font_size_now))  # configuring to the text window


# function to change font_size
def change_size(main_application):
    global font_size_now  # initializing the font size
    font_size_now = size_var.get()  # changing the font size
    textarea.config(font=(font_now, font_size_now))  # configuring to the text window


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)


def change_bold(event=None):
    bold_font = font.Font(textarea, textarea.cget("font"))
    bold_font.configure(weight="bold")
    textarea.tag_configure("bold", font=bold_font)
    current_tags = textarea.tag_names("sel.first")
    if "bold" in current_tags:
        textarea.tag_remove("bold", "sel.first", "sel.last")
    else:
        textarea.tag_add("bold", "sel.first", "sel.last")


bold_btn.configure(command=change_bold)


# italic function
def change_italic(event=None):
    italic_font = font.Font(textarea, textarea.cget("font"))
    italic_font.configure(slant="italic")
    textarea.tag_configure("italic", font=italic_font)
    current_tags = textarea.tag_names("sel.first")
    if "italic" in current_tags:
        textarea.tag_remove("italic", "sel.first", "sel.last")
    else:
        textarea.tag_add("italic", "sel.first", "sel.last")


italic_btn.configure(command=change_italic)


# underline function
def underline():
    underline_font = font.Font(textarea, textarea.cget("font"))
    underline_font.configure(underline=1)
    textarea.tag_configure(1, font=underline_font)
    current_tags = textarea.tag_names("sel.first")
    if "1" in current_tags:
        textarea.tag_remove("1", "sel.first", "sel.last")
    else:
        textarea.tag_add("1", "sel.first", "sel.last")


underline_btn.configure(command=underline)

# creating status bar
status_bar = Label(root, text='Status Bar', padx=10, bg='white')  # creating the label to the status bar
status_bar.pack(side=BOTTOM)  # displays the Status Bar on the bottom of the Window
text_changed = False


def changed(event=None):
    global text_changed
    if textarea.edit_modified():
        text_changed = True
        words = len(textarea.get(1.0, 'end').split())  # counting Characters from staring point(including Spaces)
        characters = len(textarea.get(1.0, 'end'))  # Counting words in every line from the beginning
        row, col = textarea.index('insert').split('.')  # Counting every line from the beginning
        status_bar.config(text=f'Characters : {characters}, Words: {words}, Lines: {row}: {col}')
        textarea.edit_modified(False)


textarea.bind('<<Modified>>', changed)


# function to add "Google" to 'Help' menu_item
def google(event=None):
    webbrowser.open('https://google.com')  # Connecting to the google website


# function to add "Python.org" to 'Help' menu_item
def python(event=None):
    webbrowser.open('https://python.org')  # Connecting to the python.org website


# function to add "about Notepy" to 'Help' menu_item
def about(event=None):
    os.startfile(r'"C:\Users\naddu\Desktop\project\about.pyw"')  # Starting a file to show the about PyBook, only extension with (.pyw)


# function to change 'Background color'
def change_back_color(event=None):
    c = colorchooser.askcolor()  # choosing the color in the Background color dialog box
    textarea.configure(background=c[1])  # adding the choosen color for the frame,range is 0 or 1


# defining run menu-item
def run_code(event=None):
    if path == '':  # to display messagebox telling user to save the code
        result = messagebox.askquestion('Error', 'Please save the file before running...!')
        if result == 'yes':
            save_as()  # Calling the Save_as() function after clickig the 'Yes' Button
    else:
        command = f'python {path}'  # file path
        os.system(f"start cmd /k {command}")  # Connecting Output to the Command Prompt


# defining save-as menu-item
def save_as(event=None):
    global path  # declaring path as global to use it in other functions
    path = filedialog.asksaveasfilename(filetypes=[('Python Files', '*.py')],
                                        defaultextension='.py')  # asksaveasfilename returns path where file is saved
    if path != '':  # condition to avoid No such file or directory exists error
        file = open(path, 'w')  # opening file in write mode
        root.title(f" PyBook - {path}")  # This will be Visible as IDE name + File path on top of the Window
        file.write(textarea.get(1.0, END))  # writing text on textarea into the file
        file.close()  # Closing a file


# defining openfile menu-item
def openfile(event=None):
    global path  # declaring path as global to use it in other function
    path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')],
                                      defaultextension='.py')  # opens the File Dialog Box only with Python Files
    root.title(f" PyBook - {path}")  # This will be Visible as IDE name + File path on top of the Window
    if path != '':
        file = open(path, 'r')
        data = file.read()
        textarea.delete(1.0, END)
        textarea.insert(1.0, data)
        file.close()


# defining save menu-item
def save(event=None):
    if path == '':  # to check if the file is already saved or not...!
        save_as()
    else:
        with open(path, 'w') as f:
            f.write(textarea.get(1.0, END))  # Saves the Current window Code


# defining new menu-item
def new(event=None):
    os.startfile(r'"C:\Users\sanjay\Desktop\project\new.pyw"')  # Starting a file to Show the New Window , only extension with (.pyw)


# defining cut menu-item
def cut_file(event=None):
    global selected
    try:
        if event:
            selected = root.clipboard_get()  # Check to see if keyboard shortcut used
        else:
            if textarea.selection_get():
                selected = textarea.selection_get()  # Grab selected text from text box
                textarea.delete("sel.first", "sel.last")  # Delete selected text from text box
                root.clipboard_clear()  # Clear the clipboard and then append
                root.clipboard_append(selected)
    except TclError:
        pass


# defining copy menu-item
def copy_file(event=None):
    global selected
    try:
        if event:
            selected = root.clipboard_get()  # Check to see if keyboard shortcut used
        else:
            if textarea.selection_get():
                selected = textarea.selection_get()  # grab selected text from text box
                root.clipboard_clear()  # Clear the clipboard and then append
                root.clipboard_append(selected)
    except TclError:
        pass


# defining paste menu-item
def paste_file(event=None):
    global selected
    try:
        if event:
            selected = root.clipboard_get()  # check to see if keyboard shortcut used
        else:
            if selected:
                position = textarea.index(INSERT)
                textarea.insert(position, selected)  # inserts the text into the window
    except (TclError, NameError):
        pass


# defining exit menu-item
def i_exit(event=None):
    result = messagebox.askyesno('Exit', 'Do you want to exit....?')  # to display messagebox asking to exit or not
    if result:
        root.destroy()  # exit from the window if user chooses yes


# defining clear menu-item
def clear(event=None):
    textarea.delete(1.0, END)  # clears all the Text in the current window


# defining select_all menu-item
def select_all(event=None):
    textarea.tag_add(SEL, "1.0", END)  # selects all the Text in the window
    textarea.mark_set(INSERT, "1.0")  # inserting the text in to the window
    textarea.see(INSERT)
    return 'break'


# defining find menu-item
def find_func(event=None):
    def find(find_input=None):
        word = find_input.get()  # getting the input from the user
        matches = 0  # initializing the matches
        if word:
            start_pos = '1.0'
            while True:
                start_pos = textarea.search(word, start_pos,stopindex=tk.END)  # checking the word from the starting position to the end
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                textarea.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                textarea.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = textarea.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        textarea.delete(1.0, tk.END)
        textarea.insert(1.0, new_content)
        
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.resizable(0, 0)
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)
    text_find_label = ttk.Label(find_frame, text='Find :')
    text_replace_label = ttk.Label(find_frame, text='Replace')
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)
    find_dialogue.title(path)
    find_dialogue.mainloop()


show_toolbar = tk.BooleanVar()
show_toolbar = False


# function to hide toolbar
def hide_toolbar():
    global show_toolbar

    if not show_toolbar:
        textarea.pack_forget()
        tool_bar_label.pack(side=tk.TOP, fill=tk.X, pady=0)
        textarea.pack(fill=tk.BOTH, expand=True)
        show_toolbar = True
        editFrame.place(x=0, y=40, height=760, relwidth=1)
    else:
        tool_bar_label.pack_forget()
        show_toolbar = False
        editFrame.place(x=0, y=0, height=700, relwidth=1)


show_status_bar = tk.BooleanVar()
show_status_bar.set(True)


# function to hide status_bar
def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar = True


view_menu.add_checkbutton(label='Tool Bar', onvalue=False, offvalue=1, variable=show_toolbar, compound=tk.LEFT,
                          command=hide_toolbar)
view_menu.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_status_bar, compound=tk.LEFT,
                          command=hide_status_bar)

# adding New File,Open File,Save,Save as,exit menu-items to file menu
file_menu.add_command(label='New File', accelerator='Ctrl+N', command=new)
file_menu.add_command(label='Open File', accelerator='Ctrl+O', command=openfile)
file_menu.add_command(label='Save', accelerator='Ctrl+S', command=save)
file_menu.add_command(label='Save as', accelerator='Ctrl+Shift+S', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Ctrl+Q', command=i_exit)

# adding Cut,Copy,Paste menu-items to edit-menu
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=cut_file)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=copy_file)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=paste_file)
edit_menu.add_command(label='Select-all', accelerator='Ctrl+A', command=select_all)
edit_menu.add_separator()
edit_menu.add_command(label='Find', compound=tk.LEFT, accelerator='Ctrl+F', command=find_func)

# adding background color and foreground color
color_menu.add_command(label='Background', accelerator='Ctrl+B', command=change_back_color)

# run-menu starts
run_menu.add_command(label='Run Code', accelerator='Ctrl+R', command=run_code)

# adding Clear to menu-bar
clear_menu.add_command(label='Clear Code', accelerator='Ctrl+K', command=clear)

# creating help menu
help_menu.add_command(label='Google', accelerator='Ctrl+G', command=google)
help_menu.add_command(label='Python.Org', accelerator='Ctrl+P', command=python)
help_menu.add_separator()
help_menu.add_command(label='About PyBook', command=about)

# adding Icon on the top of the window
p1 = PhotoImage(file=r"C:\Users\naddu\Desktop\project\icon.png")
root.iconphoto(False, p1)
root.config(menu=myMenu)  # binding mymenu to root

# binding shortcuts for menu-items
root.bind(' <Control-n> ', new)
root.bind(' <Control-o> ', openfile)
root.bind(' <Control-s> ', save)
root.bind(' <Control-S> ', save_as)
root.bind(' <Control-q> ', i_exit)
root.bind(' <Control-x> ', cut_file)
root.bind(' <Control-c> ', copy_file)
root.bind(' <Control-v> ', paste_file)
root.bind(' <Control-a> ', select_all)
root.bind(' <Control-f> ', find_func)
root.bind(' <Control-b> ', change_back_color)
root.bind(' <Control-r> ', run_code)
root.bind(' <Control-g> ', google)
root.bind(' <Control-p> ', python)
root.bind(' <Control-k> ', clear)
root.mainloop()  # to display output window continuously




