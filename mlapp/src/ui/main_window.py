import tkinter


class MainWindow:
    def __init__(self):
        self.wnd = tkinter.Tk()
        self.menu = tkinter.Menu(self.wnd)

    def mainloop(self):
        self.wnd.config(menu=self.menu)
        self.menu.add_cascade(label='File')
        self.menu.add_cascade(label='Edit')
        self.menu.add_cascade(label='View')
        self.menu.add_cascade(label='About')
        self.wnd.mainloop()
