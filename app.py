from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

books=[] #lege array waar ik alle objecten van boeken opsla





@app.route('/')
def hello_world():
    return render_template('index.html', books=books)


@app.route('/library')
def library():
    return render_template('library.html', books=books)

@app.route('/addBooks', methods=['POST'])
def add_books():
    if request.method == "POST":
        title = request.form['Titel']
        author = request.form['Author']
        year = request.form['Year']

        # Check for duplicates
        for book in books:
            if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
                # Render the page with a duplicate warning
                return render_template('addbooks.html', duplicate=True)

        # If no duplicate, add the book
        books.append({"year": year, "title": title, "author": author})
        print(books)

        return redirect(url_for('library'))



@app.route('/readbook/<int:book_id>')
def readbook(book_id):
    book = books[book_id]

    book_content = [
        {"chapter": 1, "title": "Introduction to Selection Lab", "text": "Selection Lab is a company dedicated to fostering innovation and providing exceptional solutions to modern challenges."},
        {"chapter": 2, "title": "Our Mission", "text": "At Selection Lab, our mission is to empower businesses and individuals through cutting-edge technology and unparalleled support."},
        {"chapter": 3, "title": "Our Vision", "text": "We envision a world where every challenge is met with creativity and every problem finds a smart solution."},
        {"chapter": 4, "title": "Core Values", "text": "Integrity, innovation, and customer-centricity are at the heart of everything we do at Selection Lab."},
        {"chapter": 5, "title": "The Future", "text": "Selection Lab aims to expand its reach and continue leading the way in technological excellence."}
    ]
    return render_template('readbook.html', book_content=book_content, book=book, )


@app.route('/insertBooks')
def insert_books():
    return render_template('addbooks.html')


if __name__ == '__main__':
    app.run()

