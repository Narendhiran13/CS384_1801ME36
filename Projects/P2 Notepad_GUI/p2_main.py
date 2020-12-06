
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import datetime
import os
import time

Base = Tk()
Base.title("Note_pad")
Base.geometry("700x700")
Base.resizable(height=None, width=None)


statbarb = Label(Base, text="Ln", relief=SUNKEN, bd=1, anchor="w")

file_Vari = None

txt_Ar = Text(Base, undo=True, wrap=None,
              height=Base.winfo_height(), width=Base.winfo_width())
txt_Ar.grid(row=0, sticky=N + E + S + W)

Base.grid_rowconfigure(0, weight=1)
Base.grid_columnconfigure(0, weight=1)


scroll_b = Scrollbar(txt_Ar, command=txt_Ar.yview)

txt_Ar.config(yscrollcommand=scroll_b.set)

scroll_b.pack(side=RIGHT, fill=Y)
# making New File


def newfile(*args):
    global Base, txt_Ar, file_Vari
    file_Vari = None
    Base.title("New File")
    txt_Ar.delete(1.0, END)

# Open a File


def openfile(*args):
    global Base, txt_Ar, file_Vari, origfilecontents
    file_Vari = askopenfilename(defaultextension=".txt", filetypes=[
                                ("All Files", "*.*"), ("Text Files", "*.txt")])
    if file_Vari == "":
        file_Vari = None
        origfilecontents = None
    else:
        try:
            Base.title(os.path.basename(file_Vari))
            txt_Ar.delete(1.0, END)
            file = open(file_Vari, "r")
            txt_Ar.insert(1.0, file.read())
            origfilecontents = file.read()
            file.close()
        except:
            Base.title("NeeruText")
            showerror("ERROR", str("Unable to open " +
                                   file_Vari+"\n"+"Not a .txt file!"))

# Save a File


def save_file(*args):
    global Base, txt_Ar, file_Vari, origfilecontents
    if file_Vari == None:
        save_as_file()
    else:
        file = open(file_Vari, "w")
        origfilecontents = txt_Ar.get(1.0, END)
        file.write(txt_Ar.get(1.0, END))
        file.close()
        showinfo("Successfully saved", "All changes saved")


def find_fun(*args):
    global Base, txt_Ar, file_Vari

    def find():
        txt_Ar.tag_remove('matches', '1.0', END)
        word = find_input.get()
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = txt_Ar.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                txt_Ar.tag_add("matches", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                txt_Ar.tag_config(
                    'matches', foreground='red', background='blue')
    find_popup = Toplevel()
    find_popup.geometry('450x200')
    find_popup.title('find word')
    find_popup.resizable(0, 0)
    # fram for find
    find_fram = LabelFrame(find_popup, text='Find')
    find_fram.pack(pady=20)
    # label
    text_find = Label(find_fram, text='find')
    find_input = Entry(find_fram, width=30)
    find_button = Button(find_fram, text='find', command=find)
    text_find.grid(row=0, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    find_button.grid(row=1, column=0, padx=8, pady=4)


def find_and_replace():
    global Base, txt_Ar, file_Vari

    def find():
        txt_Ar.tag_remove('matches', '1.0', END)
        word = find_input.get()
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = txt_Ar.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                txt_Ar.tag_add("matches", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                txt_Ar.tag_config(
                    'matches', foreground='red', background='blue')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = txt_Ar.get(1.0, END)
        new_content = content.replace(word, replace_text)
        txt_Ar.delete(1.0, END)
        txt_Ar.insert(1.0, new_content)

    find_popup = Toplevel()
    find_popup.geometry('450x200')
    find_popup.title('find word')
    find_popup.resizable(0, 0)
    # fram for find
    find_fram = LabelFrame(find_popup, text='Find and Replace')
    find_fram.pack(pady=20)
    # label
    text_find = Label(find_fram, text='find')
    text_replace = Label(find_fram, text='Replace')
    # entry box
    find_input = Entry(find_fram, width=30)
    replace_input = Entry(find_fram, width=30)
    # button
    find_button = Button(find_fram, text='find', command=find)
    replace_button = Button(find_fram, text='Replace', command=replace)
    # text label grid
    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)
    # entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    # button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

# save a file as Save as


def save_as_file():
    global Base, txt_Ar, file_Vari
    file_Vari = asksaveasfilename(defaultextension=".txt", filetypes=[
        ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_Vari == "":
        file_Vari = None
    else:
        file = open(file_Vari, "w")
        file.write(txt_Ar.get(1.0, END))
        file.close()
        showinfo("Successfully saved", str(
            "Saved as "+file_Vari+" successfully!"))

# Show Date and Time


def date_time_func(*args):
    global txt_Ar
    txt_Ar.insert(END, str(datetime.datetime.now()))
# Cut a File


def cut_func():
    global txt_Ar
    txt_Ar.event_generate("<<Cut>>")
# Copy a File


def copy_func():
    global txt_Ar
    txt_Ar.event_generate("<<Copy>>")
# Paste a File


def paste_func():
    global txt_Ar
    txt_Ar.event_generate("<<Paste>>")
# Delete a File


def delete_func():
    global txt_Ar
    ranges = txt_Ar.tag_ranges(SEL)
    txt_Ar.delete(*ranges)
# Description of file


def about():
    showinfo("About NText",
             "Text editor built using Tkinter Developed by Narendhiran and Gourav\n")
# Exit a File


def exit_application():
    Base.quit()
# Select all in a File


def select_all_func():
    global txt_Ar
    txt_Ar.event_generate("<<SelectAll>>")
# Undo in a File


def undo_func():
    global txt_Ar
    try:
        txt_Ar.edit_undo()
    except:
        pass
# Re Do in a File


def re_do_func():
    global txt_Ar
    try:
        txt_Ar.edit_redo()
    except:
        pass
# Implementing Find Line Count function


def find_lines_count():
    global txt_Ar, S3
    if txt_Ar.compare("end-1c", "!=", "1.0"):
        S6.entryconfig(0, label=str(
            str(int(txt_Ar.index('end').split('.')[0]) - 1)+" Lines"))
# Implementing Find_words Count function


def find_words_count():
    global txt_Ar, S5
    if txt_Ar.compare("end-1c", "!=", "1.0"):
        S5.entryconfig(0, label=str(
            str(len(txt_Ar.get(0.0, END).replace("\n", " ").split(" "))-1)+" Words"))
# Exit Without Saving Function


def exit_without_saving():
    global Base, txt_Ar, origfilecontents
    if file_Vari != None:
        if origfilecontents == txt_Ar.get(1.0, END):
            pass
        else:
            exit_application()
    result = askquestion(title="Exit", message=str("Do you want to save changes made to "+(
        os.path.basename(file_Vari) if file_Vari != None else "New File")+" ?"), icon='warning')
    if result == 'yes':
        save_file()
    else:
        exit_application()


txt_Ar.bind("<F5>", date_time_func)
txt_Ar.bind("<Control-n>", newfile)
txt_Ar.bind("<Control-s>", save_file)
txt_Ar.bind("<Control-o>", openfile)

menu = Menu(Base)
Base.config(menu=menu)


S1 = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=S1)
S1.add_command(label="New    Ctrl+N", command=newfile)
S1.add_command(label="Open   Ctrl+O", command=openfile)
S1.add_command(label="Save    Ctrl+S", command=save_file)
S1.add_command(label="Save as", command=save_as_file)
S1.add_separator()
S1.add_command(label="Exit", command=exit_without_saving)


S2 = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=S2)
S2.add_command(label="Undo        Ctrl+Z", command=undo_func)
S2.add_command(label="Redo        Ctrl+Y", command=re_do_func)
S2.add_separator()
S2.add_command(label="Cut          Ctrl+X", command=cut_func)
S2.add_command(label="Copy       Ctrl+C", command=copy_func)
S2.add_command(label="Paste       Ctrl+V", command=paste_func)
S2.add_command(label="Delete      Del", command=delete_func)
S2.add_separator()
S2.add_command(label="Select all    Ctrl+A", command=select_all_func)
S2.add_command(label="Date/Time   F5", command=date_time_func)
S2.add_separator()
S2.add_command(label="Find", command=find_fun)
S2.add_command(label="Find and Replace", command=find_and_replace)


S3 = Menu(menu, tearoff=0)
S5 = Menu(S3, tearoff=0, postcommand=find_words_count)
S6 = Menu(S3, tearoff=0, postcommand=find_lines_count)
menu.add_cascade(label="View", menu=S3)
S3.add_cascade(label="Word Count", menu=S5)
S3.add_cascade(label="Line Count", menu=S6)
S5.add_command(label="0 Words", command=None)
S6.add_command(label="0 Lines", command=None)

S4 = Menu(menu, tearoff=0)
menu.add_command(label="About", command=about)
Base.mainloop()
