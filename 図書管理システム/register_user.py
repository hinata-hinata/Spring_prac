import tkinter as tk
import db

class Register(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=600, height=600)
    self.master = master
    self.pack()

    master.geometry('600x600')
    master.title('Hello Tkinter')

    self.create_widgets()


  def create_widgets(self):
    self.label_name = tk.Label(self, text='名前')
    self.label_mail = tk.Label(self, text='メール')
    self.label_pw = tk.Label(self, text='パスワード')
    self.label_pw_con = tk.Label(self, text='パスワード再入力')
    
    self.label_name.place(x=50, y=100)
    self.label_mail.place(x=50, y=140)
    self.label_pw.place(x=50, y=180)
    self.label_pw_con.place(x=50, y=220)
    
    self.entry_name = tk.Entry(self)
    self.entry_mail = tk.Entry(self)
    self.entry_pw = tk.Entry(self, show='*') 
    self.entry_pw_con = tk.Entry(self, show='*')  

    
    self.entry_name.place(x=150, y=100)
    self.entry_mail.place(x=150, y=140)
    self.entry_pw.place(x=150, y=180)
    self.entry_pw_con.place(x=150, y=220)
    
    #ラジオボタン
    self.radio_status = tk.IntVar()
    self.radio1 = tk.Radiobutton(self, text='管理者', variable=self.radio_status, value=0)
    self.radio2 = tk.Radiobutton(self, text='利用者', variable=self.radio_status, value=1)
    self.radio1.place(x=150, y=260)
    self.radio2.place(x=210, y=260)

    
    self.button = tk.Button(self, text='登録', command=self.register)
    self.button.place(x=100, y=300)
    
    self.label_error = tk.Label(self, text='', fg='red')
    self.label_error.place(x=80, y=290)
    
  def register(self):
    name = self.entry_name.get() 
    mail = self.entry_mail.get()
    pw = self.entry_pw.get()
    pw_con = self.entry_pw_con.get()
    role = self.radio_status.get()
    salt = db.get_salt()
    
    if name == '' or mail == '' or pw == '' or pw_con == '' or role == '':
      self.label_error.configure(text='入力されていない欄があります。')
      return
    if pw != pw_con:
      self.label_error.configure(text='パスワードが違います。')
      return
    if db.select_user(mail):
      self.label_error.configure(text='このメールアドレスは既に使用されています。')
      return
    
    hashed_pw = db.get_hashed_pw(pw, salt)
    
    db.register_user(name, mail, hashed_pw, salt, role)
    import login
    self.destroy()
    login.Login(self.master)

if __name__ == '__main__':
  root = tk.Tk()
  app = Register(master=root)
  Register(master=root)
  app.mainloop()