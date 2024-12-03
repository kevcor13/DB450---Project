from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a base class for the models
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    premium_months = Column(Integer, default=0)

# Create a database engine
engine = create_engine('sqlite:///askdy.db')

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a user
new_user = User(username='test_user', password='securepassword')
session.add(new_user)
session.commit()

print("User added successfully.")
