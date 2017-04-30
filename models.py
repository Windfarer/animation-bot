from mongoengine import Document, StringField, ListField


class Animation(Document):
    movie_name = StringField()
    tt_id = StringField(primary_key=True)
    characters = ListField()
