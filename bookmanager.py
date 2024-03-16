import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data/bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Book(db.Model):
    ##title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    title = db.Column(db.String(80), unique=True, primary_key=True)
    author = db.Column(db.String(80), nullable=True, primary_key=False)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
        #return "<Author: {}>".format(self.author)

@app.route("/", methods=["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            ##book = Book(title=request.form.get("title"))
            book1 = Book(title=request.form.get("title"))
            book2 = Book(author=request.form.get("author"))
            db.session.add(book1)
            db.session.add(book2)
            db.session.commit()

        except Exception as e:
            print("Failed to add book")
            print(e)

    books = Book.query.all()
    return render_template("home.html",books=books)
 
@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()

    except Exception as e:
        print("Couldn't update book title")
        print(e)

    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', debug=True)

