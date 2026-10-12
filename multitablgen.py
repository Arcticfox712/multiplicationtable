import tkinter as tk 
screen=tk.Tk()
screen.title("Multiplication Table Generator (yum)")
screen.configure(bg= "white")
screen.geometry("500x800")

def generator():
    lb1.delete(0, tk.END)
    numbr= int(e1.get())

    hi= range1.get()

    for i in range (1, hi + 1):
        result = str(numbr) + "x" + str(i) + "=" + str(numbr*i)
        lb1.insert(tk.END, result)
    



l1=tk.Label(text ="What number do you wish to multiply?", width = 30, height= 2, bg= "white", fg= "black")
l1.place(x= 10, y= 10)
e1= tk.Entry(width= 25, bg= "white", fg="black")
e1.place(x= 300, y= 17)
l2= tk.Label(text= "Select your range: ", width = 30, height= 2, bg= "white", fg= "black")
l2.place (x= 260, y= 60)

range1= tk.IntVar()

r1= tk.Radiobutton (text= "10" , value= 10, variable= range1)
r1.place( x= 280, y= 90)
r2= tk.Radiobutton (text= "20" , value= 20, variable= range1)
r2.place( x= 330, y= 90)
r3= tk.Radiobutton (text= "30" , value= 30, variable= range1)
r3.place(x= 380, y= 90)

b1= tk.Button(text= "Generate", width = 20, height= 2, bg= "green", fg= "black", command= generator)
b1.place(x= 300, y= 150)

lb1= tk.Listbox(width= 30, height= 30)
lb1.place (x= 70, y=90)

# l1

screen.mainloop()