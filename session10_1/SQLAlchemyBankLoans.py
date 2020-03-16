"""
Before you read this working implementation,
please review the SQLAlchemyTutorial to walk through the steps of
initialising a simple SQLAlchemy ORM on Python
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import select

engine = create_engine('sqlite:///database.db')
engine.connect()

Base = declarative_base()

class Clients(Base):
    __tablename__ = 'clients'
    CLIENTNUMBER = Column(Integer, primary_key = True)
    FIRSTNAME  = Column(Text)
    SURNAME = Column(Text)
    EMAIL Column(Text)
    PHONE Column(Text)

    def __repr__(self):
        return(f'<Client(id={self.CLIENTNUMBER}, name={self.SURNAME})>')


class Loans(Base):
    __tablename__ = 'loans'
    ACCOUNTNUMBER =  Column(Integer)# INTEGER, A unique integer to identify this account
    CLIENTNUMBER = Column(Integer, ForeignKey('clients.CLIENTNUMBER')) # INTEGER, -- An integer to identify the client (clients may have more than one account)
    STARTDATE =  Column(DateTime)# -- The time that this account was created
    STARTMONTH =  Column(Integer)# -- The month for which the first repayment is due (201805 means May 2018)
    TERM =  Column(Integer)# INTEGER, -- Over how many months the loan must be repaid
    REMAINING_TERM =  Column(Integer) #INTEGER, -- How many months remain
    PRINCIPALDEBT = Column(Numeric(11,2)) #NUMERIC(11, 2), -- The size of the initial loan
    ACCOUNTLIMIT = Column(Numeric(11,2)) #NUMERIC(11, 2), --
    BALANCE Column(Numeric(11,2)) #NUMERIC(11, 2), -- How much is currently owed
    STATUS Column(Text(11)) #VARCHAR(11), -- Human readable status - e.g. "PAID OFF", "ARREARS", "NORMAL"

    def __repr__():
        return(f'<Loan(acc={self.ACCOUNTNUMBER}, client={self.CLIENTNUMBER})>')

#
#
# class User(Base):
# 	__tablename__ = 'users'
# 	id = Column(Integer, primary_key = True)
# 	name = Column(Text)
# 	insurance_id = Column(Integer)
#
# 	def __repr__(self):
# 		return "<User(id={0}, name={1}, insurance_id={2})>".format(self.id, self.name, self.insurance_id)
#
# class Insurance(Base):
# 	__tablename__ = 'insurance'
# 	id = Column(Integer, ForeignKey('users.insurance_id'), primary_key = True)
# 	claim_id = Column(Integer)
# 	users = relationship(User)
#
# 	def __repr__(self):
# 		return "<Insurance(id={0}, claim_id={1}>".format(self.id, self.claim_id)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

clients_info = [(1, 'Robert', 'Warren', 'RobertDWarren@teleworm.us', '(251) 546-9442'),
                (2, 'Vincent', 'Brown', 'VincentHBrown@rhyta.com', '(125) 546-4478'),
                (3, 'Janet', 'Prettyman', 'JanetTPrettyman@teleworm.us', '(949) 569-4371'),
                (4, 'Martina', 'Kershner', 'MartinaMKershner@rhyta.com', '(630) 446-8851'),
                (5, 'Tony', 'Schroeder', 'TonySSchroeder@teleworm.us', '(226) 906-2721'),
                (6, 'Harold', 'Grimes', 'HaroldVGrimes@dayrep.com', '(671) 925-1352')]
clients_key = ['CLIENTNUMBER', 'FIRSTNAME', 'SURNAME', 'EMAIL', 'PHONE']

for i in range(len(clients_info)):
    session.add(Clients(**dict(zip(clients_info[i], clients_key))))

session.commit()

# session.add(User(id = 1, name = "What's His Name", insurance_id = 1))
# session.add(Insurance(id = 1, claim_id = 1))
# session.commit()


# Query Everyone who owes more than $5,000 on an account:
SELECT FIRSTNAME, SURNAME, BALANCE FROM Loans
    JOIN Clients ON Loans.CLIENTNUMBER = Clients.CLIENTNUMBER
    WHERE BALANCE > 5000.00;

j = Clients.join(Loans, Loans.c.CLIENTNUMBER=Clients.c.CLIENTNUMBER)
stmt = select([Loans.FIRSTNAME, Loans.SURNAME, Loans.BALANCE]).select_from(j)

# students.join(addresses, students.c.id == addresses.c.st_id)


# print(session.query(User).all())
