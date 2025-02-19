import tkinter as tk
import register_user
import db
import manage
import user_main

class Login(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=600, height=600)
    self.pack()

    master.geometry('600x600')
    master.title('ログイン')

    self.create_widgets()


  def create_widgets(self):
    self.entry_mail = tk.Entry(self)
    self.entry_pw = tk.Entry(self)
    self.entry_mail.place(x=250, y=100)
    self.entry_pw.place(x=250, y=200)
    self.entry_mail.focus_set()
    
    self.login_button = tk.Button(self, text='ログイン', command=self.login)
    self.login_button.place(x=300, y=260)
    
    self.button = tk.Button(self, text='新規登録', command=self.register_user)
    self.button.place(x=300, y=300)
    
    self.label_error = tk.Label(self, text='', fg='red')
    self.label_error.place(x=250, y=350)
    
  def register_user(self):
    self.destroy()
    register_user.Register(self.master)
    
  def login(self):
    mail = self.entry_mail.get()
    pw = self.entry_pw.get()
    
    if mail == '' or pw == '':
      self.label_error.configure(text='入力されていない欄があります。')
      return
    
    user = db.select_user(mail)
    salt = user[4]
    input_hashed_pw = db.get_hashed_pw(pw, salt)
    hashed_pw = user[3]
    
    user_id = user[0]
    
    if input_hashed_pw != hashed_pw:
      self.label_error.configure(text='パスワードが違います。')
      return
    
   
    #権限確認
    role = db.check_role(mail)
    if role == 0:
      self.destroy()
      manage.Manage(self.master)
    else:
      self.destroy()
      user_main.User_main(self.master, user_id)

if __name__ == '__main__':
  root = tk.Tk()
  app = Login(master=root)
  app.mainloop()