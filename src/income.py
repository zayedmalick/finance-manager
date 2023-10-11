from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer)
    source = Column(String)
    date = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f"Income: Amount={self.amount}, Source={self.source}, Date={self.date}"

engine = create_engine('sqlite:///data.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_income(income):
    session = Session()
    session.add(income)
    session.commit()
    session.close()

def get_income_data():
    session = Session()
    incomes = session.query(Income).all()
    session.close()
    return incomes
