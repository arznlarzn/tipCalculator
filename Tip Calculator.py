from tkinter import *
from tkinter import messagebox



class MyGUI:

    def __init__(self):
        

        self.root = Tk()
        self.root.title('Tip Calculator!')
        self.root.geometry('600x400')


        self.things = Label(self.root, text='The value of the tip, as a percentage, is:', font=('Times New Roman', 14))
        self.things.pack(padx=10,pady=20)
        self.tip = Entry(self.root, width=14, font=('Times New Roman', 14))
        self.tip.insert(0, '15')
        self.tip.pack(padx=10, pady=10)
        self.instruction = Label(self.root, text='Here, enter the total amount of the service used:', font=('Times New Roman', 14))
        self.instruction.pack(padx= 10, pady=10)
        self.textbox = Entry(self.root, width=22, font=('Times New Roman', 14))
        self.textbox.pack(padx=10, pady=10)
        self.button = Button(self.root, text='Calculate', font=('Times New Roman', 22), command=self.calculate)
        self.button.pack(padx=10,pady=10)

        self.answer = Label(self.root, bd=2, relief="solid", text=' ', font=('Times New Roman', 22))
        self.answer.pack(padx=10,pady=10)

        #this is the instruction for the user- this just demonstrates that there is logic to let the user know if they didn't enter an amount
        #and that this programmer can set these sort of parameters.
        #although this itself is just the instruction.
        self.suggest = Label(self.root, text='*try hitting \'Calculate\' without entering anything in, to see what happens*', font=('Times New Roman', 14))
        self.suggest.pack(padx=10,pady=20)

        # This is the line that makes clicking the exit button have a result, here as called with on_closing
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.root.mainloop()

    def calculate(self):
        if self.textbox.get() == '':
            messagebox.showinfo(title='Wtf?', message='You have to put SOME amount in there!? Geez. *Facepalm*')
        else:
            total = float(self.textbox.get()) * (float(self.tip.get()) / 100)
            formatted_total = "{:.2f}".format(total)
            self.answer.config(text=formatted_total)

        #This is the method for the closing window
    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message="Do you really want to quit?"):
            self.root.destroy()




MyGUI()

