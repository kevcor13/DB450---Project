from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
import random

# Define a base class for the models
Base = declarative_base()

class Parts(Base):
    __tablename__ = 'Parts'
    part_id = Column(Integer, primary_key=True, autoincrement=True)
    Part_name = Column(String, nullable=False)
    part_price = Column(Integer, nullable=False)

class Employees(Base):
    __tablename__ = 'Employees'
    Employee_ID = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String, nullable=False)
    L_name = Column(String, nullable=False)
    labor_hours = Column(Integer, nullable=False)

class Customer(Base):
    __tablename__ = 'Customer'
    customer_ID = Column(Integer, primary_key=True, autoincrement=True)
    C_f_name = Column(String, nullable=False)
    C_l_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    Automobile_type = Column(String, nullable=False)

class Appointments(Base):
    __tablename__ = 'Appointments'
    appointment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('Customer.customer_ID'), nullable=False)
    Status = Column(String, nullable=False)
    EmployeeID = Column(Integer, ForeignKey('Employees.Employee_ID'), nullable=False)
    Date = Column(String, nullable=False)

    customer = relationship('Customer', back_populates='appointments')
    employee = relationship('Employees', back_populates='appointments')

class NeededParts(Base):
    __tablename__ = 'NeededParts'
    part_id = Column(Integer, ForeignKey('Parts.part_id'), primary_key=True)
    appointment_id = Column(Integer, ForeignKey('Appointments.appointment_id'), primary_key=True)

    part = relationship('Parts', back_populates='needed_parts')
    appointment = relationship('Appointments', back_populates='needed_parts')

class Invoice(Base):
    __tablename__ = 'Invoice'
    appointment_id = Column(Integer, ForeignKey('Appointments.appointment_id'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('Customer.customer_ID'), nullable=False)
    TotalCost = Column(Integer, nullable=False)

    customer = relationship('Customer')

Customer.appointments = relationship('Appointments', back_populates='customer', cascade="all, delete-orphan")
Employees.appointments = relationship('Appointments', back_populates='employee', cascade="all, delete-orphan")
Parts.needed_parts = relationship('NeededParts', back_populates='part', cascade="all, delete-orphan")
Appointments.needed_parts = relationship('NeededParts', back_populates='appointment', cascade="all, delete-orphan")

# Create a database engine
engine = create_engine('sqlite:///finalchat.db')

# Create all tables
Base.metadata.create_all(engine)

# Setup session
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    print("Welcome to your Database")
    print("1. Make appointment")
    print("2. Add employee")
    choice = input("Enter choice: ")

    if choice == "1":
        make_appointment()
    elif choice == "2":
        add_employee()
    else:
        print("Invalid option. Please select a valid option.")

def add_employee():
    f_name = input("Enter first name: ").strip()
    L_name = input("Enter last name: ").strip()
    Labor_hours = 10  # Assuming a default labor hours
    employee = Employees(f_name=f_name, L_name=L_name, labor_hours=Labor_hours)
    session.add(employee)
    session.commit()
    print(f"Employee has been added with Employee ID: {employee.Employee_ID}")

def make_appointment():
    C_f_name = input("Enter client first name: ").strip()
    C_l_name = input("Enter client last name: ").strip()
    email = input("Enter email: ")
    Automobile_type = input("Enter make and model: ")
    
    customer = Customer(C_f_name=C_f_name, C_l_name=C_l_name, email=email, Automobile_type=Automobile_type)
    session.add(customer)
    session.commit()
    print(f"Customer {customer.customer_ID} added")

if __name__ == "__main__":
    main_menu()
