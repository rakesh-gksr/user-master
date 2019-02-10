import datetime

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from project import db

from project.api.models.quotes import AuthorSchema, QuoteSchema, Author, Quote


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True, only=('id', 'content'))

##### API #####
quotes_blueprint = Blueprint('quotes', __name__)

@quotes_blueprint.route('/quotes/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    # Serialize the queryset
    result = authors_schema.dump(authors)
    return jsonify({'authors': result})


@quotes_blueprint.route('/quotes/authors/<int:pk>', methods=['GET'])
def get_author(pk):
    try:
        author = Author.query.get(pk)
    except :
        return jsonify({'message': 'Author could not be found.'}), 400
    author_result = author_schema.dump(author)
    quotes_result = quotes_schema.dump(author.quotes.all())
    return jsonify({'author': author_result, 'quotes': quotes_result})

@quotes_blueprint.route('/quotes/', methods=['GET'])
def get_quotes():
    quotes = Quote.query.all()
    result = quotes_schema.dump(quotes, many=True)
    return jsonify({'quotes': result})

@quotes_blueprint.route('/quotes/<int:pk>', methods=['GET'])
def get_quote(pk):
    try:
        quote = Quote.query.get(pk)
    except :
        return jsonify({'message': 'Quote could not be found.'}), 400
    result = quote_schema.dump(quote)
    return jsonify({'quote': result})


@quotes_blueprint.route('/quotes', methods=['POST'])
def new_quote():
    json_data = request.get_json()
    # print "json_data==>",json_data
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400
    # Validate and deserialize input
    try:
        data = quote_schema.load(json_data)
        import pprint
        pprint.pprint(data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    return jsonify({
        'message': 'Created new quote.',
        'quote': True,
    })
    first, last = data[0]['author']['first'], data[0]['author']['last']
    author = Author.query.filter_by(first=first, last=last).first()
    if author is None:
        # Create a new author
        author = Author(first=first, last=last)
        db.session.add(author)
    # Create new quote
    quote = Quote(
        content=data[0]['content'],
        author=author,
        posted_at=datetime.datetime.utcnow(),
    )
    db.session.add(quote)
    db.session.commit()
    result = quote_schema.dump(Quote.query.get(quote.id))
    return jsonify({
        'message': 'Created new quote.',
        'quote': result,
    })
