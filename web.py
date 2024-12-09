from sqlalchemy.orm import sessionmaker
from Final import Customer, Employees
from sqlalchemy import create_engine, func
import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
import random 

# creates connection to DataBase
engine = create_engine('sqlite:///finalchat.db')
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    print("Welcome to you Database")
    print("1. Make appointment")
    print("2. Add employee ")
    choice = input("Enter choice: ")

    if choice == "1":
        make_appointment()
    elif choice == "2":
        add_employee()
    else:
        print("invalid option. please select a valid option")
def add_employee():
    f_name = input("Enter first name: ").strip()
    L_name = input("Enter Last name: ").strip()
    Labor_hours = 10
    employee = Employees(f_name=f_name, L_name=L_name, labor_hours=Labor_hours)
    session.add(employee)
    session.commit()
    print(f"employee has been added with Employee: {employee.Employee_ID}")
def make_appointment():
    C_f_name = input("Enter client first name: ").strip()
    C_l_name = input("Enter client last name: ").strip()
    email = input("Email: ")
    Automobile_type = input("Enter make and model: ")
    #customer_ID = random.randint(1,1000)

    customer = Customer(C_f_name=C_f_name, C_l_name=C_l_name,email=email,Automobile_type=Automobile_type)
    session.add(customer)
    session.commit()
    print(f"Customer {customer.customer_ID} added")


if __name__ == "__main__":
    main_menu()
