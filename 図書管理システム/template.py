import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.pack()

    master.geometry('400x400')
    master.title('Hello Tkinter')

    self.create_widgets()


  def create_widgets(self):
    pass


if __name__ == '__main__':
  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()