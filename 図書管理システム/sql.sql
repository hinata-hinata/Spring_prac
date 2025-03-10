CREATE TABLE users(
  user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_name VARCHAR(255) NOT NULL,
  mail VARCHAR(255) NOT NULL UNIQUE,
  hashed_pw VARCHAR(64) NOT NULL,
  salt VARCHAR(20),
  role INTEGER NOT NULL
);

CREATE TABLE books(
  book_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  book_name VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  ISBN VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE lending(
  lend_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL UNIQUE,
  lend_date DATETIME NOT NULL,
  return_date DATETIME ,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- CREATE TABLE log(
--   log_id INTEGER PRIMARY KEY AUTO_INCREMENT,
--   user_id INTEGER NOT NULL,
--   book_id INTEGER NOT NULL,
--   lend_id INTEGER NOT NULL,
--   lend_date DATETIME NOT NULL,
--   return_date DATETIME ,
--   FOREIGN KEY (user_id) REFERENCES users(user_id),
--   FOREIGN KEY (book_id) REFERENCES books(book_id),
--   FOREIGN KEY (lend_id) REFERENCES lending(lend_id)
-- );

CREATE TABLE log(
  log_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  user_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  lend_id INTEGER NOT NULL,
  lend_date DATETIME NOT NULL,
  return_date DATETIME
);