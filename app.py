# from crypt import methods
# from curses import echo
# from os import name
# from flask import Flask ,request, jsonify

# app = Flask(__name__)

# books_list=[
#     {
#         "id":"0",
#         "author":"samar elsayed",
#         "language":"english",
#         "title":"book1",
#     },
#     {
#         "id":"1",
#         "author":"talia mogeeth",
#         "language":"italian",
#         "title":"book2",
#     },
#     {
#         "id":"2",
#         "author":"hamza mogeeth",
#         "language":"frensh",
#         "title":"book3",
#     },
# ]


# @app.route('/')
# def index():
#     return 'hello world'

# @app.route('/books',methods=['GET','POST'])
# def books():
#     if request.method =='GET':
#         if len(books_list)>0:
#             return jsonify(books_list)
#         else:
#             'nothing found',404
#     if request.method =='POST':
#         new_author = request.form['author']
#         new_lang = request.form['language']
#         new_title = request.form['title']
#         iD =books_list[-1]
        
#         new_obj ={
#             'id':iD,
#             'author':new_author,
#             'language':new_lang,
#             'title':new_title,
#         }
#         books_list.append(new_obj)
#         return jsonify(books_list), 201
    
    
# @app.route('/book/<int:id>',methods=['GET','PUT','DELETE'])
# def single_book(id):
#     if request.method =='GET':
#         for book in books_list:
#             if book['id']==id:
#                 return jsonify(book)
#             pass
#     if request.method =='PUT':
#         for book in books_list:
#             if book['id'] == id:
#                 book['author']= request.form['author']
#                 book['language']= request.form['language']
#                 book['title']= request.form['title']
#                 update_book={
#                     'id':id,
#                     'author':book['author'],
#                     'language':book['language'],
#                     'title':book['title'],
#                 }
#                 return jsonify(update_book)
        
#     if request.method =='DELETE':
#         for index ,book in enumerate(books_list):
#             if book['id'] ==id:
#                 books_list.pop(index)
#                 return jsonify(books_list)
        
    
# if __name__ == "__main__":
#     app.run()
        
# from flask import Flask, request, jsonify
# import json
# import sqlite3

# app = Flask(__name__)


# def db_connection():
#     conn = None
#     try:
#         conn = sqlite3.connect("books.sqlite")
#     except sqlite3.error as e:
#         print(e)
#     return conn


# @app.route("/books", methods=["GET", "POST"])
# def books():
#     conn = db_connection()
#     cursor = conn.cursor()

#     if request.method == "GET":
#         cursor = conn.execute("SELECT * FROM book")
#         books = [
#             dict(id=row[0], author=row[1], language=row[2], title=row[3])
#             for row in cursor.fetchall()
#         ]
#         if books is not None:
#             return jsonify(books)

#     if request.method == "POST":
#         new_author = request.form["author"]
#         new_lang = request.form["language"]
#         new_title = request.form["title"]
#         sql = """INSERT INTO book (author, language, title)
#                  VALUES (?, ?, ?)"""
#         cursor = cursor.execute(sql, (new_author, new_lang, new_title))
#         conn.commit()
#         return f"Book with the id: 0 created successfully", 201


# @app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
# def single_book(id):
#     conn = db_connection()
#     cursor = conn.cursor()
#     book = None
#     if request.method == "GET":
#         cursor.execute("SELECT * FROM book WHERE id=?", (id,))
#         rows = cursor.fetchall()
#         for r in rows:
#             book = r
#         if book is not None:
#             return jsonify(book), 200
#         else:
#             return "Something wrong", 404

#     if request.method == "PUT":
#         sql = """UPDATE book
#                 SET title=?,
#                     author=?,
#                     language=?
#                 WHERE id=? """

#         author = request.form["author"]
#         language = request.form["language"]
#         title = request.form["title"]
#         updated_book = {
#             "id": id,
#             "author": author,
#             "language": language,
#             "title": title,
#         }
#         conn.execute(sql, (author, language, title, id))
#         conn.commit()
#         return jsonify(updated_book)

#     if request.method == "DELETE":
#         sql = """ DELETE FROM book WHERE id=? """
#         conn.execute(sql, (id,))
#         conn.commit()
#         return "The book with id: {} has been ddeleted.".format(id), 200


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='sql6.freesqldatabase.com',
            database='sql6474081',
            user='sql6474081',
            password='rlivYyUN5E',
            charset='utf8mb4',
            # cursorclass=pymysql.cursors.DictCursor
            cursorclass=pymysql.cursors.DictCursor,
    )
    except pymysql.Error as e:
        print(e)
    return conn


@app.route("/books", methods=["GET", "POST"])
def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT * FROM book")
        books = [
            dict(id=row['id'], author=row['author'], language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == "POST":
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        sql = """INSERT INTO book (author, language, title)
                 VALUES (%s, %s, %s)"""
        cursor = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: 0 created successfully", 201


@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE book
                SET title=?,
                    author=?,
                    language=?
                WHERE id=? """

        author = request.form["author"]
        language = request.form["language"]
        title = request.form["title"]
        updated_book = {
            "id": id,
            "author": author,
            "language": language,
            "title": title,
        }
        conn.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == "DELETE":
        sql = """ DELETE FROM book WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been ddeleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True)