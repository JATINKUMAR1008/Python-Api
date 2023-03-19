from flask import request,json,jsonify
from app import app
from flask_marshmallow import Marshmallow
from app import db
from components import Orders
ma=Marshmallow(app)

class Books(db.Model):
    name=db.Column(db.String)
    price=db.Column(db.Integer)
    Book_id=db.Column(db.Integer,primary_key=True)#author's name, description, rating, reviews.
    Release = db.Column(db.String)
    genre=db.Column(db.String)
    copy = db.Column(db.String)
    author= db.Column(db.String)
    publisher= db.Column(db.String)
    ratings=db.Column(db.Integer)
    Msrp=db.Column(db.Integer)
    edition = db.Column(db.String)
    atb=db.Column(db.String)
    
    

    def __init__ (self,name,price,Release,genre,copy,author,publisher,ratings,Msrp,edition,atb):
        self.name=name
        self.price=price
        self.Release=Release
        self.genre=genre
        self.copy=copy
        self.author=author
        self.publisher=publisher
        self.ratings=ratings
        self.Msrp=Msrp
        self.edition=edition
        self.atb=atb
    

class BookSchema(ma.Schema):
    class Meta:
        fields=('Book_id','name','price','Release','genre','copy','author','publisher','ratings','Msrp','edition','atb')



book_schemas=BookSchema(many=True)
book_schema=BookSchema()

db.create_all()



@app.route('/add_books',methods=['POST'])
def add_books():
    name=request.json['name']
    price=request.json['price']
    Release=request.json['Realease']
    genre=request.json['genre']
    copy=request.json['copy']
    author=request.json['author']
    publisher=request.json['publisher']
    ratings=request.json['ratings']
    Msrp=request.json['Msrp']
    edition=request.json['edition']
    atb=request.json['atb']
    new_Book = Books(name,price,Release,genre,copy,author,publisher,ratings,Msrp,edition,atb)
    db.session.add(new_Book)
    db.session.commit()
    return book_schema.jsonify(new_Book)

@app.route('/books',methods=['GET'])
def get_books():
    all_books=Books.query.all()
    result = book_schemas.dump(all_books)
    return jsonify(result)
