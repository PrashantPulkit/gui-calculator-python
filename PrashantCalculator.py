from tkinter import *
import pygame

def buttonSound():
    pygame.mixer.music.load('untitled.mp3')
    pygame.mixer.music.play()

root =Tk()
root.iconbitmap(r"calculator.ico")
root.iconname("Prashant's Calculator")
root.title("Prashant's Calculator")
pygame.mixer.init()

def click(event):
    buttonSound()
    text = event.widget.cget("text")
    #print(text)
    if text=="=":
        if scvalue.get().isdigit():
         ent.update()
        else: 
         value=eval(ent.get())
         scvalue.set(round(value,2))
         ent.update()
    elif text=="C":
        scvalue.set("")
        ent.update()
        pass
    elif text == "EXIT":
        exit()
    else:
        if text=="X":
           text="*"
        scvalue.set(scvalue.get()+text)
        ent.update()
        pass
root.config(background="black")
root.geometry("380x630")
root.minsize(400,600)
#root.maxsize(400,600)
scvalue=StringVar()
scvalue.set("")
ent = Entry(root,textvariable=scvalue,font="lucida 40 ",bg="black",fg="white",border=0)
ent.pack(fill="x",ipadx=5,ipady=5,padx=10,pady=5)
bt_name=["C","%","/","=","7","8","9","X","4","5","6","-","1","2","3","+","EXIT","0","."]
for j in range(5):
    f = Frame(root,bg="black")
    for i in range(4*j,4*(j+1)):
        try:
            if ((i+1)%4)==0 or i in range(4):    
                b = Button(f,text=f"{bt_name[i]}",font="lucida 40 ",bg="black",fg="cyan",border=0)
                b.pack(side="left",anchor="n",ipadx=5,padx=5,pady=5,fill="x")
                b.bind("<Button-1>",click)
            else:
                b = Button(f,text=f"{bt_name[i]}",font="lucida 40 ",bg="black",fg="white",border=0)
                b.pack(side="left",anchor="n",ipadx=5,padx=5,pady=5,fill="x")
                b.bind("<Button-1>",click)   
        except:
            pass    
    f.pack(side="top",anchor="center",fill="x")


root.mainloop()