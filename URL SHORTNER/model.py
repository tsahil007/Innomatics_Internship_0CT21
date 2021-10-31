from project import db


class History(db.Model):
    url_user = db.Column(db.String(200), primary_key=True)
    shorten_url = db.Column(db.String(20), nullable=False)
