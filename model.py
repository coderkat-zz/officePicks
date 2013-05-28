from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref


engine = create_engine("sqlite:///op.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit=False,
                         autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(64))
    password = Column(String(64))
    series_id = Column(Integer, ForeignKey("series.id"), nullable=True)

    series = relationship("Series", backref=backref("admin", order_by=id))


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey("admin.id"))
    team = Column(String(128))
    total_games = Column(Integer)

    admin = relationship("Admin", backref=backref("series", order_by=id))


class Participant(Base):
    __tablename__ = "participant"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    series_id = Column(Integer, ForeignKey("series.id"))
    buy_ins = Column(Integer)

    series = relationship("Series", backref=backref("participant", order_by=id))


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    series_id = Column(Integer, ForeignKey("series.id"))
    winner_id = Column(Integer, ForeignKey("participant.id"), nullable=True)

    series = relationship("Series", backref=backref("game", order_by=id))
    winner = relationship("Participant", backref=backref("game", order_by=id))


def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///op.db", echo=True)
    Session = sessionmaker(bind=ENGINE)
    return Session()


def main():
    pass


if __name__ == "__main__":
    main()
