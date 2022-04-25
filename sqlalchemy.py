import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, VARCHAR
from sqlalchemy.engine import result
from sqlalchemy.orm import declarative_base

db = declarative_base()

engine = create_engine(
    "database+dialect://username:password@hostname:3306/imdb")

meta = MetaData(bind=engine)
MetaData.reflect(meta)

tbimdb = Table(db.Model)(
    'imdb', meta,
    Column('season',Integer),
    Column('episode_num',Integer),
    Column('title',VARCHAR, primary_key=True, nullable=False ),
    Column('original_air_date',VARCHAR),
    Column('imdb_rating',Numeric),
    Column('total_votes',Numeric),
    Column('desc',VARCHAR)

)

tbimdb.query.filter(tbimdb.desc.contains('Amy'))