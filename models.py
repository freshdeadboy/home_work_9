from mongoengine import Document, StringField, ListField

class Author(Document):
    name = StringField(required=True, unique=True)

class Quote(Document):
    text = StringField(required=True)
    author = StringField(required=True)
