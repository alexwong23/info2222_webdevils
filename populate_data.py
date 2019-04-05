import sqlite3
con = sqlite3.connect('./db/webdevils.db')
cur = con.cursor()

# create schema
con.execute("""CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, unikey char(8) NOT NULL,
        password char(50) NOT NULL, status int NOT NULL,
        first_name char(50) NOT NULL, last_name char(50) NOT NULL,
        date_created datetime NOT NULL)""")
con.commit()
con.execute("""CREATE TABLE user_sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT, token char(20) NOT NULL,
        date_created datetime NOT NULL, user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id))""")
con.commit()
con.execute("""CREATE TABLE messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_created datetime NOT NULL,
        text char(100),
        sender_id INTEGER,
        receiver_id INTEGER,
        receiver_unikey char(8) ,
        receiver_first_name char(50) ,
        receiver_last_name char(50) ,
        FOREIGN KEY(sender_id) REFERENCES users(id),
        FOREIGN KEY(receiver_id) REFERENCES users(id))""")
con.commit()
con.execute("""CREATE TABLE category_types (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name char(100))""")
con.commit()
con.execute("""CREATE TABLE categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name char(100), type_id INTEGER,
        FOREIGN KEY(type_id) REFERENCES category_types(id))""")
con.commit()
con.execute("""CREATE TABLE content (
        id INTEGER PRIMARY KEY AUTOINCREMENT, title char(100),
        description char(200), category_id INTEGER,
        FOREIGN KEY(category_id) REFERENCES categories(id))""")
con.commit()

users = [
    ('admin1', 'admin1', 1, 'Admin', 'WebDevils'),
    ('user2', 'password', 0, 'Alex', 'Wong'),
    ('user3', 'password', 0, 'Kirath', 'Singh'),
    ('user4', 'password', 0, 'Tim', 'Tam'),
    ('user5', 'password', 0, 'Alan', 'Fekete'),
    ('user6', 'password', 0, 'David', 'Black'),
    ('user7', 'password', 2, 'Muted', 'User'),
    ('user8', 'password', 3, 'Banned', 'User')
]


# 1 is admin
#remaining numbers are users
messages = [
    (2, 3, 'how are you user two?','user3','kirath','Singh'),
    (3, 2, 'good gee thanks user one','user2','Alex', 'Wong'),
    (2, 4, 'how are you user four?','user4','Tim', 'Tam'),
    (4, 2, 'Aye man all good','user2','Alex', 'Wong'),
    (2, 4, 'How is your momma doing?','user4','Tim', 'Tam'),
    (4, 2, 'she is doing well mate','user2','Alex', 'Wong'),
    (2, 5, 'how are you user five?','user5','Alan', 'Fekete'),
    (2, 5, 'you ther five?','user5','Alan', 'Fekete'),
    (5, 2, 'Yes yes i am here','user2','Alex', 'Wong')
]

# fake users and messages
con.executemany("INSERT INTO users (unikey, password, status, first_name, last_name, date_created) VALUES (?, ?, ?, ?, ?, datetime('now', 'localtime'))", users)
con.commit()
con.executemany("INSERT INTO messages (sender_id, receiver_id, text, receiver_unikey, receiver_first_name, receiver_last_name, date_created) VALUES (?, ?, ?, ?, ?, ?, datetime('now', 'localtime'))", messages)
con.commit()
# populate html and css content
con.execute("INSERT INTO category_types (name) VALUES ('HTML')")
con.commit()
con.execute("INSERT INTO category_types (name) VALUES ('CSS')")
con.commit()

# html_id = cur.execute("SELECT id FROM category_types WHERE name='HTML'").fetchone()[0]
# con.commit()
# css_id = cur.execute("SELECT id FROM category_types WHERE name='CSS'").fetchone()[0]
# con.commit()
html_id = 1
css_id = 2

categories = [
    ('Basic HTML', html_id),
    ('Formatting', html_id),
    ('Forms and Input', html_id),
    ('Properties', css_id),
    ('Selectors', css_id),
    ('Functions', css_id),
]

con.executemany("INSERT INTO categories (name, type_id) VALUES (?, ?)", categories)
con.commit()

basic_html_id = cur.execute("SELECT id FROM categories WHERE name='Basic HTML' AND type_id=(?)", (html_id,)).fetchone()[0]
con.commit()
formatting_id = cur.execute("SELECT id FROM categories WHERE name='Formatting' AND type_id=(?)", (html_id,)).fetchone()[0]
con.commit()
forms_id = cur.execute("SELECT id FROM categories WHERE name='Forms and Input' AND type_id=(?)", (html_id,)).fetchone()[0]
con.commit()
properties_id = cur.execute("SELECT id FROM categories WHERE name='Properties' AND type_id=(?)", (css_id,)).fetchone()[0]
con.commit()
selectors_id = cur.execute("SELECT id FROM categories WHERE name='Selectors' AND type_id=(?)", (css_id,)).fetchone()[0]
con.commit()
functions_id = cur.execute("SELECT id FROM categories WHERE name='Functions' AND type_id=(?)", (css_id,)).fetchone()[0]
con.commit()

content = [
    ('<!DOCTYPE>', 'Must be the very first thing in your HTML document, before the <html> tag', basic_html_id),
    ('<html>', 'Tell the browser that this is an HTML document', basic_html_id),
    ('<head>', 'A container for all the head elements', basic_html_id),
    ('<title>', 'Required in all HTML documents, defines the title of the document', basic_html_id),
    ('<body>', 'Defines the document\'s body, contains all the contents of an HTML document, such as text, hyperlinks, images, tables, lists, etc.', basic_html_id),
    ('<h1> to <h6>', 'Defines HTML headings, <h1> being the most important and <h6> being the least important heading.', basic_html_id),
    ('<p>', 'Defines a paragraph. Browsers automatically add some space (margin) before and after each <p> element. The margins can be modified with CSS (with the margin properties).', basic_html_id),
    ('<br>', 'Inserts a single line break. It is an empty tag which means that it has no end tag.', basic_html_id),
    ('<hr>', 'Defines a thematic break in an HTML page (e.g. a shift of topic). It is used to separate content (or define a change) in an HTML page.', basic_html_id),
    ('<abbr>', 'Defines an abbreviation or an acronym, like "Mr,", "ASAP", "ATM". Marking up abbreviations can give useful information to browsers, translation systems and search-engines.', formatting_id),
    ('<address>', 'Defines the contact information for the author/owner of a document or an article. Text in the element usually renders in italic.', formatting_id),
    ('<b>', 'Specifies bold text.', formatting_id),
    ('<bdi>', 'bdi stands for Bi-Directional Isolation. It isolates a part of text that might be formatted in a different direction from other text outside it.', formatting_id),
    ('<bdo>', 'bdo stands for Bi-Directional Override. It overrides the current text direction.', formatting_id),
    ('<blockquote>', 'Specifies a section that is quoted from another source. Browsers usually indent <blockquote> elements.', formatting_id),
    ('<cite>', 'Defines the title of a work (e.g. a book, a song, a movie, etc.). Note: A persons\'s name is not the title of a work.', formatting_id),
    ('<code>', 'It is a phrase tag. It defines a piece of computer code.', formatting_id),
    ('<del>', 'Defines text that has been deleted from a document.', formatting_id),
    ('<dfn>', 'Represents the defining instance of a term. The defining instance is often the first use of a term in a document.', formatting_id),
    ('<em>', 'It is a phrase tag. It renders as emphasized text.', formatting_id),
    ('<i>', 'Defines a part of text in an alternative voice or mood. The content of the <i> tag is usually displayed in italic. It can be used to indicate a technical term, a phrase from another language, etc.', formatting_id),
    ('<ins>', 'Defines a text that has been inserted into a document. Browsers will normally strike a line through deleted text and underline inserted text.', formatting_id),
    ('<kbd>', 'Defines keyboard input.', formatting_id),
    ('<mark>', 'Defines marked/highlighted text.', formatting_id),
    ('<meter>', 'Defines a scalar measurement within a known range (a gauge).', formatting_id),
    ('<pre>', 'Defines preformatted text.', formatting_id),
    ('<progress>', 'Represents the progress of a task.', formatting_id),
    ('<q>', 'Defines a short quotation.', formatting_id),
    ('<rp>', 'Defines what to show in browsers that do not support ruby annotations.', formatting_id),
    ('<rt>', 'Defines an explanation/pronounciation of characters (for East Asian typography).', formatting_id),
    ('<ruby>', 'Defines a ruby annotation (for East Asian typography).', formatting_id),
    ('<s>', 'Defines text that is no longer correct.', formatting_id),
    ('<samp>', 'Defines sample output from a computer program.', formatting_id),
    ('<small>', 'Defines smaller text.', formatting_id),
    ('<strong>', 'Defines important text.', formatting_id),
    ('<sub>', 'Defines superscripted text.', formatting_id),
    ('<template>', 'Defines a template.', formatting_id),
    ('<time>', 'Defines a date/time.', formatting_id),
    ('<u>', 'Defines text that should be stylistically different from normal text.', formatting_id),
    ('<var>', 'Defines a variable.', formatting_id),
    ('<wbr>', 'Defines a possible line-break.', formatting_id),
    ('align-content', 'Specifies the alignment between the lines inside a flexible container when the items do not use all available space.', forms_id),
    ('backface-visibility', 'Defines whether or not the back face of an element should be visible when facing the user.', forms_id),
    ('caption-side', 'Specifies the placement of a table caption.', forms_id),
    ('direction', 'Specifies the text direction/writing direction.', forms_id),
    ('empty-cells', 'Specifies whether or not to display borders and background on empty cells in a table.', forms_id),
    ('.class', 'Example .intro: Selects all elements with class="intro".', selectors_id),
    ('#id', 'Example #firstname: Selects the element with id="firstname".', selectors_id),
    ('*', 'Example *: Selects all elements.', selectors_id),
    ('element ', 'Example p: Selects all <p> elements.', selectors_id),
    ('element,element', 'Example div, p: Selects all <div> elements and all <p> elements.', selectors_id),
    ('attr()', 'Returns the value of an attribute of the selected element.', functions_id),
    ('calc()', 'Allows you to perform calculations to determine CSS property values.', functions_id),
    ('cubic-bezier()', 'Defines a Cubic Bezier curve.', functions_id),
    ('hsl()', 'Defines colors using the Hue-Saturation-Lightness model (HSL).', functions_id),
    ('hsla()', 'Defines colors using the Hue-Saturation-Lightness-Alpha model (HSLA).', functions_id)
]

con.executemany("INSERT INTO content (title, description, category_id) VALUES ((?), (?), (?))", content)
con.commit()

# merge into one table
con.execute("""CREATE TABLE all_content AS
        SELECT content.title, content.description,
        categories.name , category_types.name AS category_type
        FROM content
        INNER JOIN categories ON content.category_id = categories.id
        INNER JOIN category_types ON categories.type_id = category_types.id """)
con.commit()
