from flaskLearn.model import db

class Blog():

    class Field():
        author ="author",
        text ="text",
        tags ="tags",
        create_date = "create_date"

    collection = db.blog


