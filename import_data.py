import json
from mongoengine import connect
from models import Author, Quote

def import_data(authors_filename, quotes_filename):
    connect('Сluster0', host='mongodb+srv://zajchuk2014:GFnbFetD2EaVWVJh@cluster0.lxirfac.mongodb.net/')

    with open(authors_filename, 'r') as f:
        authors_data = json.load(f)
        for author_name in authors_data:
            author = Author(name=author_name)
            author.save()

    with open(quotes_filename, 'r') as f:
        quotes_data = json.load(f)
        for quote_data in quotes_data:
            quote = Quote(text=quote_data['text'], author=quote_data['author'])
            quote.save()

if __name__ == "__main__":
    import_data('authors.json', 'quotes.json')
