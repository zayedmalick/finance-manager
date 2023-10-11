from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer)
    category = Column(String)
    date = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f"Expense: Amount={self.amount}, Category={self.category}, Date={self.date}"

engine = create_engine('sqlite:///data.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_expense(expense):
    session = Session()
    session.add(expense)
    session.commit()
    session.close()

def get_expense_data():
    session = Session()
    expenses = session.query(Expense).all()
    session.close()
    return expenses
