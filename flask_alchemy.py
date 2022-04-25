from ntpath import join
from flask import Flask
from flask_alchemy import SQLAlchemy
from datetime import datetime





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////imdb.db'

db = SQLAlchemy(app)

class imdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)



class IMDB(db.Model):
    imdb_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    imdb_rating = db.Column(db.Integer(80), nullable=False)
    total_votes = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String, nullable=False,)
    # one to one relation ship
    directors = db.relationship('Directed_by', backref= 'IMDB', uselist= False)
    #one to many
    writters = db.relationship('Written_by', backref= 'IMDB')
    #one to many
    teleplayer = db.relationship('Teleplay_by', backref= 'IMDB')
    #one to one
    episodes = db.relationship('episodes', backref= 'IMDB', uselist= False)





class Directed_by(db.Model):
    director_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    imdb_id = db.Column(db.Integer,db.ForeignKey('IMDB.imdb_id'))




class Written_by(db.Model):
    writter_id = db.Column(db.Integer, primary_key=True)
    prod_code = db.Column(db.String(80), nullable=False)
    imdb_id = db.Column(db.Integer,db.ForeignKey('IMDB.imdb_id'))



class Teleplay_by(db.Model):
    teleplay_id = db.Column(db.Integer, primary_key=True)
    prod_code = db.Column(db.String(80), nullable=False)
    imdb_id = db.Column(db.Integer,db.ForeignKey('IMDB.imdb_id'))
    

class episodes(db.Model):
    episode_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    season = db.Column(db.Integer,nullable=False)
    episode_num_in_season = db.Column(db.Integer,nullable=False)
    original_air_date = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    prod_code = db.Column(db.Integer,nullable=False)
    us_viewers = db.Column(db.Integer,nullable=False)
    imdb_id = db.Column(db.Integer,db.ForeignKey('IMDB.imdb_id'))




def average_rating():
    print('average imdb rating:')

    db.session.query(
    Directed_by.director_id,Written_by.writter_id,Teleplay_by.teleplay_id,IMDB.imdb_id,
    join(Directed_by).join(Written_by).join(Teleplay_by).db.fun.avg('%n',Directed_by.imdb_rating),
             
    ).groupby()
    db.session.query(Directed_by.director_id,Written_by.writter_id,Teleplay_by.teleplay_id,IMDB.imdb_id,
       join(Directed_by).join(Written_by).join(Teleplay_by).db.fun.avg('%n',Written_by.imdb_rating),
    ).groupby()
    db.session.query(Directed_by.director_id,Written_by.writter_id,Teleplay_by.teleplay_id,IMDB.imdb_id,
        join(Directed_by).join(Written_by).join(Teleplay_by).db.fun.avg('%n',Teleplay_by.imdb_rating),      
    ).groupby()


    