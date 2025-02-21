import tkinter as tk
from tkinter import messagebox
import login

class Auth(tk.Frame):
  def __init__(self, master, key):
    super().__init__(master, width=600, height=600)
    self.master = master
    self.key = key
    self.pack()
 

    master.geometry('600x600')
    master.title('Hello Tkinter')

    self.create_widgets()


  def create_widgets(self):
    self.entry = tk.Entry(self)
    self.entry.place(x=145, y=50)
    
    self.button = tk.Button(self, text='決定', command=self.key_check)
    self.button.place(x=190, y=100)
    
    self.label = tk.Label(self, text='', fg='red')
    self.label.place(x=160, y=140)

  def key_check(self):
    input_key = self.entry.get()
    if self.key == input_key:
      messagebox.showinfo('認証完了', '認証に成功しました。ログイン画面に遷移します。')
      self.destroy()
      login.Login(self.master)
    else:
      self.label.configure(text='認証コードが違います。')  

