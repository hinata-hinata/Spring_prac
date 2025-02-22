import tkinter as tk
from tkinter import ttk
import db
from tkinter import messagebox

class Manage(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=600, height=600)
    self.master = master
    self.pack()

    master.geometry('600x600')
    master.title('管理者画面')

    self.create_widgets()


  def create_widgets(self):
    self.treeview = ttk.Treeview(self, show='headings', height=10)
    self.treeview.place(x=60, y=30)
    
    header = ('id', 'title', 'author', 'ISBN')
    self.treeview.configure(columns=header)
    
    self.treeview.heading('id', text='ID')
    self.treeview.heading('title', text='題名')
    self.treeview.heading('author', text='著者')
    self.treeview.heading('ISBN', text='ISBN')
    # self.treeview.heading('publish_date', text='出版日')
    
    self.treeview.column('id', width=30, anchor='center')
    self.treeview.column('title', width=120, anchor='center')
    self.treeview.column('author', width=120, anchor='center')
    self.treeview.column('ISBN', width=90, anchor='center')
    # self.treeview.column('publish_date', width=80, anchor='center')
    
    books = db.select_books()
    for book in books:
      self.treeview.insert('', index='end', values=book)
    
    self.label_title = tk.Label(self, text='題名')
    self.label_author = tk.Label(self, text='著者')
    self.label_isbn = tk.Label(self, text='ISBN')
    self.label_title.place(x=50, y=300)
    self.label_author.place(x=50, y=340)
    self.label_isbn.place(x=50, y=380)
    
    self.entry_title = tk.Entry(self)
    self.entry_author = tk.Entry(self)
    self.entry_isbn = tk.Entry(self)
    self.entry_title.place(x=100, y=300)
    self.entry_author.place(x=100, y=340)
    self.entry_isbn.place(x=100, y=380)
    
    self.label_error = tk.Label(self, text='', fg='red')
    self.label_error.place(x=100, y=410)

    self.button_add = tk.Button(self, text='追加', command=self.add_book)
    self.button_add.place(x=50, y=440)
    
    self.button_del = tk.Button(self, text='削除', command=self.del_book)
    self.button_del.place(x=450, y=100)
    
    self.button_return = tk.Button(self, text='戻る', command=self.return_login)
    self.button_return.place(x=450, y=400)
    
  def return_login(self):
    import login
    self.destroy()
    login.Login(self.master)
    
  def del_book(self):
    selected_row_id = self.treeview.selection()
    selected_row_data = self.treeview.item(selected_row_id, option='values')
    db.del_lending_book(selected_row_data[0])
    db.del_book(selected_row_data[0])
    self.treeview.delete(selected_row_id)
    messagebox.showinfo('削除', '本を削除しました。')
    
  def add_book(self):
    title = self.entry_title.get()
    author = self.entry_author.get()
    isbn = self.entry_isbn.get()
    
    if title == '' or author == '' or isbn == '':
      self.label_error.configure(text='入力されていないフォームがあります。')
      return
      
    db.insert_book(title, author, isbn)
    self.label_error.configure(text='')
    self.entry_title.delete(0, tk.END)
    self.entry_author.delete(0, tk.END)
    self.entry_isbn.delete(0, tk.END)
    messagebox.showinfo('登録完了', '本の登録が完了しました。')
    
    #ツリービュー更新
    for item in self.treeview.get_children():
      self.treeview.delete(item)
    
    books = db.select_books()
    for book in books:
      self.treeview.insert('', index='end', values=book)

if __name__ == '__main__':
  root = tk.Tk()
  app = Manage(master=root)
  app.mainloop()