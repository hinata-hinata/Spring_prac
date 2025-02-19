import tkinter as tk
from tkinter import ttk
import db
from tkinter import messagebox

class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master, width=600, height=600)
    self.pack()

    master.geometry('600x600')
    master.title('Hello Tkinter')

    self.create_widgets()


  def create_widgets(self):
    self.treeview = ttk.Treeview(self, show='headings', height=10)
    self.treeview.place(x=80, y=30)
    
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
      
    self.button = tk.Button(self, text='選択', command=self.click_event)
    self.button.place(x=100, y=400)
    
  def click_event(self):
    selected_row_id = self.treeview.selection()
    selected_row_data = self.treeview.item(selected_row_id, option='values')
    print(selected_row_data)

if __name__ == '__main__':
  root = tk.Tk()
  app = Application(master=root)
  app.mainloop()