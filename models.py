
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import db


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    completed = db.column(db.boolean, nullable=False, default=False)
    upcoming_shows=db.column(db.String(500))
    past_show=db.column(db.String(500))
    website_link=db.Column(db.String(120))
    genres=db.Column(ARRAY(String))
    seeking_talent=db.Column(db.boolean)
    seeking_description=db.column(db.String(500))
    shows=db.relationship('Show', backref='venue', lazy='dynamic')
    def __repr__(self):
        return '<Venue {}>'.format(self.name)


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    completed = db.column(db.boolean, nullable=False, default=False)
    website_link=db.Column(db.String(120))
    upcoming_shows=db.column(db.String(500))
    past_show=db.column(db.String(500))
    shows=db.relationship('Show', backref='artist', lazy='dynamic')

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class show(db.model):
  __tablename__ = 'show'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
  artist_name=db.Column(db.String)
  Venue_id = db.column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
  venue_name=db.Column(db.String)
  completed = db.column(db.boolean, nullable=False, default=False)
  start_time=db.column(db.String(200))
  artist_image_link=db.column(db.String(500))
  def __repr__(self):
        return '<Show {}{}>'.format(self.artist_id, self.venue_id)
 