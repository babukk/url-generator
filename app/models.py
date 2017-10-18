
from app import db, ma

# --------------------------------------------------------------------------------------------------
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    author = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(2000), default="")
    slug = db.Column(db.String(256), unique=False)

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

    def  __getitem__(self, item):
        return getattr(self, item)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'description': self.description,
        }

    # def __repr__(self):
    #    return '<Book %r>' % (self.title)

# --------------------------------------------------------------------------------------------------
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'description', 'slug',)


book_schema = BookSchema()
books_schema = BookSchema(many=True)
