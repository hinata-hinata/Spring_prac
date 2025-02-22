import tkinter as tk
from tkinter import messagebox
import login
from mail import auth_code, send_mail

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
    
    self.entry_2 = tk.Entry(self)
    self.entry_2.place(x=145, y=50)
    
    self.button = tk.Button(self, text='決定', command=self.key_check)
    self.button.place(x=190, y=100)
    
    # self.button_one_more = tk.Button(self, text='再送信', command=self.one_more)
    # self.button_one_more.place(x=190, y=140)
    
    self.label = tk.Label(self, text='', fg='red')
    self.label.place(x=160, y=180)
    
  # def one_more(self):
  #   subject = '認証コード'
  #   key2 = auth_code()
  #   body = f'あなたの認証コードは{key2}です。'
  #   send_mail(self.mail, subject, body)
  #   messagebox.showinfo('再送信', '認証コードを再送信しました。')
    

  def key_check(self):
    input_key = self.entry.get()
    if self.key == input_key:
      messagebox.showinfo('認証完了', '認証に成功しました。ログイン画面に遷移します。')
      self.destroy()
      login.Login(self.master)
    else:
      self.label.configure(text='認証コードが違います。')  

