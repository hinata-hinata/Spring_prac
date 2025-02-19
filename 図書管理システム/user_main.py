import tkinter as tk
import db
from tkinter import ttk
from tkinter import messagebox

class User_main(tk.Frame):
  def __init__(self, master, user_id):
    super().__init__(master, width=600, height=600)
    self.master = master
    self.user_id = user_id
    self.pack()

    master.geometry('600x600')
    master.title('利用者画面')

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
      
    self.button_borrow = tk.Button(self, text='借りる', command=self.borrow)
    self.button_borrow.place(x=450, y=50)
    
    self.label_borrow_book_list = tk.Label(self, text='かりている本')
    self.label_borrow_book_list.place(x=30, y=280)
    
    
    #借りている本一覧
    self.treeview_2 = ttk.Treeview(self, show='headings', height=5)
    self.treeview_2.place(x=30, y=330)
    
    header = ('id', 'title', 'author', 'lend_date', 'return_date')
    self.treeview_2.configure(columns=header)
    
    self.treeview_2.heading('id', text='ID')
    self.treeview_2.heading('title', text='題名')
    self.treeview_2.heading('author', text='著者')
    self.treeview_2.heading('lend_date', text='借りた日')
    self.treeview_2.heading('return_date', text='返却日')
    
    self.treeview_2.column('id', width=30, anchor='center')
    self.treeview_2.column('title', width=110, anchor='center')
    self.treeview_2.column('author', width=110, anchor='center')
    self.treeview_2.column('lend_date', width=120, anchor='center')
    self.treeview_2.column('return_date', width=120, anchor='center')
    
    lend_books = db.lending_books()
    for lend_book in lend_books:
      self.treeview_2.insert('', index='end', values=lend_book)
      
    self.button_return = tk.Button(self, text='返却', command=self.return_book)
    self.button_return.place(x=50, y=500)

  def return_book(self):
    selected_retun_id = self.treeview_2.selection()
    if len(selected_retun_id) == 1:
      selected_retun_data = self.treeview_2.item(selected_retun_id, option='values')
      db.update_null(selected_retun_data[0])
      
      #リフレッシュ
      for item in self.treeview_2.get_children():
        self.treeview_2.delete(item)
        
      all_lending_books = db.all_lending_books()
      for lending_book in all_lending_books:
        self.treeview_2.insert('', index='end', values=lending_book)
     
     #リセット 
    # books = db.select_books()
    # for book in books:
    #   self.treeview.insert('', index='end', values=book)
    # lend_books = db.select_lend_books()
    
    # for lend_book in lend_books:
    #   self.treeview_2.insert('', index='end', values=lend_book)
    
  def borrow(self):
    selected_row_id = self.treeview.selection()
    if len(selected_row_id) == 1:
      selected_row_data = self.treeview.item(selected_row_id, option='values')
      book_id = selected_row_data[0]

      if db.select_lending(book_id) == None:
        db.insert_lending(self.user_id, book_id)
        messagebox.showinfo('借りる', '本を借りました。')
        
        #返却テーブルを更新
        lend_book = db.select_lend_books(book_id)
        self.treeview_2.insert('', index='end', values=lend_book)
      else:
        messagebox.showinfo('借りる', 'この本は既に借りられています。')
    else:
      pass
        

if __name__ == '__main__':
  root = tk.Tk()
  app = User_main(master=root)
  app.mainloop()