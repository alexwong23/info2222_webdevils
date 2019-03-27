import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()

# create schema
con.execute("""CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, unikey char(8) NOT NULL,
        password char(50) NOT NULL, status int NOT NULL,
        first_name char(50) NOT NULL, last_name char(50) NOT NULL,
        date_created datetime NOT NULL)""")

con.execute("""CREATE TABLE messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text char(100), date_created datetime NOT NULL,
        sender_id INTEGER, receiver_id INTEGER,
        FOREIGN KEY(sender_id) REFERENCES users(id),
        FOREIGN KEY(receiver_id) REFERENCES users(id))""")

con.execute("""CREATE TABLE category_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name char(100))""")

con.execute("""CREATE TABLE categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name char(100), type_id INTEGER,
        FOREIGN KEY(type_id) REFERENCES category_types(id))""")

con.execute("""CREATE TABLE content (
        id INTEGER PRIMARY KEY AUTOINCREMENT, title char(100),
        description char(200), category_id INTEGER,
        FOREIGN KEY(category_id) REFERENCES categories(id))""")


# fake users and messages
con.execute("INSERT INTO users (unikey, password, status, first_name, last_name, date_created) VALUES ('admin001', 'admin001', 1, 'Admin', 'WebDevils', datetime('now', 'localtime'))")
con.execute("INSERT INTO users (unikey, password, status, first_name, last_name, date_created) VALUES ('user1', 'password', 0, 'User', 'One', datetime('now', 'localtime'))")
con.execute("INSERT INTO users (unikey, password, status, first_name, last_name, date_created) VALUES ('user2', 'password', 0, 'User', 'Two', datetime('now', 'localtime'))")

user1_id = cur.execute("SELECT id FROM users WHERE unikey='user1'").fetchone()[0]
user2_id = cur.execute("SELECT id FROM users WHERE unikey='user2'").fetchone()[0]
con.execute("INSERT INTO messages (sender_id, receiver_id, text, date_created) VALUES ((?), (?), 'how are you user two?', datetime('now', 'localtime'))", (user1_id, user2_id,))
con.execute("INSERT INTO messages (sender_id, receiver_id, text, date_created) VALUES ((?), (?), 'good gee thanks user one', datetime('now', 'localtime'))", (user2_id, user1_id,))

# populate html and css content
con.execute("INSERT INTO category_types (name) VALUES ('HTML')")
con.execute("INSERT INTO category_types (name) VALUES ('CSS')")

html_id = cur.execute("SELECT id FROM category_types WHERE name='HTML'").fetchone()[0]
css_id = cur.execute("SELECT id FROM category_types WHERE name='CSS'").fetchone()[0]
con.execute("INSERT INTO categories (name, type_id) VALUES ('Front end Tags', (?))", (html_id,))
con.execute("INSERT INTO categories (name, type_id) VALUES ('Styling Tags', (?))", (css_id,))

tags_id = cur.execute("SELECT id FROM categories WHERE name='Front end Tags'").fetchone()[0]
styles_id = cur.execute("SELECT id FROM categories WHERE name='Styling Tags'").fetchone()[0]
con.execute("INSERT INTO content (title, description, category_id) VALUES ('<div>', 'div tags help to do great things', (?))", (tags_id,))
con.execute("INSERT INTO content (title, description, category_id) VALUES ('class', 'classes can be set in html too', (?))", (styles_id,))


# merge into one table
con.execute("""CREATE TABLE all_content AS
        SELECT content.title, content.description,
        categories.name, category_types.name
        FROM content
        INNER JOIN categories ON content.category_id = categories.id
        INNER JOIN category_types ON categories.type_id = category_types.id """)
con.commit()
