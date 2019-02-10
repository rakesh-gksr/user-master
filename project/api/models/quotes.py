# project/api/models/quotes.py
from marshmallow import Schema, fields, ValidationError, pre_load

from project import db

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))

class Quote(db.Model):
    __tablename__ = "quote"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship(
        'Author',
        backref=db.backref('quotes', lazy='dynamic'),
    )
    posted_at = db.Column(db.DateTime)

##### SCHEMAS #####


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    first = fields.Str()
    last = fields.Str()
    # formatted_name = fields.Method('format_name', dump_only=True)
    #
    # def format_name(self, author):
    #     return '{}, {}'.format(author.last, author.first)


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')

class QuoteSchema(Schema):
    id = fields.Int(dump_only=True)
    author = fields.Nested(AuthorSchema, validate=must_not_be_blank)
    content = fields.Str(required=True, validate=must_not_be_blank)
    posted_at = fields.DateTime(dump_only=True)

    # Allow client to pass author's full name in request body
    # e.g. {"author': 'Tim Peters"} rather than {"first": "Tim", "last": "Peters"}
    @pre_load
    def process_author(self, data):
        author_name = data.get('author')
        if author_name:
            first, last = author_name.split(' ')
            author_dict = dict(first=first, last=last)
        else:
            author_dict = {}
        data['author'] = author_dict
        return data
