from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    Date,
)

from .meta import Base


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    fname = Column(Unicode)
    lname = Column(Unicode)
    uname = Column(Unicode)
    pword = Column(Unicode)
    email_add = Column(Unicode)
    food = Column(Unicode)

Index('my_index', Entry.uname, unique=True, mysql_length=255)
