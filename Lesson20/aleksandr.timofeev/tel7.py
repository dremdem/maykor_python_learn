# -*- coding: utf-8 -*- 

from tkinter import *
 
 
class Frame_Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width=500, height=30, bg="grey")
 
        self.parent = parent
        self.parent.geometry("500x300")
        self.parent.title("Телефонный справочник г. Заинск")
 
        self.grid(row=0, column=0)
        self.grid_propagate(False)
        self.create_widgets()
 
    def create_widgets(self):
 
        # I-knopka
        self.bttn1 = Button(self)
        self.bttn1.grid(row=0, column=0)
        self.bttn1.configure(text="Добавить", highlightbackground=self["bg"])
        # II-knopka
        self.bttn2.grid(row=0, column=1)
        self.bttn2.configure(text="Изменить", highlightbackground=self["bg"])
        # III-knopka
        self.bttn3 = Button(self)
        self.bttn3.grid(row=0, column=3)
        self.bttn3["text"] = "Удалить"
        self.bttn3["highlightbackground"] = self["bg"]
        # IV-knopka
        self.bttn4 = Button(self)
        self.bttn4.grid(row=0, column=4)
        self.bttn4["text"] = "Справка"
        self.bttn4["highlightbackground"] = self["bg"]
        # V-knopka
        self.bttn5 = Button(self)
        self.bttn5.grid(row=0, column=5)
        self.bttn5["text"] = "Выход"
        self.bttn5["highlightbackground"] = self["bg"]
 
root = Tk()
app = Frame_Example(root)
 
root.mainloop()