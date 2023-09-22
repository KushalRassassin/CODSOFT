import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("500x750+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('tasklist.txt','w')
        file.close()

Image_icon = PhotoImage(file="Images/R.png")
root.iconphoto(False, Image_icon)

TopImage = PhotoImage(file="Images/topbar.png")
Label(root,image=TopImage).pack()

menuImage = PhotoImage(file="Images/dock.png")
Label(root, image=menuImage, bg="#32405b").place(x=50, y=25)

listImage = PhotoImage(file="Images/task.png")
Label(root, image=listImage, bg="#32405b").place(x=400, y=10)

heading = Label(root, text="ALL TASKS", font="arial 20 bold", fg="white",bg = "#32405b")
heading.place(x=130, y=20)

frame = Frame(root,width=500,height=50,bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button = Button(frame, text="ADD", font= "arial 20 bold", width=6, bg="#5a95ff", fg="#fff",bd=0, command= addTask)
button.place(x=400,y=0)

#listbox:
frame1 = Frame(root, bd=3, width=800, height=280, bg="#32405b")
frame1.pack(pady= (160,0))

listbox = Listbox(frame1, font=('arial',12), width=50,height=20, bg="#32405b", fg= "white", cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side= RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
openTaskFile()
#delete
Delete_icon = PhotoImage(file="Images/delete.png")
Button(root,image=Delete_icon,bd=0, command=deleteTask).pack(side=BOTTOM,pady=13,)
root.mainloop()