import MySQLdb
import random
import hashlib
import hashlib

def get_connection():
  connection = MySQLdb.connect(user='root', 
                              password='hinata0703',
                              host='localhost',
                              database='book_management')
  return connection

def select_books():
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT * FROM books'
  cursor.execute(sql)
  books = cursor.fetchall()
  cursor.close()
  connection.close()
  return books

def get_salt():
  source = 'abcdefghijklmnopqrstuvwsyz1234567890'
  salt = ''
  for _ in range(20):
    random_salt = random.choice(source)
    salt += random_salt
  return salt
  
def get_hashed_pw(pw, salt):
  hashed_pw = hashlib.pbkdf2_hmac('sha256', pw.encode(), salt.encode(), 200).hex()
  return hashed_pw
  
def register_user(name, mail, hashed_pw, salt, role):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'INSERT INTO users(user_name, mail, hashed_pw, salt, role) VALUES (%s, %s, %s, %s, %s)'
  cursor.execute(sql, (name, mail, hashed_pw, salt, role))
  connection.commit()
  cursor.close()
  connection.close()
  
def select_user(mail):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT * from users WHERE mail = %s'
  cursor.execute(sql, (mail, ))
  user = cursor.fetchone()
  cursor.close()
  connection.close()
  return user

def insert_book(title, author, ISBN):
  connection =get_connection()
  cursor = connection.cursor()
  sql = 'INSERT INTO books (book_name, author, ISBN) VALUES(%s, %s, %s)'
  cursor.execute(sql, (title, author, ISBN))
  connection.commit()
  cursor.close()
  connection.close()
  
def check_role(mail):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT * FROM users WHERE mail = %s'
  cursor.execute(sql, (mail,))
  role = cursor.fetchone()
  cursor.close()
  connection.close()
  return role[5]

def insert_lending(user_id, book_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'INSERT INTO lending (user_id, book_id, lend_date, return_date) VALUES(%s, %s, now(), NULL)'
  cursor.execute(sql, (user_id, book_id))
  connection.commit()
  cursor.close()
  connection.close()
  
def select_lending(book_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT book_id FROM lending WHERE book_id = %s'
  cursor.execute(sql, (book_id, ))
  result = cursor.fetchone()
  cursor.close()
  connection.close()
  return result

def select_lend_books(book_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT lend_id, book_name,author, lend_date, return_date FROM books JOIN lending ON books.book_id = lending.book_id WHERE return_date is NULL and books.book_id = %s'
  cursor.execute(sql, (book_id,))
  will_return = cursor.fetchone()
  cursor.close()
  connection.close()
  return will_return

def update_null(lend_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'UPDATE lending SET return_date = now() WHERE lend_id = %s'
  cursor.execute(sql, (lend_id, ))
  connection.commit()
  cursor.close()
  connection.close()
  
def lending_books():
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT lend_id, book_name,author, lend_date, return_date FROM books JOIN lending ON books.book_id = lending.book_id WHERE return_date is NULL'
  cursor.execute(sql)
  all_books = cursor.fetchall()
  cursor.close()
  connection.close()
  return all_books

def all_lending_books():
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT lend_id, book_name,author, lend_date, return_date FROM books JOIN lending ON books.book_id = lending.book_id WHERE return_date is NULL'
  cursor.execute(sql)
  lending_books = cursor.fetchall()
  cursor.close()
  connection.close()
  return lending_books

def insert_log(user_id, book_id, lend_id, lend_date, return_date):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'INSERT INTO log (user_id, book_id, lend_id, lend_date, return_date) VALUES(%s, %s, %s, %s, %s)'
  cursor.execute(sql, (user_id, book_id, lend_id, lend_date, return_date))
  connection.commit()
  cursor.close()
  connection.close()

def select_lending_2(lend_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT * FROM lending WHERE lend_id = %s'
  cursor.execute(sql, (lend_id, ))
  result = cursor.fetchone()
  cursor.close()
  connection.close()
  return result

def select_book_id(lend_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT book_id FROM lending WHERE lend_id = %s'
  cursor.execute(sql, (lend_id,))
  book_id = cursor.fetchone()
  cursor.close()
  connection.close()
  return book_id

def select_log(book_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT log_id, book_name, lend_date, return_date FROM log JOIN books ON log.book_id = books.book_id WHERE books.book_id = %s'
  cursor.execute(sql, (book_id,))
  log = cursor.fetchone()
  cursor.close()
  connection.close()
  return log

def select_logs():
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT log_id, book_name, lend_date, return_date FROM log JOIN books ON log.book_id = books.book_id'
  cursor.execute(sql)
  logs = cursor.fetchall()
  cursor.close()
  connection.close()
  return logs

def update_retun_date(lend_id):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'UPDATE lending SET return_date = NULL WHERE lend_id = %s'
  cursor.execute(sql, (lend_id,))
  connection.commit()
  cursor.close()
  connection.close()
  
