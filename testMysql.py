from sqlalchemy import Column,String,create_engine
from sqlalchemy.types import CHAR,Integer,String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

Base = declarative_base()
class App(Base):
    __tablename__ = 'app'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    cn_name = Column(String(32))
    desc = Column(Text)
    status = Column(Integer)
class User(Base):
    __tablename__ = 't_user'
    userid = Column('userid',Integer,primary_key=True,nullable=True)
    username = Column('username',String(64),nullable=True)
    password = Column('password',String(64),nullable=True)


engine = create_engine('mysql://root:s12345678@localhost/test')

Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()

ed_user = User(userid='1', username='ABCV', password='errorpasswd')
session.add(ed_user)

for instance in session.query(User).order_by(User.userid):
    print(instance.username)


session.commit()
session.close()