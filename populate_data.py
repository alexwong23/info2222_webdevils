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
con.execute("INSERT INTO categories (name, type_id) VALUES ('Basic HTML', (?))", (html_id,))
con.execute("INSERT INTO categories (name, type_id) VALUES ('Formatting', (?))", (html_id,))
con.execute("INSERT INTO categories (name, type_id) VALUES ('Forms and Input', (?))", (html_id,))
con.execute("INSERT INTO categories (name, type_id) VALUES ('Styling Tags', (?))", (css_id,))

basic_html_id = cur.execute("SELECT id FROM categories WHERE name='Basic HTML'").fetchone()[0]
formatting_id = cur.execute("SELECT id FROM categories WHERE name='Formatting'").fetchone()[0]
styles_id = cur.execute("SELECT id FROM categories WHERE name='Styling Tags'").fetchone()[0]
def insert_content(title, description, category_id):
    con.execute("INSERT INTO content (title, description, category_id) VALUES ((?), (?), (?))", (title, description, category_id,))
insert_content('<!DOCTYPE>', 'Must be the very first thing in your HTML document, before the <html> tag', basic_html_id)
insert_content('<html>', 'Tell the browser that this is an HTML document', basic_html_id)
insert_content('<head>', 'A container for all the head elements', basic_html_id)
insert_content('<title>', 'Required in all HTML documents, defines the title of the document', basic_html_id)
insert_content('<body>', 'Defines the document\'s body, contains all the contents of an HTML document, such as text, hyperlinks, images, tables, lists, etc.', basic_html_id)
insert_content('<h1> to <h6>', 'Defines HTML headings, <h1> being the most important and <h6> being the least important heading.', basic_html_id)
insert_content('<p>', 'Defines a paragraph. Browsers automatically add some space (margin) before and after each <p> element. The margins can be modified with CSS (with the margin properties).', basic_html_id)
insert_content('<br>', 'Inserts a single line break. It is an empty tag which means that it has no end tag.', basic_html_id)
insert_content('<hr>', 'Defines a thematic break in an HTML page (e.g. a shift of topic). It is used to separate content (or define a change) in an HTML page.', basic_html_id)
insert_content('<abbr>', 'Defines an abbreviation or an acronym, like "Mr,", "ASAP", "ATM". Marking up abbreviations can give useful information to browsers, translation systems and search-engines.', formatting_id)
insert_content('<address>', 'Defines the contact information for the author/owner of a document or an article. Text in the element usually renders in italic.', formatting_id)
insert_content('<b>', 'Specifies bold text.', formatting_id)
insert_content('<bdi>', 'bdi stands for Bi-Directional Isolation. It isolates a part of text that might be formatted in a different direction from other text outside it.', formatting_id)
insert_content('<bdo>', 'bdo stands for Bi-Directional Override. It overrides the current text direction.', formatting_id)
insert_content('<blockquote>', 'Specifies a section that is quoted from another source. Browsers usually indent <blockquote> elements.', formatting_id)
insert_content('<cite>', 'Defines the title of a work (e.g. a book, a song, a movie, etc.). Note: A persons\'s name is not the title of a work.', formatting_id)
insert_content('<code>', 'It is a phrase tag. It defines a piece of computer code.', formatting_id)
insert_content('<del>', 'Defines text that has been deleted from a document.', formatting_id)
insert_content('<dfn>', 'Represents the defining instance of a term. The defining instance is often the first use of a term in a document.', formatting_id)
insert_content('<em>', 'It is a phrase tag. It renders as emphasized text.', formatting_id)
insert_content('<i>', 'Defines a part of text in an alternative voice or mood. The content of the <i> tag is usually displayed in italic. It can be used to indicate a technical term, a phrase from another language, etc.', formatting_id)
insert_content('<ins>', 'Defines a text that has been inserted into a document.', formatting_id)
insert_content('<kbd>', 'Defines keyboard input.', formatting_id)
insert_content('<mark>', 'Defines marked/highlighted text.', formatting_id)
insert_content('<meter>', 'Defines a scalar measurement within a known range (a gauge).', formatting_id)
insert_content('<pre>', 'Defines preformatted text.', formatting_id)
insert_content('<>', 'Comments are not displayed in the browsers.', formatting_id)
insert_content('class', 'classes can be set in html too', styles_id)



# merge into one table
con.execute("""CREATE TABLE all_content AS
        SELECT content.title, content.description,
        categories.name, category_types.name
        FROM content
        INNER JOIN categories ON content.category_id = categories.id
        INNER JOIN category_types ON categories.type_id = category_types.id """)
con.commit()
